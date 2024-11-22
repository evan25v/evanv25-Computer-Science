#First import board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time



while True:
    if cp.button_a:
       for i in range(10):
        cp.pixels.fill[i] = ((0, 0, 225))    # Turn pixel blue
       time.sleep(0.1)    # Wait for 100ma
       cp.pixels.fill[i]= ((0, 0, 0))     # Turn off pixels 
       time.sleep(0.1)    # Wait for 100ms