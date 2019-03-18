from PIL import Image

def clamp(minval, maxval, color):
    r = int(max(minval, min(color.x, maxval)))
    g = int(max(minval, min(color.y, maxval)))
    b = int(max(minval, min(color.z, maxval)))
    return (r,g,b)

def scale(old_min, old_max, new_min, new_max, old_value):
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    new_value = (((old_value - old_min) * new_range) / old_range) + new_min
    return int(new_value)

def form_image(data, height, width):
    image = Image.new('RGB', (height, width))
    image.putdata(data)
    image.save("image.png", "PNG")
