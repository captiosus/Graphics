import math
import random

def create():
    image = "P3\n500 500 255\n"
    for x in range(500):
        for y in range(500):
            red = y % 256
            green = math.tan(x) % 256
            blue = math.hypot((pow(x, 2) + 5 * x + 18), y) % 256
            image += "%d %d %d " % (red, green, blue)
        image += "\n"
    with open("starting-image.ppm", "w+") as f:
        f.write(image)

create()
