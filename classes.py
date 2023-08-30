from utils import cell, Axis
from enum import Enum

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

# here all information about player are stored
class Player:

    def __init__(self):
        self.turn:      int  = 1
        self.invasions: int  = 0
        self.blessings: int  = 0
        self.trade:     bool = False
        self.resources: Resources      = Resources()
        self.points:    dict[str, int] = {"technology": 0, "diplomacy": 0}
        self.army:      list[Warrior]  = []

    def tick(self, arc_handler):
        """
        Here tick update is made, including drawing on screen

        Parameters:
        ----------
        arc_handler : arcade object
            Handler of 'arcade' object used by arcade lib
        """
        arc_handler.draw_text("Hello from test", start_x=cell(0, Axis.X), start_y=cell(0, Axis.Y), color=arc_handler.color.BLACK, font_size=50)

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