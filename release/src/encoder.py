import board
from rotaryio import IncrementalEncoder

hw = IncrementalEncoder(board.ENC_B, board.ENC_A)

prevEncoderPosition = 0

def change():
  global prevEncoderPosition
  change = hw.position - prevEncoderPosition
  prevEncoderPosition = hw.position
  return change

def getValue():
  return hw.position - prevEncoderPosition
