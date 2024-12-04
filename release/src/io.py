import src.volume as volume
import src.button as button
import src.utils as utils

usbReader = utils.USBSerialReader()

def usbSerialReader():
  return usbReader.read(end_char=';', echo=False)

def processTask(command):
  segments = command.strip()[:-1].split(' ')

  if segments[0] == 'dial':
    verb = segments[1]
    task = segments[2]
    parameters = segments[3]

    if verb == 'SET':
      if task == 'volume':
        volume.setVolume(int(parameters))
      if task == 'power':
        button.setPower(parameters)

