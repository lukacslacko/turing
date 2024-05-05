from modules import *

scene = (cylinder(h=10, d=10) + sphere(d=10).translate([20,0,0])) - cube(r=5)
print(scene)
