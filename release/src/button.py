import board
from digitalio import DigitalInOut, Direction, Pull

# mutable power value
powerToggle = True

btn = DigitalInOut(board.KNOB_BUTTON)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

pushed = btn.value

def listenForToggle():
  global pushed, powerToggle

  if btn.value != pushed:
    pushed = btn.value
    if btn.value is False:
      powerToggle = not powerToggle

  return powerToggle

prevPowerToggle = None

def hasChanged():
  global powerToggle, prevPowerToggle
  if powerToggle != prevPowerToggle:
    prevPowerToggle = powerToggle
    return True
  return False

def setPower(onOff):
  powerToggle = onOff == 'on'
  return powerToggle
