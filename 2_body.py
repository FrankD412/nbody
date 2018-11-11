import arcade

from core.basics.mass import PointMass
from core.structures.vectors import Vector2D


class TwobodyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, scale):
        super().__init__(width, height, "2-Body Test Window")

        self._width = width
        self._height = height
        self._scale = scale
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Set up your game here
        self.sun = PointMass("Sun", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0),
                             695.508e6, 1.989e30, arcade.color.YELLOW)
        self.earth = PointMass("Earth", Vector2D(0.0, 149.6e9),
                               Vector2D(29.78e3, 0.0),
                               695.508e6, 5.972e24, arcade.color.YELLOW)

        self.sun.print_summary()
        self.earth.print_summary()

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.sun.draw(self._scale, 500)
        self.earth.draw(self._scale, 500)

    def update(self, dt):
        """ All the logic to move, and the game logic goes here. """
        self.sun.print_summary()
        self.sun.update([self.earth], dt)
        self.earth.print_summary()
        self.earth.update([self.sun], dt)


def main():
    window = TwobodyWindow(1000, 1000, 0.0000000025)
    window.set_update_rate(.000005)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
