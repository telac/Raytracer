from sphere import Sphere
from ray import Ray
from vector import Vec3
from time import time
from timeit import default_timer as timer
from scene import Scene
from light import Light


RED = Vec3(255, 0, 0)
GREEN = Vec3(0, 255, 0)
BLUE = Vec3(0, 0, 255)
BLACK = Vec3(0,0,0)
WHITE = Vec3(255, 255, 255)

if __name__ == "__main__":

    width = 500
    height = 500
    objects = []
    lights = []

    # add objects
    s_0 = Sphere(Vec3(250, 250, 30), 100, RED)
    s_1 = Sphere(Vec3(100, 200, 10), 70, GREEN)
    s_2 = Sphere(Vec3(400, 100, 20), 50, WHITE)
    s_3 = Sphere(Vec3(500, 500, 100), 400, BLUE)
    objects.append(s_0)
    objects.append(s_1)
    objects.append(s_2)
    objects.append(s_3)


    # add lights
    l_1 = Light(Vec3(50, 50, -500), WHITE)
    lights.append(l_1)

    ray_origin = Vec3(0, 0, -500)
    ray_direction = Vec3(0, 0, 0) - ray_origin
    data = [(0, 0, 0) for x in range(width*height)]
    ray = Ray(ray_origin, ray_direction)
    SphereScene = Scene(width, height, objects, lights, ray_origin)
    SphereScene.render_scene(ray)
