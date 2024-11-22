#First import board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time



while True:
   if cp.switch: 
      for i in range(5):
         cp.pixels[i] = (0, 0, 0)  # Turn off pixels 0-4
      for i in range(5, 10): 
         cp.pixels[i] = (0, 255, 0)   # Turn on pixels 5-9 Green
      else:
         for i in range(5): 
            cp.pixels[i] = (0, 255, 0)   # Turn on pixels 0-4 green
         for i in range(5, 10):
            cp.pixels[i] = (0, 0, 0)    # Tuen off pixels 5-9