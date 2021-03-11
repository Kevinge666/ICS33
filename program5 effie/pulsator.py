# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions
import model
from blackhole import Black_Hole


class Pulsator(Black_Hole):
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.b = model.cycle_count
        self.c = []

    def update(self):
        if model.cycle_count - self.b <= 30:
            c = Black_Hole.update(self).copy()
            if self.c != c:
                self.radius += len(c) - len(self.c)
                p, q = self.get_dimension()
                self.set_dimension(p + 1, q + 1)
                self.c = c.copy()
                self.b = model.cycle_count
        else:
            self.radius -= 1
            p, q = self.get_dimension()
            self.set_dimension(p - 1, q - 1)
            self.b = model.cycle_count
            if self.radius == 0:
                model.remove(self)
