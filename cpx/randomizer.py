from adafruit_circuitplayground import cp
import random

while True:
    if cp.shake(shake_threshold = 15.0):
        for i in range(10):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255) 
            cp.pixels[i] = (r, g, b)
            cp.pixels.show()