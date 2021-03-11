# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions
import model
from blackhole import Black_Hole


class Pulsator(Black_Hole):

    def __init__(self, x, y):
        self.a = model.cycle_count
        Black_Hole.__init__(self, x, y)
        self.lst = []

    def update(self):
        if model.cycle_count - self.a <= 30:
            if self.lst != Black_Hole.update(self):
                self.radius += 0.5 * (len(Black_Hole.update(self)) - len(self.lst))
                self.lst = Black_Hole.update(self).copy()
                self.lst = Black_Hole.update(self).copy()
                self.a = model.cycle_count
        else:
            self.radius -= 0.5
            self.a = model.cycle_count
            if self.radius == 0:
                model.remove(self)
