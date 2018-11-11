from collections import namedtuple


_Vector2D = namedtuple("_Vector2D", ["x", "y"])
_Vector3D = namedtuple("_Vector3D", ["x", "y", "z"])


class Vector2D(_Vector2D):

    def __add__(self, vector):
        return Vector2D(
            self.x + vector.x,
            self.y + vector.y
        )

    def __mul__(self, vector):
        return Vector2D(
            self.x * vector.x,
            self.y * vector.y
        )

    def __truediv__(self, vector):
        return Vector2D(
            self.x / vector.x,
            self.y / vector.y
        )

    def __floordiv__(self, vector):
        return Vector2D(
            int(self.x / vector.x),
            int(self.y / vector.y)
        )

    def __str__(self):
        return "x: {}, y: {}".format(self.x, self.y)


class Vector3D(_Vector3D):

    def __add__(self, vector):
        return Vector3D(
            self.x + vector.x,
            self.y + vector.y,
            self.z + vector.z
        )

    def __mul__(self, vector):
        return Vector3D(
            self.x * vector.x,
            self.y * vector.y,
            self.z * vector.z
        )

    def __truediv__(self, vector):
        return Vector3D(
            self.x / vector.x,
            self.y / vector.y,
            self.z / vector.z
        )

    def __floordiv__(self, vector):
        return Vector3D(
            int(self.x / vector.x),
            int(self.y / vector.y),
            int(self.z / vector.z)
        )

    def __str__(self):
        return "x: {}, y: {}, z: {}".format(self.x, self.y, self.z)
