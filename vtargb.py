def vtargb(vec):
    """Pretvori NumPy vektorje v šestnajstiške aRGB oblike 0xffFFFFFF"""
    return hex(int("".join(["0x", vec.a.lower(), vec.r, vec.g, vec.b]), 16))
