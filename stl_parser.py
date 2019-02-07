import re


def avg_(loop):
	new = []
	for i in range(3):
		new.append(sum([x.coordinates[i] for x in loop])/3)
	return new


class Vertex:
	def __init__(self, coordinates):
		def float_(significand, exponent):
			return float(significand)*10**(int(exponent)-1)

		matches = rx_dict["float"].finditer(coordinates)
		self.coordinates = [float_(i.group("significand"), i.group("exponent")) for i in matches]

	def __call__(self):
		return self.coordinates

	def __iter__(self):
		for i in self.coordinates:
			yield i


class Facet:
	def __init__(self, normal, loop):
		self.normal = Vertex(rx_dict["vertex"].search(normal).group("vertex"))
		matches = rx_dict["vertex"].finditer(loop)
		self.loop = [Vertex(i.group("vertex")) for i in matches]
		#[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
		self.center = avg_(self.loop)


	def __call__(self):
		list_ = [i() for i in self.loop]
		list_.append(list(self.normal()))
		list_.append(self.center)
		return list_

	def __iter__(self):
		for i in self.loop.append(self.normal):
			yield list(i)


class Solid:
	def __init__(self, solid, name=False):
		self.name = name
		matches = rx_dict["facet"].finditer(solid)
		self.facets = [Facet(i.group("normal"), i.group("loop")) for i in matches]

	def __str__(self):
		name = self.name if self.name else hash(self)
		return "Solid name: {}, number of faces: {}".format(name, len(self.facets))

	def __iter__(self):
		for i in self.facets:
			yield list(i)

	def __call__(self):
		return [i() for i in self.facets]
		#return [list(i) for i in self.facets]


rx_dict = { # strings for parsing stl files
	"solid": re.compile(r"solid ascii (?P<name>.*)\n"
		+ r"(\s*facet.*\n(\s*vertex.*\n)*\s*endfacet\n)*"),
	"facet": re.compile(r"\s*facet (?P<normal>normal .*)\n\s*outer loop"
		+ r"\n(?P<loop>(?:\s*vertex.*\n){3})\s*endloop\n\s*endfacet"),
	"vertex": re.compile(r"(?:(?:vertex)|(?:normal))\s*"
		+ r"(?P<vertex>(?:-?\d.\d*e[-+]\d*\s?\n?){3})"),
	"float": re.compile(r"(?P<significand>-?\d.\d*)e(?P<exponent>[-+]\d*)")
}


def parse(str):
	return Solid(str)()
	
if __name__ == "__main__":
	with open("Nova mapa/cube.stl", "r") as f:
		print(Solid(f.read())())
		for i in Solid(f.read()):
			print(i)
