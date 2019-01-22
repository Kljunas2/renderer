#!/usr/bin/env python3

import tkinter as tk
from time import sleep, clock
from math import*
import numpy as np

import projection

def circle(array, canvas):
	canvas.create_oval(
		50*array[0]+249, 50*array[1]+249,
		50*array[0]+251, 50*array[1]+251,
		fill= "blue")

def project_line(camera, point1, point2):
	return [camera.projection(i) for i in [point1, point2]]


def draw_line(canvas, point1, point2, colour):
	canvas.create_line(50*point1[0]+250, 50*point1[1]+250,
			   50*point2[0]+250, 50*point2[1]+250, fill=colour)

def draw_face(canvas, face):
        draw_line(canvas)

camera1 = projection.Camera([0, 6, 3], [80, 0, 0], [0, 0, 200])
points = [[1,1,1], [1,1,-1], [1,-1,1], [1,-1,-1], [-1,1,1], [-1,1,-1], [-1,-1,1], [-1,-1,-1]]


master = tk.Tk()
w = tk.Canvas(master, width=500, height=500)
w.pack()

speed=1.5


while True:
	sleep(0.01)
	camera1.phi = -speed*clock()+pi
	camera1.x = sin(speed*clock())*50/clock()#NEKI NE DELA???
	camera1.y = -cos(speed*clock())*50/clock()
	#camera1.phi = sin(speed*clock())*0.1
	#camera1.y = -cos(speed*clock())*5
	#for i in range(8):
	#	points[i]=np.array([points[i]]).dot(
	#		np.array([[cos(speed),-sin(speed),0],
	#                          [sin(speed),cos(speed),0],[0, 0, 1]]).T)

	w.delete("all")
	dots=[]
	x = project_line(camera1, [0,0,0], [1,0,0])
	draw_line(w, x[0], x[1], "red")
	y = project_line(camera1, [0,0,0], [0,1,0])
	draw_line(w, y[0], y[1], "green")
	z = project_line(camera1, [0,0,0], [0,0,1])
	draw_line(w, z[0], z[1], "blue")
	for i in points:
		dots.append(camera1.projection(i))
	for j in [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],
		[2,6],[7,3],[7,6],[7,5],[4,6],[4,5]]:
		draw_line(w, dots[j[0]], dots[j[1]], "black")
	master.update()
