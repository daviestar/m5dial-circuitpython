## Install CircuitPython

https://circuitpython.org/board/m5stack_dial

Download the latest CircuitPython .uf2 file, and the latest tinyuf2 Bootloader .zip. If the bootloader link doesn't work, go to https://github.com/adafruit/tinyuf2/releases, select the latest release and download the tinyuf2-m5stack_stamps3-x.x.x.zip file.

### Flash bootloader

Reset the M5Dial by plugging it in and holding the reset button (under sticker on PCB) then pressing the other reset button on the bottom right.

Enter boot mode by unplugging usb, holding the reset button on the bottom right while plugging back in.

Go to https://adafruit.github.io/Adafruit_WebSerial_ESPTool. Change the Baud rate to 460800. Click connect, and the WebSerial API should show M5Stack on cu.usbmodemxxxxx on MacOS, and show "Paired" (if not, try initiating boot mode again). Then choose "Erase" to erase the flash storage on device. Then unzip the tinyuf2 release downloaded above, and choose the 'combined.bin' and flash to the device. Then click the reset button on the bottom right one last time.

The "hello world" script should then appear on the display.

## Usage

### Console

```bash
ls /dev/*
```

Find the address that starts with /dev/tty.usbmodemxxxxx.

Install https://github.com/tio/tio.

Then run

```bash
tio /dev/tty.usbmodemxxxxxx
```

Once connected, hit Ctrl+C to enter REPL, then type:

```python
import board
dir(board)
```

### Filesystem

A disk should have mounted named CIRCUITPY, open this with VSCode and edit code.py.

The M5Dial should reboot each time code.py is saved.


