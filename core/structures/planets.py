from core.basics.mass import PointMass2D
from core.structures.vectors import Vector2D


class Planet2D(PointMass2D):
    def __init__(self, name, pos, vi, radius, mass, color, moons=[]):
        super(Planet2D, self).__init__(name, pos, vi, radius, mass, color)
        self._moons = []
        for moon in moons:
            moon._pv = moon._pv + self._pv
            moon._velocity = moon._velocity + self._velocity
            self._moons.append(moon)

    def update(self, neighbors, dt, dt_scale=1.0):
        for moon in self._moons:
            print(moon._pv)
            moon.print_summary()
            moon.update(neighbors + [self], dt, dt_scale)

        neighbors += self._moons
        super(Planet2D, self).update(neighbors, dt, dt_scale)

    def on_draw(self):
        for moon in self._moons:
            moon.on_draw()

        super(Planet2D, self).on_draw()
