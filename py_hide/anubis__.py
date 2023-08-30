from objects__ import Buildings, Game
from utils__ import *
import pygame_gui
import pygame
import json

def save(num: int, bs: Buildings):
    naming = f"save{num}"
    with open(f"saves/{naming}_bd.json", "w") as bdfile: bdfile.write(json.dumps(bs.read(), indent=4))

def load(num: int):
    naming = f"save{num}"
    with open(f"saves/{naming}_bd.json", "r") as bdfile: builds = json.loads(bdfile.read())

    return {"builds": builds}

pygame.init()

# screen builder
pygame.display.set_caption("Ancient Settlers: By the Hand of Anubis")
screen  = pygame.display.set_mode((Window.get(Axis.X), Window.get(Axis.Y)))
manager = pygame_gui.UIManager((Window.get(Axis.X), Window.get(Axis.Y)))
clock   = pygame.time.Clock()

# data builder
game = Game(screen) # game object to manage everything
run  = []           # add to the list to exit the program

while not run:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        manager.process_events(event)

        if event.type == pygame.QUIT or event.button == pygame.K_ESCAPE:
            run.append("!")

    manager.update(time_delta)

    screen.fill("#4B3913")
    # game.draw()
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()