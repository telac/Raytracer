#!/usr/bin/env python

from math import sqrt


class Vec3():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def square(self):
        return self.x*self.x + self.y * self.y + self.z * self.z

    def length(self):
        return sqrt(self.square())

    def dot(self, vec):
         return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def round_tuple(self):
        return (int(self.x), int(self.y), int(self.z))

    def cross(self, vec):
        v_x = self.y * vec.z - self.z * vec.y
        v_y = self.z * vec.x - self.x * vec.z
        v_z = self.x * vec.y - self.y * vec.x
        return self.__class__(v_x, v_y, v_z)

    def distance(self, vec):
        return sqrt((self.x - vec.x) ** 2 + (self.y - vec.y) ** 2 + (self.z - vec.z) ** 2)

    def normalize(self):
        return self.__class__(
                        self.x / self.length(),
                        self.y / self.length(),
                        self.z /self.length()
                )

    def __add__(self, other):
        if type(other) == type(self):
            return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return self.__class__(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if type(other) == type(self):
            return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return self.__class__(self.x - other, self.y - other, self.z - other)

    def __truediv__(self, other):
        if type(other) == type(self):
            return self.__class__(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            return self.__class__(self.x / other, self.y / other, self.z / other)

    def __mul__ (self, other):
        if type(other) == type(self):
            return self.dot(other)
        else:
            return self.__class__(self.x * other, self.y * other, self.z * other)

    def __rmul__ (self, other):
        if type(other) == type(self):
            return self.dot(other)
        else:
            return self.__class__(self.x * other, self.y * other, self.z * other)

    def __lmul__ (self, other):
        if type(other) == type(self):
            return self.dot(other)
        else:
            return self.__class__(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)


if __name__ == "__main__":
    v1 = Vec3(0.0, 0.0, 1.0)
    print(v1 * v1)
