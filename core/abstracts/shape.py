from abc import ABC, abstractmethod

from core.structures.vectors import Vector2D


class Shape2D(ABC):
    def __init__(self, x, y, height, width, color):
        self._pv = Vector2D(x, y)
        self._angle = 0

        self._height = height
        self._width = width
        self._color = color

    def update(self, dv, da=0):
        self._pv += dv
        self._angle += da

    @abstractmethod
    def draw(self, scale):
        pass

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
