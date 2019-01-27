"""from write_png import *
save_png([["0xffFF0000", 0xffFFFF00],
           [0xff00aa77, 0xff333333]], 'test_grid.png')
class RGBA:
        def __init__(self, red, green, blue, alpha):         
                self.r = red if red < 256 else 255
                self.g = green if green < 256 else 255
                self.b = blue if blue < 256 else 255
                self.a = alpha if alpha < 256 else 255

        def __call__(self):
                alpha = format(self.a, "02x")
                red = format(self.r, "02X")
                green = format(self.g, "02X")
                blue = format(self.b, "02X")
                return "".join(["0x", alpha, red, green, blue])

from random import randint
b = [[RGBA(i, j, 255, 255)() for j in range(10)] for i in range(255)]
save_png(b, "img.png")
cb = [[0xff00AA00 for j in range(10)] for i in range(255)]
save_png(cb, "i.png")
print(cb)
"""
import numpy
