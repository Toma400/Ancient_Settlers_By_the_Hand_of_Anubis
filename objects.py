from kivy.graphics import Rectangle
from utils import *

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

class Buildings:

    build_size = 64

    def __init__(self):
        """Creates 20 slots of buildings (initially empty)"""
        self.slots = {str(i): "empty" for i in range(1, 21)}

        self.bs = self.build_size #shortener

    def build(self, slot: int, building: BD):
        """Creates building on empty slot"""
        if not 0 < slot < 21: raise ValueError(f"Tried to build in slot {slot} which is outside of range for [Buildings] class")

        if self.slots[str(slot)] == "empty": self.slots[str(slot)] = building
        else:                                print ("!!!!!!!!!!!! SLOT IS TAKEN !!!!!!!!!!!!!")

    def destroy(self, slot: int):
        """Removes building from the slot"""
        self.slots[str(slot)] = "empty"

    def read(self):
        """Returns slots dictionary"""
        return self.slots

    def load(self, save: dict):
        """Reads loaded save list"""
        self.slots = save["builds"]

    def rect(self, slot: int):
        """Returns position of specific slot (width/height are under self.bs)"""
        recs = cells(0, 100)
        posnum = int(slot) - 1
        if posnum < 10: x_mod = posnum * self.bs;        y_mod = 64
        else:           x_mod = (posnum - 10) * self.bs; y_mod = 128
        return recs[0] + x_mod, recs[1] - y_mod

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