from displayio import Group
from adafruit_display_shapes.arc import Arc
from adafruit_display_text.label import Label
from adafruit_bitmap_font.bitmap_font import load_font

import src.utils as utils

# mutable volume value
value = 0

foreColour = 0xff5400
bgColour = 0x2a2a2a
resolution = 100

label = Label(
  load_font('assets/font-24.bdf'),
  color = foreColour,
  anchored_position = [120, 225],
  anchor_point = [0.5, 1]
)
label.text = str(value)

group = Group()
gauge = Group()
group.append(gauge)
group.append(label)

def setup():
  for n in range(resolution):
    angle = 270 / resolution
    direction = 180 + 45 - (angle * n)
    segment = Arc(
      x = 120,
      y = 120,
      radius = 116,
      arc_width = 8,
      segments = 6,
      angle = angle,
      direction = direction - (angle / 2),
      fill = foreColour if n <= value else bgColour
    )
    gauge.append(segment)

  return group

def setFromEncoder(change):
  factor = 4
  return setVolume(value + (change * factor))

def setVolume(newValue):
  global value
  value = utils.clamp(newValue, 0, 100)

  label.text = str(value)
  updateGauge()

  return value

def updateGauge():
  for n in range(resolution):
    if n < value:
      if gauge[n].fill != foreColour:
        gauge[n].fill = foreColour
    else:
      if gauge[n].fill != bgColour:
        gauge[n].fill = bgColour
