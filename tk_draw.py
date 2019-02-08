#!/usr/bin/env python3

import tkinter as tk
from time import sleep, clock
from math import*
import numpy as np

import projection
import stl_parser as parser

def circle(array, canvas):
	canvas.create_oval(
		50*array[0]+249, 50*array[1]+249,
		50*array[0]+251, 50*array[1]+251,
		fill= "blue")


def project_line(camera, point1, point2):
	return [camera.projection(i) for i in [point1, point2]]


def draw_line(canvas, point1, point2, colour="black"):
	canvas.create_line(50*point1[0]+250, 50*point1[1]+250,
			   50*point2[0]+250, 50*point2[1]+250, fill=colour)

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def draw_face(canvas, face):
	normal = camera1.normal(face[3], face[4])
	if normal > 1:
		return
	loop = list(map(camera1.projection, face[:3]))
	#print(normal)
	coords = tuple(map(lambda x: 50*x+250, [loop[0][0], loop[0][1], loop[1][0], loop[1][1], loop[2][0], loop[2][1]]))
	fill = _from_rgb((275-int(normal*240),275-int(normal*240),275-int(normal*240)))
	canvas.create_polygon(coords, fill=fill)



with open("shapes/cube.stl", "r") as f:
	solid = parser.parse(f.read())
	print("Parsing done.")



camera1 = projection.Camera([20, 20, 10], [75, 0, 0], [0, 0, 40])
#points = [[1,1,1], [1,1,-1], [1,-1,1], [1,-1,-1], [-1,1,1], [-1,1,-1], [-1,-1,1], [-1,-1,-1]]


master = tk.Tk()
w = tk.Canvas(master, width=500, height=500)
w.pack()

speed=10



while True:
	w.delete("all")
	sleep(0.01)
	camera1.phi = -speed*clock()+pi
	camera1.x = sin(speed*clock())*40
	camera1.y = -cos(speed*clock())*40
	camera1.update()

	print(camera1.x, camera1.y, camera1.psi, camera1.theta, camera1.phi)

	x = project_line(camera1, [0,0,0], [1,0,0])
	draw_line(w, x[0], x[1], "red")
	y = project_line(camera1, [0,0,0], [0,1,0])
	draw_line(w, y[0], y[1], "green")
	z = project_line(camera1, [0,0,0], [0,0,1])
	draw_line(w, z[0], z[1], "blue")


	for i in solid:
		draw_face(w, i)

	#dots=[]
	#for i in points:
	#	dots.append(camera1.projection(i))
	#for j in [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],
	#	[2,6],[7,3],[7,6],[7,5],[4,6],[4,5]]:
	#	draw_line(w, dots[j[0]], dots[j[1]], "black")
	master.update()
