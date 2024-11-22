#First import board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time
import neopixel 

pixels = neopixel



while True: 
    if cp.acceleration.x < -2:    #Tilted to the left
        pixels[1] = ((0, 255, 0))  # Green
        pixels[2] = ((0, 225, 0))  # Green
        pixels[3] = ((0, 255,0))
        pixels[6] = ((0, 0, 0))
        pixels[7] = ((0, 0, 0))
        pixels[8] = ((0, 0, 0))
    elif cp.acceleration.x > 2:   # Tilted to the right 

        pixels[1] = ((0, 0, 0))
        pixels[2] = ((0, 0, 0))
        pixels[3] = ((0, 0, 0))
        pixels[6] = ((225, 0, 0))
        pixels[7] = ((225, 0, 0))
        pixels[8] = ((225, 0, 0))
    else:
        cp.pixels.fill((0, 0, 0))    # All off if not tiled
        time.sleep(0.1)