# from kivy.graphics import Rectangle
import PIL.Image
import pygame
from arcade.texture import Texture
from PIL import Image
from utils__ import *
import arcade
import nutils

class BD: # "BD" from "Building"
    MINE          = "mine"
    SAWMILL       = "sawmill"
    CLAYHOLE      = "clayhole"
    MINT          = "mint"
    MARKET        = "market"
    BARRACKS      = "barracks"
    TEMPLE        = "temple"
    OBSERVATORIUM = "observatorium"
    PYRAMID       = "pyramid"
    EMPTY         = "empty"

class asImage:

    prefix = "_temp"

    def __init__(self, path: str, pos: (int, int)):
        self._img = Image.open(path)
        self.siz  = (pos[0], pos[1])
        self.img  = self.res((self.siz[0], self.siz[1]), path) # path to resized _img
        self.pil  = Image.open(self.img)         # PIL-opened form
        self.py   = pygame.image.load(self.img)  # PyGame Surface

    def res(self, size: (int, int), path: str) -> str:
        fpath = f"{self.prefix}/{path}"

        with self._img as i:
            ret = i.resize(size)
            ret.save(fpath)

        return fpath

class Game:
    """Class managing every element of the game"""
    RES_MOD = 2    # resources per building

    def __init__(self, screen: pygame.Surface):
        self.turn      = 1
        self.invasions = 0
        self.blessings = 0
        self.trade     = False
        self.buildings = Buildings(screen)
        self.resources = Resources()
        self.points    = {"technology": 0, "diplomacy": 0}
        self.army      = []

    def draw(self):
        self.buildings.draw()
        self.resources.draw()

class Warrior:

    class KIND(Enum):
        CHARIOT   = "chariot"
        ARCHER    = "archer"
        SWORDSMAN = "swordsman"

    def __init__(self, kind: KIND):
        self.type: Warrior.KIND = kind
        self.upgrade: bool      = False

class Resources:
    """Class managing every resource in the game"""

    def __init__(self):
        self.STONE = 0
        self.WOOD  = 0
        self.CLAY  = 0
        self.GOLD  = 0

    def gatherResources(self, slots: dict):
        modifier = 2
        for building in slots:
            match building:
                case BD.MINE:     self.STONE += modifier
                case BD.SAWMILL:  self.WOOD  += modifier
                case BD.CLAYHOLE: self.CLAY  += modifier
                case BD.MINT:     self.GOLD  += modifier

    def draw(self):
        pass

class Buildings:
    build_size = 64

    def __init__(self, screen: pygame.Surface):
        self.objs = [Building(i, self.build_size, screen) for i in range(1,21)]

    def draw(self):
        for obj in self.objs:
            obj.draw()


class Buildings_:
    """Class managing buildings during the game"""

    build_size = 64

    def __init__(self):
        """Creates 20 slots of buildings (initially empty)"""
        self.objs  = {str(i): Building(i, self.build_size) for i in range(1,21)}
        self.slots = {str(i): "empty" for i in range(1, 21)}
        self.is_built = {BD.MARKET: False,
                         BD.TEMPLE: False,
                         BD.PYRAMID: False}

        self.bs = self.build_size #shortener

    def build(self, slot: int, building: BD):
        """Creates building on empty slot"""
        if not 0 < slot < 21: raise ValueError(f"Tried to build in slot {slot} which is outside of range for [Buildings] class")

        if self.slots[str(slot)] == "empty": self.slots[str(slot)] = building
        else:                                print ("!!!!!!!!!!!! SLOT IS TAKEN !!!!!!!!!!!!!")

    def destroy(self, slot: int):
        """Removes building from the slot"""
        self.slots[str(slot)] = "empty"

    def read(self) -> dict: ## TODO: Isn't it a bit redundant alias for 'self.slots'?
        """Returns slots dictionary"""
        return self.slots

    def load(self, save: dict):
        """Reads loaded save list"""
        self.slots = save["builds"]

    @staticmethod
    def fullRect() -> ((int, int), (int, int)):
        """Returns position of whole GUI element, as tuple of start/end tuples"""
        return (0, 0), (Buildings.build_size*10, Buildings.build_size*2)

    def slotRect(self, slot: int) -> (int, int):
        """Returns position of specific slot (width/height are under self.bs)"""
        recs = cells(0, 100)
        posnum = int(slot) - 1
        if posnum < 10: x_mod = posnum * self.bs;        y_mod = 64
        else:           x_mod = (posnum - 10) * self.bs; y_mod = 128
        return recs[0] + x_mod, recs[1] - y_mod

    def isClicked(self, pos_clicked: (int, int)) -> bool:
        """Returns slot that was clicked (or 0 if not)"""
        rect = self.fullRect()
        return nutils.iterateOverPos((rect[0][0], rect[0][1], rect[1][0], rect[1][1]), (pos_clicked[0], pos_clicked[1]))
        # return 0

    def draw(self):
        """Draws slots on screen"""
        recs = cells(0, 100)
        x_move = 32
        for i in self.slots:
            posnum = int(i)-1
            if posnum < 10: x_mod = posnum*self.bs + x_move;      y_mod = 64
            else:           x_mod = (posnum-10)*self.bs + x_move; y_mod = 128

            arcade.draw_texture_rectangle(recs[0]+x_mod, recs[1]-y_mod, self.bs, self.bs,
                                          Texture(f"{self.slots[i]}", Image.open(f"assets/builds/{self.slots[i]}.png")))
            # Rectangle(source=f"assets/builds/{self.slots[i]}.png",
            #           pos=(recs[0]+x_mod, recs[1]-y_mod),
            #           size=(self.bs, self.bs))
            print(i, recs[0]+x_mod, recs[1]-y_mod)

class Building:

    def __init__(self, slot: int, tile_size: int, screen: pygame.Surface):
        self.slot: int = validSlot(slot)
        self.tile: int = tile_size
        self.type: BD  = BD.EMPTY
        self.pos       = self.init_pos(slot, tile_size, 32)
        self.scr       = screen
        #self.draw()

    # sets tuple of tuples (init_pos, size) of where Building tile is
    def init_pos(self, slot: int, tile_size: int, x_move: int) -> (int, int):
        recs = cells(0, 100)
        if slot < 10:
            x_mod = slot*tile_size + x_move
            y_mod = 64
        else:
            x_mod = (slot-10)*tile_size + x_move
            y_mod = 128
        return recs[0]+x_mod, recs[1]-y_mod

    def draw(self):
        # arcade.draw_texture_rectangle(self.pos[0][0], self.pos[0][1], self.pos[1][0], self.pos[1][1],
        #                               Texture(f"Building_{self.slot}", Image.open(f"assets/builds/{self.type}.png")))
        self.scr.blit(asImage(f"assets/builds/{self.type}.png", cells(10, 10)).py, (self.pos[0], self.pos[1]))

    def build(self, variant: BD):
        self.type = variant
        self.draw()

    def destroy(self):
        self.type = BD.EMPTY
        self.draw()

#==============================================================================
# HELPER FUNCS
#==============================================================================
# Checks if slot is within 1-20 range
def validSlot(n: int):
    if 1 <= n <= 20: return n
    else: raise ValueError("Invalid slot number (is not between 1 and 20)")