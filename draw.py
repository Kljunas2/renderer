#!/usr/bin/env python3

from PIL import ImageDraw, Image


import projection
import stl_parser as parser



def init(width, height):
	img = Image.new("RGBA", (width, height))
	img.putdata([(255,255,255,255)]*height*width)
	return img


def project_line(camera, point1, point2):
	tmp = [camera.projection(i) for i in [point1, point2]]
	return (tmp[0][0]+960, tmp[0][1]+540, tmp[1][0]+960, tmp[1][1]+540)

def draw_face(camera, face):

#nov komentar
camera1 = projection.Camera([25, -25, 10], [75, 0, 225], [0, 0, 40])
camera1.update()

img = init(1920, 1080)
print(project_line(camera1, [1,1,1], [-1,-1,-1]))

draw = ImageDraw.Draw(img)
draw.line(project_line(camera1, [1,1,1], [1,1,-1]), fill=(0,255,0,255))
draw.line(project_line(camera1, [1,1,1], [1,-1,1]), fill=(0,255,0,255))
draw.line(project_line(camera1, [1,-1,1], [1,-1,-1]), fill=(0,255,0,255))
draw.line(project_line(camera1, [1,-1,-1], [1,1,-1]), fill=(0,255,0,255))
img.show()
