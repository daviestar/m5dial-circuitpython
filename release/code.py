import board
import time
from displayio import Group

import src.io as io
import src.encoder as encoder
import src.button as button
# import src.touchscreen as touchscreen
import src.volume as volume
import src.radio as radio

board.DISPLAY.rotation = 180
board.DISPLAY.brightness = 1

screen = Group()
screen.append(radio.setup())
screen.append(volume.setup())
board.DISPLAY.root_group = screen

while True:
  command = io.usbSerialReader()
  if command:
    io.processTask(command)

  powerToggle = button.listenForToggle()
  if button.hasChanged():
    if powerToggle is True:
      board.DISPLAY.brightness = 1
      print('dsp SET power on;')
    else:
      board.DISPLAY.brightness = 0
      print('dsp SET power off;')

  if powerToggle is True:
    val = encoder.change()
    if val != 0:
      level = volume.setFromEncoder(val)
      print(f'dsp SET volume {level};')
    # if touchscreen.ft.touched:
    #   print(touchscreen.ft.touches)

  time.sleep(.15)
