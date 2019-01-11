#!/usr/bin/env python3

import numpy as np
from math import *



class Camera:
	"""rot is given in degrees, ez display[2] controls field of view."""
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

	def projection(self, point):
		"""Returns input vector relative to the camera, projected onto 2d plane.
		a = input vector - camera vector
		r = rotation vector
		w, v, u = rotation matrices for z, y and x axis respectively
		b = 2d output vector
		"""
		a = np.array(point)-np.array([self.x, self.y, self.z])
		r = np.array([self.psi, self.theta, self.phi])
		# u, v and w are transposed, because it is easier to describe matrix
		# as a collection of basis vectors.
		u = np.array([[1,0,0], [0,cos(r[0]),-sin(r[0])], [0,sin(r[0]),cos(r[0])]]).T
		v = np.array([[cos(r[1]),0,sin(r[1])], [0, 1, 0], [-sin(r[1]),0,cos(r[1])]]).T
		w = np.array([[cos(r[2]),-sin(r[2]),0], [sin(r[2]),cos(r[2]),0], [0,0,1]]).T
		d = np.append(a.dot(w).dot(v).dot(u), [1])
		e = np.array([[1,0,0,0],
			[0,1,0,0],
			[-self.ex/self.ez, -self.ey/self.ez, 1, -1/self.ez],
			[0,0,0,1]]).transpose()
		f = d.dot(e)
		b = np.array([f[0]/f[3],f[1]/f[3]])
		return b


