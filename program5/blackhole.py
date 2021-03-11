# The Black_Hole class is derived from Simulton. It updates by finding/removing
#   any class derived from Prey whose center is contained within its radius
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
        self.new = []
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
            x, y = xy.get_location()
            return self.distance([x, y]) < self.radius

    def update(self):
        self.new += model.find(lambda x: isinstance(x, Prey) and self.contains(x))
        for i in self.new:
            if i in model.ball:
                model.remove(i)
        return self.new
