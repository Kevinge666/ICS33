# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):

    def __init__(self, x, y, angle, speed):
        self.image = PhotoImage(file='ufo.gif')
        wide = self.image.width()
        high = self.image.height()
        Prey.__init__(self, x, y, wide, high, angle, speed)

    def update(self):
        a = random()
        if a <= 0.3:
            num = a - 0.5
            max_speed = max(3, self.get_speed() + num)
            new_speed = min(7, max_speed)
            self.set_velocity(new_speed, self.get_angle() + num)
        self.move()

    def display(self, the_canvas):
        the_canvas.create_image(*self.get_location(), image=self.image)
