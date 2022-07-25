# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:58:50 2021

@author: ewanh
"""
import numpy as np
import statistics
from Particle import ChargedParticle
from Particle import bunch
from Particle import Particle

#print(bunch)

xpositions = []
ypositions = []
xvelocity = []
yvelocity = []
kineticenergies = []
xmomenta = []
ymomenta = []

#for i in bunch:
    #xpositions.append(i[1])
    
#print(xpositions)
    
#print(bunch[0])

#print(bunch[0].position[0])
#print(bunch[1].position[0])

for i in bunch:
    tempx = i.position[0]
    xpositions.append(tempx)
    
for i in bunch:
    tempy = i.position[1]
    ypositions.append(tempy)
    
    
#print(xpositions)

meanx = statistics.mean(xpositions)
varx = statistics.variance(xpositions)
#print(meanx)
#print(varx)

def mean(list):
    return statistics.mean(list)

meanx2 = mean(xpositions)
#print(meanx2)

def variance(list):
    return statistics.variance(list)
    
    
apple = Particle.kineticenergy(bunch[0])
#print(apple)
    
banana = Particle.momentum(bunch[0])
#print(banana)


def InterquartileRange(list):
    return np.percentile(list, 75) - np.percentile(list, 25)

pear = InterquartileRange(xpositions)

#print(pear)



for i in bunch:
    tempke = Particle.kineticenergy(i)
    kineticenergies.append(tempke)
    
mom1 = Particle.momentum(bunch[0])
mom2 = Particle.momentum(bunch[1])

print(mom1)
print(mom2)
    
#print(kineticenergies)

for i in bunch:
    tempxp = Particle.momentum(i)[0]
    xmomenta.append(tempxp)
    
for i in bunch:
    tempyp = Particle.momentum(i)[1]
    ymomenta.append(tempyp)
    
print(xmomenta)
print(ymomenta)



class Statistics:
    
    def mean(self):
        return statistics.mean(self)
    