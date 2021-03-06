#!/usr/bin/env python3

from PIL import ImageDraw, Image


import projection
import stl_parser as parser


def init(width, height):
	img = Image.new("RGBA", (width, height))
	img.putdata([(255, 255, 255, 255)] * height * width)
	return img


def project_line(camera, point1, point2):
	tmp = [camera.projection(i) for i in [point1, point2]]
	return (tmp[0][0] + 960, tmp[0][1] + 540, tmp[1][0] + 960, tmp[1][1] + 540)


def draw_face(camera, face):
	normal = camera1.normal(face[3], face[4])
	if normal > 1:
		return

	loop = list(map(camera1.projection, face[:3]))
	coords = [tuple([(x[0] + 1) * width / 2, (x[1] + 1) * height / 2])
		for x in loop]
	shade = 255 - int(normal * 255)
	fill = (shade, shade, shade, 255)
	draw.polygon(coords, fill=fill)


width = 1920
height = 1080


camera1 = projection.Camera([10, 38, 10], [75, 0, -343], [0, 0, 10])
camera1.update()

with open("shapes/sphere.stl", "r") as f:
	solid = parser.parse(f.read())
	print("Parsing done.")

img = init(1920, 1080)
# print(project_line(camera1, [1,1,1], [-1,-1,-1]))

draw = ImageDraw.Draw(img)
for i in solid:
	draw_face(camera1, i)

img.show()
