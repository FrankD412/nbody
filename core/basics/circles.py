import arcade

from core.abstracts.shape import Shape2D


class Circle(Shape2D):
    def __init__(self, x, y, radius, color):
        super(Circle, self).__init__(x, y, radius, radius, color)

    def draw(self, scale=1, offset=0):
        args = [self._pv.x, self._pv.y, self._height, self._width]
        args = list(map(lambda x: x * scale, args))
        print(args)
        args[0] += offset
        args[1] += offset
        args += [self._color, self._angle]
        arcade.draw_ellipse_filled(*args)
