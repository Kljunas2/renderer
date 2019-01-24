import re

class Vertex:
        def __init__():
                pass

class Face:
        def __init__():
                pass


class Solid:
        def __init__():
                pass


with open(file, "r") as f:
        f.readline().lstrip()
        
rx_dict = {
    'solid': re.compile(r'solid ascii\n(?P<solid>.*)\nendsolid'),
    'facet': re.compile(r'facet (?P<facet>)\nendfacet'),
    'normal': re.compile(r'normal(?P<normal>Name|Score)\n'),
}
