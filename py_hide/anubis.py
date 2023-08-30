import kivy
from objects__ import Buildings, Game
from kivy.uix.widget import Widget
from kivy.app import App
from utils__ import *
import json

def save(num: int, bs: Buildings):
    naming = f"save{num}"
    with open(f"saves/{naming}_bd.json", "w") as bdfile: bdfile.write(json.dumps(bs.read(), indent=4))

def load(num: int):
    naming = f"save{num}"
    with open(f"saves/{naming}_bd.json", "r") as bdfile: builds = json.loads(bdfile.read())

    return {"builds": builds}

class ScreenRound(Widget):

    def __init__(self, game: Game, **kwargs):
        super(ScreenRound, self).__init__(**kwargs)
        # VALUES

        with self.canvas:
            j = Buildings()
            # this is how game will load again
            j.load(load(15)) # the same numer of save (save15)
            j.draw()
            print(j.isClicked((5, 185)))
            #hhmmmmm, let's load the saved game!

            #j.load(load(0))
            #j.build(1, BD.MINE); j.build(2, BD.MINE)
            #save(0, j)
            #load(0)

    # def on_touch_down(self, touch):
    #     if super().on_touch_down(touch):
    #         return True
    #     if not self.collide_point(touch.x, touch.y):
    #         return False
    #     print('you touched me!')
    #     return True

class AncientSettlers(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Ancient Settlers: By the Hand of Anubis"
        self.icon  = "assets/icon.png"
        self.game  = Game()

    def build(self):
        return ScreenRound(game=self.game)

AncientSettlers().run()
