# Imports
import ctypes
import os
import random
# import pyautogui
from PIL import Image, ImageDraw, ImageFilter

# variables
screen_width, screen_height = 1920, 1080 # pyautogui.size()
background = Image.new('RGB', (screen_width, screen_height))
tile_width, tile_height = screen_width / 5, screen_height / 5
draw: ImageDraw = ImageDraw.Draw(background)

# color palette
BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

rgb_1 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

rgb_2 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

rgb_3 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

rgb_4 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

rgb_5 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

rgb_6 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

colour_choice = [BLACK, WHITE, rgb_1, rgb_2, rgb_3, rgb_4, rgb_5, rgb_6]

# Step 1: create image with random coloured tiles
for y in range(0, int(screen_height / tile_height)):
    for x in range(0, int(screen_width / tile_width)):
        # random_colour = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        draw.rectangle((tile_width * x, tile_height * y, tile_width * (x + 1), tile_height * (y + 1)),
                       random.choice(colour_choice))

# Step 2: blur the image and save it
background_blured = background.filter(ImageFilter.GaussianBlur(radius=200))
background_blured.save('wallpaper_gradient.jpeg')

# Step 3: Apply as wallpaper
# SPI_SETDESKWALLPAPER = 20
# ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.# # abspath("wallpaper_gradient.jpeg"), 0)
