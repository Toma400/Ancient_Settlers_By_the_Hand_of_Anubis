from utils import WinRes as WR
import arcade

width  = WR.X
height = WR.Y
title  = "Ancient Settlers: By the Hand of Anubis"

# Open the window. Set the window title and dimensions
arcade.open_window(width, height, title)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.finish_render()

arcade.run()