#!/usr/bin/env python

import math


class Ray():
    def __init__(self, orig, dir):
        self.origin = orig
        self.direction = dir

    def at(self, distance):
        return self.origin + self.direction.normalize() * distance
