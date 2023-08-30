from kivy.graphics import Rectangle
from enum import Enum
from utils__ import *
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

class Game:
    """Class managing every element of the game"""
    RES_MOD = 2    # resources per building

    def __init__(self):
        self.turn      = 1
        self.invasions = 0
        self.blessings = 0
        self.trade     = False
        self.buildings = Buildings()
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
    """Class managing buildings during the game"""

    build_size = 64

    def __init__(self):
        """Creates 20 slots of buildings (initially empty)"""
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
        for i in self.slots:
            posnum = int(i)-1
            if posnum < 10: x_mod = posnum*self.bs;      y_mod = 64
            else:           x_mod = (posnum-10)*self.bs; y_mod = 128

            Rectangle(source=f"assets/builds/{self.slots[i]}.png",
                      pos=(recs[0]+x_mod, recs[1]-y_mod),
                      size=(self.bs, self.bs))
            print(i, recs[0]+x_mod, recs[1]-y_mod)