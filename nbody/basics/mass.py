from math import sqrt

from core.basics.circles import Circle
from core.structures.vectors import Vector2D

# 6.67408 × 10-11 m3 kg-1 s-2
GRAV_CONSTANT = 6.67408e-11


class PointMass2D(Circle):
    """A class representing point masses."""

    def __init__(self, name, pos, vi, radius, mass, color):
        """Initialize a new PointMass object."""
        super(PointMass2D, self).__init__(pos.x, pos.y, radius, color)
        self.name = name
        self._velocity = vi
        self.mass = mass
        self.timestep = 0.0

    def print_summary(self, dt=0):
        _info = \
            "------------------------------------\n" \
            "| Name:     {}\n" \
            "| Position: {}\n" \
            "| Timestep: {}\n" \
            "| Delta t:  {}\n" \
            "| Velocity: {}\n" \
            "| Mass:     {}\n" \
            "------------------------------------" \
            .format(self.name, self._pv, self.timestep, dt, self._velocity,
                    self.mass)
        print(_info)

    def update(self, neighbors, dt, dt_scale):
        self.timestep += (dt * dt_scale)
        dv = Vector2D(0.0, 0.0)
        dt = Vector2D(dt * dt_scale, dt * dt_scale)
        x = self._pv.x
        y = self._pv.y
        for n in neighbors:
            # Compute the full force of gravity.
            fg = GRAV_CONSTANT * n.mass
            dist = Vector2D((n._pv.x - x), (n._pv.y - y))
            d = sqrt(dist.x**2 + dist.y**2)
            d = Vector2D(d, d)
            fg = Vector2D(fg, fg) / d / d

            # So, as it turns out, the triangle formed by the component vectors
            # of gravitational forces of objects in motion forms similar
            # triangles to the components of the triangle formed by the
            # components of the distance triangle. Because they're similar,
            # we can compute the component vectors for the gravitation force
            # by scaling related to the same proportion of distance.
            # Fgx / (x1 - x2) = Fg / d
            fg = fg * (dist / d)
            dv += fg

        self._velocity += (dv * dt)
        self._pv += (self._velocity * dt) + Vector2D(.5, .5) * dt * dt * dv
