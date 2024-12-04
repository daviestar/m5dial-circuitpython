def clamp(n, minN, maxN):
  return max(min(maxN, n), minN)

class USBSerialReader:
  """ Read a line from USB Serial (up to end_char), non-blocking, with optional echo """
  def __init__(self):
    self.s = ''
  def read(self,end_char='\n', echo=True):
    import sys, supervisor
    n = supervisor.runtime.serial_bytes_available
    if n > 0:                    # we got bytes!
      s = sys.stdin.read(n)    # actually read it in
      if echo: sys.stdout.write(s)  # echo back to human
      self.s = self.s + s      # keep building the string up
      if s.endswith(end_char): # got our end_char!
        rstr = self.s        # save for return
        self.s = ''          # reset str to beginning
        return rstr
    return None
