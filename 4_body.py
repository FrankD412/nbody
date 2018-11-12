import arcade

from core.structures.planets import Planet2D
from core.structures.vectors import Vector2D


class FourBodyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, scale, dt_scale):
        super().__init__(width, height, "4-Body Test Window")

        self._width = width
        self._height = height
        self._scale = scale
        self._dt_scale = dt_scale
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Set up your game here
        self.sun = Planet2D("Sun", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0),
                            695.508e6, 1.989e30, arcade.color.YELLOW)

        self.moon = Planet2D("Earth Moon", Vector2D(0.0, 149.6e9+384.4e6),
                             Vector2D(29.78e3+1.023e3, 0.0), (695.508e6)/2, 7.34767309e22,
                             arcade.color.WHITE)

        self.earth = Planet2D("Earth", Vector2D(0.0, 149.6e9),
                              Vector2D(29.78e3, 0.0),
                              695.508e6, 5.972e24, arcade.color.BLUE)
        self.mercury = Planet2D("Mercury", Vector2D(0.0, 57.91e9),
                                Vector2D(48e3, 0.0),
                                695.508e6, 3.285e23, arcade.color.RED)
        self.venus = Planet2D("Venus", Vector2D(0.0, 108.2e9),
                              Vector2D(35e3, 0.0),
                              695.508e6, 4.867e24, arcade.color.WHITE)

        self.sun.print_summary()
        self.mercury.print_summary()
        self.venus.print_summary()
        self.earth.print_summary()
        self.moon.print_summary()

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.sun.draw(self._scale, 500)
        self.earth.draw(self._scale, 500)
        self.moon.draw(self._scale, 500)
        self.venus.draw(self._scale, 500)
        self.mercury.draw(self._scale, 500)

    def update(self, dt):
        """ All the logic to move, and the game logic goes here. """
        dt_scale = self._dt_scale
        self.sun.print_summary()
        self.sun.update([self.earth, self.mercury, self.venus, self.moon], dt, dt_scale)
        self.earth.print_summary()
        self.earth.update([self.sun, self.mercury, self.venus, self.moon], dt, dt_scale)
        self.moon.print_summary()
        self.moon.update([self.sun, self.mercury, self.venus, self.earth], dt, dt_scale)
        self.mercury.print_summary()
        self.mercury.update([self.sun, self.earth, self.venus, self.moon], dt, dt_scale)
        self.venus.print_summary()
        self.venus.update([self.sun, self.mercury, self.earth, self.moon], dt, dt_scale)


def main():
    window = FourBodyWindow(1000, 1000, 0.0000000025, 100000)
    window.set_update_rate(.000005)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
