import board
from displayio import TileGrid
from adafruit_imageload import load

def setup():
  img, palette = load("assets/nts2.gif")
  x = round((board.DISPLAY.width - img.width) / 2)
  y = round((board.DISPLAY.height - img.height) / 2)
  return TileGrid(img, x=x, y=y, pixel_shader=palette)
