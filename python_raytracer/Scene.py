#!/usr/bin/env python

import math
from vector import Vec3
from ray import Ray
from helpers import form_image

RED = Vec3(255, 0, 0)
GREEN = Vec3(0, 255, 0)
BLUE = Vec3(0, 0, 255)
BLACK = Vec3(0,0,0)
WHITE = Vec3(255, 255, 255)
MAX_DEPTH = 2
BIAS = 0.01


class Scene():

    def __init__(self, width, height, objects):
        self.width = width
        self.height = height
        self.objects = objects
        self.data = [(0, 0, 0) for x in range(self.width*self.height)]

    def render_scene(self, ray):
        for y in range(self.height):
            for x in range(self.width):
                ray.direction.x = x
                ray.direction.y = y
                color = self.trace_ray(ray)
                self.data[x + y * self.width] = color.round_tuple()
                if x % 400 == 0 and y % 100 == 0:
                    form_image(self.data, self.height, self.width)
        form_image(self.data, self.height, self.width)

    def trace_ray(self, ray, depth=0):
        for obj in self.objects:
            intersect = obj.intersect(ray)
            if intersect:
                V = -1 * Vec3(ray.direction.x, ray.direction.y, ray.direction.z).normalize()
                point = ray.at(intersect)
                N = obj.get_normal(point)
                ratio = max(0, N*V)
                color = ratio * obj.color
                moved_point = point + N * BIAS
                reflection = Ray(moved_point, ray.reflect(N))
                if depth < MAX_DEPTH:
                    color += 0.7 * self.trace_ray(reflection, depth + 1)
                return color
        return BLACK
