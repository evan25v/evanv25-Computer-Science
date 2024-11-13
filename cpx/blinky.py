#First impor board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time


# when program finishes, board enters a waiting state
while True:
    cp.pixels.fill((0, 225, 0))      # Turn all lights green
    time.sleep(0.376)   # Wait for 376 milliseconds 
    
    cp.pixels.fill((0, 0, 0))      # Turn all lights off 
    time.sleep(0.376)         # Wait for 376 milliseconds 





