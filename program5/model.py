import controller
import model  # Use in update_all to pass update a reference to this module
import random, math
# Use the reference to this module to pass it to update methods

from ball import Ball
from floater import Floater
from blackhole import Black_Hole
from pulsator import Pulsator
from hunter import Hunter
from special import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
ball = set()
obj = Ball


# return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(), controller.the_canvas.winfo_height())


# reset all module variables to represent an empty/stopped simulation
def reset():
    global running, cycle_count, ball
    running = False
    cycle_count = 0
    ball = set()


# start running the simulation
def start():
    global running
    running = True


# stop running the simulation (freezing it)
def stop():
    global running
    running = False


# tep just one update in the simulation
def step():
    global running, cycle_count
    cycle_count += 1
    running = False
    for a in ball:
        a.update()


# remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global obj
    if kind == 'Remove':
        obj = "Remove"
    else:
        obj = eval(kind)


# add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def random_speed():
    # Magnitude is 5-10
    return random.randint(5, 10)


def random_angle():
    # between 0 and 2pi
    return random.random() * math.pi * 2


def mouse_click(x, y):
    global ball
    if obj == 'Remove':
        a = ball.copy()
        qe = [x,y]
        for i in a:
            if i.contains(qe):
                ball.remove(i)
    else:
        if obj == Ball:
            ball.add(Ball(x, y, random_angle()))
        elif obj == Black_Hole:
            ball.add(Black_Hole(x, y))
        elif obj == Pulsator:
            ball.add(Pulsator(x, y))
        elif obj == Floater:
            ball.add(Floater(x, y, random_angle(), random_speed()))
        elif obj == Hunter:
            ball.add(Hunter(x, y))
        elif obj == Special:
            ball.add(Special(x,y,random_angle(),random_speed()))


# add simulton s to the simulation
def add(s):
    global ball
    ball.add(s)


# remove simulton s from the simulation    
def remove(s):
    global ball
    ball.remove(s)


# find/return a set of simulations that each satisfy predicate p
def find(p):
    new_ball = set()
    for i in ball:
        if p(i) is True:
            new_ball.add(i)
    return new_ball


# call update for every simulton in this simulation (passing model to each)
# this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        a = ball.copy()
        for b in a:
            b.update()


# For animation: (1) delete every simulton on the canvas; (2) call display on
#  each simulton being simulated, adding it back to the canvas, possibly in a
#  new location; (3) update the progress label defined in the controller
# this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)

    for b in ball:
        b.display(controller.the_canvas)

    controller.the_progress.config(text=str(cycle_count) + " cycles/" + str(len(ball)) + " simutons")
