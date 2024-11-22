from adafruit_circuitplayground import cp
import random
import board
import digitalio
import neopixel


pixels = neopixel(board.Neopixel, 10, brightness = 0.3)
cp.button_a = digitalio
cp.button_b = digitalio
# Set the color for the pixels 
color = (128,0, 128)  # Purple color 

while True:
    if cp.button_a:
      # Generatea random number between 10 and 10
      num_pixels = random.randint(1, 10)
      # Light up the corresponding number of pixels
      for i in range(num_pixels):
         pixels[i] = color
    while cp.buuton_a:
       pass    # Wait for the button to be released 
    if cp.button_b:
       # Turn off all the pixels
       pixels.fill((0, 0, 0))
       while cp.button_b:
          pass   # Wait for the button to be released 