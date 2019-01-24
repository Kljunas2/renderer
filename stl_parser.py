#!/usr/bin/env python3

import re


class Vertex:
	def __init__(self, coordinates):
		def float_(significand, exponent):
			return float(significand)*10**int(exponent)

		matches = rx_dict["float"].finditer(coordinates)
		self.coordinates = [float_(i.group("significand"), i.group("exponent")) for i in matches]

	def __repr__(self):
		return "x: {}, y: {}, z: {}".format(str(self.coordinates[0]), str(self.coordinates[1]), str(self.coordinates[2]))

	def __call__(self):
		return self.coordinates


class Facet:
	def __init__(self, normal, loop):
		self.normal = Vertex(rx_dict["vertex"].search(normal).group("vertex"))
		matches = rx_dict["vertex"].finditer(loop)
		self.loop = [Vertex(i.group("vertex")) for i in matches]

	def __str__(self):
		return "normal: {}, loop: {}".format(self.normal, self.loop)

	def __repr__(self):
		return "normal: {} loop: {}".format(self.normal, self.loop)


class Solid:
	def __init__(self, solid, *name):
		if not name:
			self.name = None
		matches = rx_dict["facet"].finditer(solid)
		self.facets = [Facet(i.group("normal"), i.group("loop")) for i in matches]

	def __str__(self):
		return "Solid name: {}, number of faces: {}".format(self.name, len(self.facets))

	def __iter__(self):
		for i in self.facets:
			yield i


rx_dict = { # strings for parsing stl files
	"facet": re.compile(r"\s*facet (?P<normal>normal .*)\n\s*outer loop"
		+ r"\n(?P<loop>(?:\s*vertex.*\n){3})\s*endloop\n\s*endfacet"),
	"vertex": re.compile(r"(?:(?:vertex)|(?:normal))\s*"
		+ r"(?P<vertex>(?:-?\d.\d*e[-+]\d*\s?\n?){3})"),
	"float": re.compile(r"(?P<significand>-?\d.\d*)e(?P<exponent>[-+]\d*)")
}
if __name__ == "__main__":
	with open("cube.stl", "r") as f:
		for i in Solid(f.read()):
			print(i)
