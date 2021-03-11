# The Hunter class is derived from Pulsator (1st) and the Mobile_Simulton (2nd).
#   It updates/displays like its Pulsator base, but also moves (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model,math, random


class Hunter(Pulsator, Mobile_Simulton):
    see_distance = 200

    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        self.angle = random.random() * math.pi * 2
        Mobile_Simulton.__init__(self, x, y, *self.get_dimension(), self.angle, 5)

    def update(self):
        Pulsator.update(self)
        lst = []
        new_model = model.ball.copy()
        for i in new_model:
            if isinstance(i, Prey) and self.distance(list(i.get_location())) <= Hunter.see_distance:
                lst.append([i, self.distance(list(i.get_location()))])

        if lst != []:
            a = sorted(lst, key=lambda x: x[1], reverse=False)
            nod = a[0][0]
            p, q = nod.get_location()
            u, v = self.get_location()
            self.set_angle(atan2(q - v, p - u))

        Mobile_Simulton.move(self)
        Mobile_Simulton.wall_bounce(self)
