import kivy
from objects import BD, Buildings
from kivy.uix.widget import Widget
from kivy.app import App
from utils import *
import json

TITLE     = "Temple Settlers: By the Hand of Anubis"
DEV_CYCLE = "alpha"
VERSION   = "0.1.0"

def save(num: int, bs: Buildings):
    naming = f"save{num}"
    with open(f"saves/{naming}_bd.json", "w") as bdfile: bdfile.write(json.dumps(bs.read(), indent=4))

def load(num: int):
    naming = f"save{num}"
    with open(f"saves/{naming}_bd.json", "r") as bdfile: builds = json.loads(bdfile.read())

    return {"builds": builds}

class ScreenRound(Widget):

    def __init__(self, **kwargs):
        super(ScreenRound, self).__init__(**kwargs)
        # VALUES

        with self.canvas:
            j = Buildings()
            # this is how game will load again
            j.load(load(15)) # the same numer of save (save15)
            j.draw()
            #hhmmmmm, let's load the saved game!

            #j.load(load(0))
            #j.build(1, BD.MINE); j.build(2, BD.MINE)
            #save(0, j)
            #load(0)

class TempleSettlers(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = TITLE
        self.icon  = "assets/icon.png"

    def build(self):
        return ScreenRound()


if __name__ == '__main__':
    TempleSettlers().run()
