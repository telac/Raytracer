from PIL import Image
import random

data = []
for y in range(255):
    for x in range(255):
        R = x
        G = x
        B = x
        if x > 128:
            R = y
            G = y
            B = y
        data.append((R, G, B))

image = Image.new('RGB', (255, 255))
image.putdata(data)

image.save("image.png", "PNG")
