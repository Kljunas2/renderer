import image

height, width = 1920, 1080

img = image.newimg(height, width)
pixels = []
def rect(x1, y1, x2, y2):
        for i in range(height):
                for j in range(width):
                        if i >= y1 and i<= y2 and j >= x1 and j <= x2:
                                pixels.append((0,0,0,255))
                        else:
                                pixels.append((255,255,255,255))
                print(i)

rect(500, 400, 600, 1000)
print(pixels)
img.putdata(pixels)
img.show()
