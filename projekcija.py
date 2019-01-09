#!/usr/bin/env python3

import numpy as np
from time import sleep, clock
from math import *
import tkinter as tk

points = [[0, 0, 1], [1,1,1], [1,1,-1], [1,-1,1], [1,-1,-1], [-1,1,1], [-1,1,-1], [-1,-1,1], [-1,-1,-1]]

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


camera1 = Camera([5, 5, 5], [45, 45, 90], [0, 0, 200])

def projection(camera, point):
	#a = vektor tocke - vektor kamere
        a = np.array(point)-np.array([camera.x, camera.y, camera.z])
        r = np.array([camera.psi, camera.theta, camera.phi])
        d = []
        d.append(cos(r[1])*(sin(r[2])*a[1]+cos(r[2])*a[0])-sin(r[1])*a[2])
        d.append(sin(r[0])*(cos(r[1])*a[2]+sin(r[1])*(sin(r[2])*a[1]+cos(r[2])*a[0]))+cos(r[0])*(cos(r[2])*a[1]-sin(r[2])*a[0]))
        d.append(cos(r[0])*(cos(r[1])*a[2]+sin(r[1])*(sin(r[2])*a[1]+cos(r[2])*a[0]))-sin(r[0])*(cos(r[2])*a[1]-sin(r[2])*a[0]))
        b = np.array([camera.ez*d[1]/d[2]+camera.ey, camera.ez*d[0]/d[2]+camera.ex])
        return b

def circle(array, canvas):
	canvas.create_oval(array[0]+249, array[1]+249, array[0]+251, array[1]+251, fill= "blue")


master = tk.Tk()
w = tk.Canvas(master, width=500, height=500)
w.pack()
sliderp = tk.Scale(master, from_=0, to=360, orient="horizontal")
sliderp.pack()
sliderx = tk.Scale(master, from_=-5, to=5, orient="horizontal")
slidery = tk.Scale(master, from_=-5, to=5, orient="horizontal")
sliderx.pack()
slidery.pack()
speed=0.1
#camera1.ez=0

while True:
	sleep(0.01)
	camera1.psi = radians(sliderp.get())
	camera1.x = sliderx.get() #cos(speed*clock())*5
	camera1.y = slidery.get() #sin(speed*clock())*5
#	camera1.psi

	print("x: {0:.4f}, y: {1:.4f}, psi: {2:.4f}".format(camera1.x, camera1.y, degrees(camera1.psi)))
	#camera1.ez+=2
	w.delete("all")
	for i in points:
		circle(projection(camera1, i), w)
	master.update()
