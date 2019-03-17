from sphere import Sphere
from ray import Ray
from vector import Vec3
from PIL import Image

RED = Vec3(255, 0, 0)
GREEN = Vec3(0, 255, 0)
BLUE = Vec3(0, 0, 255)
WHITE = Vec3(0,0,0)
BLACK = Vec3(255, 255, 255)

def form_image(data, height, width):
    image = Image.new('RGB', (height, width))
    image.putdata(data)
    image.save("image.png", "PNG")

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

def reflect(dir, normal):
    return dir - 2 * (dir.normalize() * normal) * normal

def trace_ray(ray, depth):
    for obj in objects:
        intersect = obj.intersect(ray)
        if intersect:
            V = -1 * Vec3(ray.direction.x, ray.direction.y, ray.direction.z).normalize()
            point = ray.at(intersect)
            N = obj.get_normal(point)
            ratio = max(0, N*V)
            color = ratio * obj.color
            reflection = Ray(point + 0.001, reflect(ray.direction, N))
            if depth < 3:
                rc = trace_ray(reflection, depth + 1)
                color += rc
                color = 0.7 * color
                return color
            return color

    # black
    return Vec3(0, 0, 0)

if __name__ == "__main__":

    width = 500
    height = 500
    sphere_origin = Vec3(250, 250, 0)
    objects = []
    s_0 = Sphere(sphere_origin, 100, RED)
    s_1 = Sphere(Vec3(100, 100, 0), 70, GREEN)
    s_2 = Sphere(Vec3(400, 100, 0), 50, BLUE)
    s_3 = Sphere(Vec3(250, 250, 100), 400, BLUE)
    objects.append(s_0)
    objects.append(s_1)
    objects.append(s_2)
    objects.append(s_3)
    ray_origin = Vec3(0, 0, -500)
    ray_direction = Vec3(0, 0, 0) - ray_origin
    data = [(0, 0, 0) for x in range(width*height)]
    ray = Ray(ray_origin, ray_direction)

    for y in range(height):
        for x in range(width):
            ray.direction.x = x
            ray.direction.y = y
            color = trace_ray(ray, 0)
            data[x + y * width] = color.round_tuple()


    form_image(data, height, width)
