#!/usr/bin/env python3

from PIL import ImageDraw, Image


import projection
import stl_parser as parser



def init(width, height):
	img = Image.new("RGBA", (width, height))
	img.putdata([0]*height*width)
	return img


def project_line(camera, point1, point2):
	return [camera.projection(i) for i in [point1, point2]]

camera1 = projection.Camera([25, -25, 10], [75, 0, 225], [0, 0, 40])


img = init(1920, 1080)
print(project_line(camera1, [1,1,1], [-1,-1,-1]))
draw = ImageDraw.Draw(img)
# draw.line(project_line(camera1, [1,1,1], [-1,-1,-1]), fill=(0,255,0,255))
img.show()
