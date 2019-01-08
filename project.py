import numpy as np
from math import *
#import Tkinter as Tk

points = [[1,1,1], [1,1,0], [1,0,1], [1,0,0], [0,1,1], [0,1,0], [0,0,1], [0,0,0]]
class Camera:
        """pos je 3d array za pozicijo, rot za rotacijo v stopinjah"""
        def __init__(self, pos, rot, display):
                self.x = pos[0]
                self.y = pos[1]
                self.z = pos[2]
                self.psi = radians(rot[0])
                self.theta = radians(rot[1])
                self.phi = radians(rot[2])
                self.ex = display[0]
                self.ey = display[1]
                self.ez = display[2]
                
                

camera1 = Camera([5, 5, 5], [45, 45, 90], [2, 2, 10])

def projection(camera, point):
        a = np.array(point)-np.array([camera.x, camera.y, camera.z])
        r = np.array([camera.psi, camera.theta, camera.phi])
        d = []
        d.append(cos(r[1])*(sin(r[2])*a[1]+cos(r[2])*a[0])-sin(r[1])*a[2])
        d.append(sin(r[0])*(cos(r[1])*a[2]+sin(r[1])*(sin(r[2])*a[1]+cos(r[2])*a[0]))+cos(r[0])*(cos(r[2])*a[1]-sin(r[2])*a[0]))
        d.append(cos(r[0])*(cos(r[1])*a[2]+sin(r[1])*(sin(r[2])*a[1]+cos(r[2])*a[0]))-sin(r[0])*(cos(r[2])*a[1]-sin(r[2])*a[0]))
        b = np.array([camera.ez*d[0]/d[2]+camera.ex, camera.ez*d[1]/d[2]+camera.ey])
        print(b)        

"""master = Tk.Tk()
w= Tk.canvas(master)"""
for i in points:
        projection(camera1, i)
