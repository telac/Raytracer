#!/usr/bin/env python#!/usr/bin/env python

from math import sqrt

class Sphere():

    def __init__(self, pos, r, color):
        self.position = pos
        self.radius = r
        self.radius2 = r * r
        self.color = color

    def get_normal(self, point):
        return (point - self.position).normalize()

    def intersect(self, ray):
        rd = ray.direction.normalize()
        L = ray.origin - self.position
        a =  rd * rd
        b = 2 * rd * L
        c = L * L - self.radius2
        disc = b * b - 4 * a * c
        if disc >= 0:
            root1 = (-b - sqrt(disc)) / 2
            root2 = (-b + sqrt(disc)) / 2
            q = root2 if b > 0 else root1
            dist = q / a
            dist1 = c / q
            dist, dist1 = min(dist, dist1), max(dist, dist1)
            if dist1 >= 0:
                return dist1 if dist < 0 else dist
