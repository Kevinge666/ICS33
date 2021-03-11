import controller
import model   # Pass a reference to this module when calling each update in update_all
import random,math
#Use the reference to this module to pass it to update methods

from ball      import Ball,Special
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter



# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
alls       = set()
select = Ball
def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,alls
    running     = False
    cycle_count = 0
    alls = set()

#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 


#tep just one update in the simulation
def step ():
    global running,cycle_count
    cycle_count+=1
    running = False 
    for b in alls:
        b.update(model)

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global select
    if kind!='Remove':
        select = eval(kind)
    else:
        select = "Remove"
    


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global alls,select
    if select =='Remove':
        xy=[x,y]
        for i in alls.copy():
            if i.contains(xy):
                remove(i)
    if select == Black_Hole:
        alls.add(select(x,y))
    if select == Hunter:
        alls.add(select(x,y))
    if select == Pulsator:
        alls.add(select(x,y))
    if select == Ball or select == Special:
        alls.add(select(x,y,random_angle()))
    if select == Floater:
        alls.add(Floater(x,y,random_angle(),random.uniform(3,7)))


#add simulton s to the simulation
def add(s):
    global alls
    all.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global alls
    alls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global alls
    output=set()
    for i in alls:
        if p(i):
            output.add(i)
    return output


#call update for every simulton (passing each model) in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in alls.copy():
            b.update()

#To animate: first delete every simulton from the canvas; then call display on
#  each simulton being simulated to add it back to the canvas, possibly in a
#  new location; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in alls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(alls))+" simutons")