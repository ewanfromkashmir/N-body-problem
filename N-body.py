import numpy as np
from Particle import Particle
import math
import copy
from Planets import Planets

delta = 80000                                                               #input timestep#                         
time = 0                                                                     
Data = []    
PotentialEnergy = 0.                        

planets = Planets.SolarSystem                                               

"""Double loop to calculate the acceleration of each body by considering and summing all the components of acceleration acting on each body"""

for i in range(800000):                                                     #input number of iterations of loop#

    for planet1 in planets:  
        planet1.acceleration = np.array([0, 0, 0], dtype = float)
        for planet2 in planets:
            if planet1 == planet2: continue
            tempacc = np.array([0, 0, 0], dtype = float)
            r = np.subtract(planet1.position, planet2.position)
            tempacc += (-1.0*Particle.G*planet2.mass*r)/((np.linalg.norm(r))**3)
            planet1.acceleration += tempacc

    for planet1 in planets:
        planet1.update(delta)
    time += delta
    if i % 100 == 0:
        item = [time, copy.deepcopy(planets)]
        Data.append(item)


np.save("h:\PHYS281 Project\Results", Data, allow_pickle = True) 



