from utils import WinRes as WR
from classes import *
import arcade

width  = WR.X
height = WR.Y
title  = "Ancient Settlers: By the Hand of Anubis"

player = Player() # initial player

# Open the window. Set the window title and dimensions
arcade.open_window(width, height, title)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
player.tick(arcade) # rendering/drawing all things
arcade.finish_render()

arcade.run()