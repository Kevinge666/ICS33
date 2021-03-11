# Hunter inherits from the Pulsator (1st) and Mobile_Simulton (2nd) classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model, random, math


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        newang = random.random() * math.pi * 2
        lis = []

        for i in model.alls.copy():
            if isinstance(i, Prey) and self.distance(list(i.get_location())) < 200:
                lis.append([i, self.distance(list(i.get_location()))])
        if lis != []:
            a = sorted(lis, key=lambda x: x[1], reverse=True)[0]
            p, q = a[0].get_location()
            u, v = self.get_location()
            newang = atan2(q - v, p - u)
        Mobile_Simulton.__init__(self, x, y, *self.get_dimension(), newang, 5)

    def update(self):
        Pulsator.update(self)
        lis = []

        for i in model.alls.copy():
            if isinstance(i, Prey) and self.distance(list(i.get_location())) < 200:
                lis.append([i, self.distance(list(i.get_location()))])
        if lis != []:
            a = sorted(lis, key=lambda x: x[1], reverse=False)[0]
            p, q = a[0].get_location()
            u, v = self.get_location()
            newang = atan2(q - v, p - u)
            self.set_angle(newang)

        Mobile_Simulton.move(self)
        Mobile_Simulton.wall_bounce(self)
