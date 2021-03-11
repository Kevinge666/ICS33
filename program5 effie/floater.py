# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    @staticmethod
    def random_index(rate):
        """随机变量的概率函数"""
        #
        # 参数rate为list<int>
        # 返回概率事件的下标索引
        start = 0
        index = 0
        randnum = random.randint(1, sum(rate))

        for index, scope in enumerate(rate):
            start += scope
            if randnum <= start:
                break
        return index

    def __init__(self, x, y, angle, speed):
        self._image = PhotoImage(file='ufo.gif')
        w = self._image.width()
        h = self._image.height()
        Prey.__init__(self, x, y, w, h, angle, speed)

    def display(self, the_canvas):
        the_canvas.create_image(*self.get_location(), image=self._image)

    def update(self):
        random1 = Floater.random_index([30, 70])
        if random1 == 1:
            Prey.move(self)
            Prey.wall_bounce(self)
        else:
            g = self.get_angle()
            s = self.get_speed()
            if s + 0.5 > 7:
                a = random.uniform(-0.5, 7 - s)
            elif s - 0.5 < 3:
                a = random.uniform(3 - s, 0.5)
            else:
                a = random.uniform(-0.5, 0.5)

            b = random.uniform(-0.5, 0.5)
            self.set_angle(g + b)
            self.set_speed(s + a)
            Prey.move(self)
            Prey.wall_bounce(self)
