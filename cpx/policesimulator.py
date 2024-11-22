#First import board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time



while True:
    cp.pixels.fill = ((255, 0,  0))      # Flash all pixels red
    cp.sound_level(500, 0.5)    # Play 500Hz tone for 500ms
    time.sleep(0.5)


    cp.pixels.fill = ((0, 0, 255))  # Flash all pixels blue
    cp.sound_level(900, 0.5)   # Play 900Hz tone for 500ms
    time.sleep(0.5)