from PIL import Image
from random import randint

#width=1920
#height=1080

#img = Image.new("RGBA", (width, height))

def newimg(width, height):
        return Image.new("RGBA", (width, height))
