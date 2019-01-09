#!/usr/bin/env python3

import numpy as np
from time import sleep, clock
from math import *
import tkinter as tk

points = [[1,1,1], [1,1,-1], [1,-1,1], [1,-1,-1], [-1,1,1], [-1,1,-1], [-1,-1,1], [-1,-1,-1]]

class Camera:
	"""pos je 3d array za pozicijo, rot za rotacijo v stopinjah"""
	def __init__(self, pos, rot, display):
		self.x = pos[0]
		self.y = pos[1]
		self.z = pos[2]
		self.psi = radians(rot[0]%360)
		self.theta = radians(rot[1]%360)
		self.phi = radians(rot[2]%360)
		self.ex = display[0]
		self.ey = display[1]
		self.ez = display[2]


camera1 = Camera([5, 5, 7], [45, 0, 135], [0, 0, 20])

def projection(camera, point):
	#a = vektor tocke - vektor kamere
	a = np.array(point)-np.array([camera.x, camera.y, camera.z])
	r = np.array([camera.psi, camera.theta, camera.phi])
	u = np.array([[1,0,0], [0,cos(r[0]),-sin(r[0])], [0,sin(r[0]),cos(r[0])]]).transpose()
	v = np.array([[cos(r[1]),0,sin(r[1])], [0, 1, 0], [-sin(r[1]),0,cos(r[1])]]).transpose()
	w = np.array([[cos(r[2]),-sin(r[2]),0], [sin(r[2]),cos(r[2]),0], [0, 0, 1]]).transpose()
	d = np.append(a.dot(w).dot(v).dot(u), [1])
	e = np.array([[1,0,0,0], [0,1,0,0], [-camera.ex/camera.ez, -camera.ey/camera.ez, 1, -1/camera.ez], [0,0,0,1]]).transpose()
	f = d.dot(e)
	b = np.array([f[0]/f[3],f[1]/f[3]])
	return b

def circle(array, canvas):
	canvas.create_oval(50*array[0]+249, 50*array[1]+249, 50*array[0]+251, 50*array[1]+251, fill= "blue")



master = tk.Tk()
w = tk.Canvas(master, width=500, height=500)
w.pack()

speed=7


while True:
	sleep(0.01)
	camera1.phi = -speed*clock()+pi
	camera1.x = sin(speed*clock())*5
	camera1.y = -cos(speed*clock())*5
#	camera1.psi

	#print("x: {0:.4f}, y: {1:.4f}, psi: {2:.4f}".format(camera1.x, camera1.y, degrees(camera1.psi)))
	#print("x: {}, y: {}".format)
	#camera1.ez+=2
	w.delete("all")
	dots=[]
	for i in points:
		dots.append(projection(camera1, i))
	print(dots)
	for j in [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,6],[7,3],[7,6],[7,5],[4,6],[4,5]]:
		w.create_line(50*dots[j[0]][0]+250, 50*dots[j[0]][1]+250, 50*dots[j[1]][0]+250, 50*dots[j[1]][1]+250)
	master.update()

