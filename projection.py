#!/usr/bin/env python3

import numpy as np
import math


def mag(vector): # returns magnitude
	return(sqrt(vector.dot(vector)))

sqrt = np.sqrt
sin = math.sin
cos = math.cos
acos = np.arccos

class Rotation:
	def __init__(self, u, v, w, degrees=True):
		if degrees:
			self.u = math.radians(u)
			self.v = math.radians(v)
			self.w = math.radians(w)
		else:
			self.u = u
			self.v = v
			self.w = w

	def __call__(self):
		pass


class Camera:
	"""rot is given in degrees, ez display[2] controls field of view."""

	def __init__(self, pos, rot, display):
		self.x = pos[0]
		self.y = pos[1]
		self.z = pos[2]
		self.psi = math.radians(rot[0]%360)
		self.theta = math.radians(rot[1]%360)
		self.phi = math.radians(rot[2]%360)
		self.ex = display[0]
		self.ey = display[1]
		self.ez = display[2]
		self.r = 0

	def update(self):
		psi = self.psi
		theta = self.theta
		phi = self.phi
		# u, v and w are transposed, because it is easier to describe matrix
		# as a collection of basis vectors.
		self.r = np.array([[cos(phi),-sin(phi),0], [sin(phi),cos(phi),0], [0,0,1]]).T \
		.dot(np.array([[cos(theta),0,sin(theta)], [0, 1, 0], [-sin(theta),0,cos(theta)]]).T) \
		.dot(np.array([[1,0,0], [0,cos(psi),-sin(psi)], [0,sin(psi),cos(psi)]]).T)

	def projection(self, point):
		"""Returns input vector relative to the camera, projected onto 2d plane.
		a = input vector - camera vector
		b = 2d output vector
		"""
		a = point - np.array([self.x, self.y, self.z])
		d = a.dot(self.r)
		b = np.array([self.ez*d[0]/d[2], -self.ez*d[1]/d[2]])
		return b

	def normal(self, normal, face):
		p = np.array(normal).dot(self.r)
		q = np.array(np.array([self.x, self.y, self.z])-face).dot(self.r)
		return acos(p.dot(q)/(mag(p)*mag(q)))*2/np.pi


class Face:
	def __init__(self, ver1, ver2, ver3, normal):
		self.loop = np.array([ver1, ver2, ver3])

	def project(self, camera):
		for i in self.loop:
			camera.projection(i)
