import board
from adafruit_focaltouch import Adafruit_FocalTouch
from digitalio import DigitalInOut, Direction

i2c = board.I2C()
irq = DigitalInOut(board.TOUCH_IRQ)
irq.direction = Direction.INPUT
ft = Adafruit_FocalTouch(i2c, debug=False, irq_pin=irq)
