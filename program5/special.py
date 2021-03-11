# The ball will start at a random angle and random speed.
# I also change the color of the ball
# I think this is really funny
from prey import Prey


class Special(Prey):
    radius = 10

    def __init__(self, x, y, angle, speed):
        Prey.__init__(self, x, y, 10, 10, angle, speed)

    def update(self):
        Prey.move(self)
        Prey.wall_bounce(self)

    def display(self, the_canvas):
        the_canvas.create_oval(self._x - Special.radius, self._y - Special.radius,
                               self._x + Special.radius, self._y + Special.radius,
                               fill='red')
