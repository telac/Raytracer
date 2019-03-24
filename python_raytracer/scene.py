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
BIAS = 0.000000001


class Scene():

    def __init__(self, width, height, objects, lights, camera):
        self.width = width
        self.height = height
        self.objects = objects
        self.lights = lights
        self.camera = camera
        self.data = [(0, 0, 0) for x in range(self.width*self.height)]

    def render_scene(self, ray):
        for y in range(self.height):
            for x in range(self.width):
                ray.direction.x = x
                ray.direction.y = y
                color = self.trace_ray(ray, float('inf'))
                self.data[x + y * self.width] = color.round_tuple()
                if x % 400 == 0 and y % 100 == 0:
                    form_image(self.data, self.height, self.width)
        form_image(self.data, self.height, self.width)

    def trace_ray(self, ray, nearest_hit, depth=0):
        nearest_obj, nearest_point = None, None
        for obj in self.objects:
            intersect = obj.intersect(ray)
            if intersect:
                point = ray.at(intersect)
                distance = point.distance(self.camera)
                if distance < nearest_hit:
                    nearest_hit = distance
                    nearest_obj = obj
                    nearest_point = point

        if nearest_obj:
            N = nearest_obj.get_normal(nearest_point)
            V = -1 * Vec3(ray.direction.x, ray.direction.y, ray.direction.z).normalize()
            color = nearest_obj.color
            moved_point = nearest_point + N * BIAS
            # reflection
            reflection = Ray(moved_point, ray.reflect(N))
            if depth < MAX_DEPTH:
                color += 0.7 * self.trace_ray(reflection, float('inf'), depth + 1)

            for light in self.lights:
                to_light = light.position - moved_point
                length = to_light * to_light
                light_ray = Ray(moved_point, to_light)
                light_intersect = None
                for obj in self.objects:
                    light_intersect = obj.intersect(light_ray)
                    if light_intersect:
                        break

                if not light_intersect:
                    intensity = N * to_light.normalize()
                    if intensity > 0:
                        color *= intensity
                else:
                    color *= 0.05

            return color

        return BLACK

        # return BLACK
