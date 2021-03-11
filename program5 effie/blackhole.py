# Black_Hole inherits from only Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    def __init__(self, x, y):
        self.a = []
        self.radius = 10
        Simulton.__init__(self, x, y, 20, 20)

    def display(self, canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius,
                           self._x + self.radius, self._y + self.radius,
                           fill='black')

    def contains(self, xy):
        if type(xy) == list:
            return Simulton.contains(self, xy)
        else:
            a, b = xy.get_location()
            ab = [a, b]
            c = self.distance(ab)
            return c < self.radius

    def update(self):
        self.a += model.find(lambda x: isinstance(x, Prey) and self.contains(x))
        for i in self.a:
            if i in model.alls:
                model.remove(i)
        return self.a
