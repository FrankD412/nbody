import arcade


from renderables.basics.circle import Circle


class BounceWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, start_x, start_y, radius):
        super().__init__(width, height, "Bouncing Ball")

        self._width = width
        self._height = height
        self._radius = radius
        self._x = start_x
        self._y = start_y
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        # Set up your game here
        self._ball = Circle(self._x, self._y, 1, 3.3,
                            self._radius, arcade.color.BLACK)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self._ball.draw()

    def update(self, dt):
        """ All the logic to move, and the game logic goes here. """
        x = self._ball.x
        y = self._ball.y

        if x > self._width or x < 0:
            self._ball.x_delta = -1 * self._ball.x_delta

        if y > self._height or y < 0:
            self._ball.y_delta = -1 * self._ball.y_delta

        self._ball.update()


def main():
    window = BounceWindow(640, 220, 100, 100, 16)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
