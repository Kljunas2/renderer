#!/usr/bin/env python3

import tkinter as tk
from time import sleep, clock
from math import*

import projection

def circle(array, canvas):
	canvas.create_oval(
		50*array[0]+249, 50*array[1]+249,
		50*array[0]+251, 50*array[1]+251,
		fill= "blue")


camera1 = projection.Camera([5, 5, 4], [20, 0, 135], [0, 0, 20])
points = [[1,1,1], [1,1,-1], [1,-1,1], [1,-1,-1], [-1,1,1], [-1,1,-1], [-1,-1,1], [-1,-1,-1]]

master = tk.Tk()
w = tk.Canvas(master, width=500, height=500)
w.pack()

speed=1


while True:
	sleep(0.01)
	camera1.phi = -speed*clock()+pi
	camera1.x = sin(speed*clock())*5
	camera1.y = -cos(speed*clock())*5
	w.delete("all")
	dots=[]
	for i in points:
		dots.append(camera1.projection(i))
	for j in [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],
		[2,6],[7,3],[7,6],[7,5],[4,6],[4,5]]:
		w.create_line(50*dots[j[0]][0]+250, 50*dots[j[0]][1]+250,
				50*dots[j[1]][0]+250, 50*dots[j[1]][1]+250)
	master.update()
