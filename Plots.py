from Particle import Particle
import numpy as np 
from matplotlib import pyplot as plt

DataIn = np.load("h:\PHYS281 Project\Results.npy", allow_pickle = True)

"""Initially defining variables as empty lists for use later in the code."""

time = []
linmomentum = []
kineticenergy = []
PotentialEnergy = []
xdata = []
ydata = []
zdata = []

for i in range(len(DataIn[0][1])):
    xdata.append([])
    ydata.append([])

"""Loop to calculate the total linear momentum and total kinetic energy of the system as a function of time"""

for i in range(len(DataIn)):
    tempmomentum = np.array([0, 0, 0], dtype = float)
    temp = 0.
    for planet in DataIn[i][1]:
        tempmomentum += planet.Momentum()
        temp += planet.KineticEnergy()
    time.append(DataIn[i][0])
    linmomentum.append(np.linalg.norm(tempmomentum))
    kineticenergy.append(temp)

"""Loop to calculate x and y positions of all the bodies as a function of time"""

for i in range(len(DataIn)):
    for j in range(len(DataIn[0][1])):
        xdata[j].append(DataIn[i][1][j].position[0])
        ydata[j].append(DataIn[i][1][j].position[1])


"Code to plot different graphs"

plt.plot(time, kineticenergy, color = 'red', label = "Total Kinetic Energy")                               #total kinetic energy against time#
plt.xlabel("Time $t$ $\mathrm{(s)}$")
plt.ylabel("Total Kinetic Energy $E_{ktot}$ $\mathrm{(J)}$")
plt.show()

plt.plot(time, linmomentum, color = 'red', label = "Total Linear Momentum")                                #total linear momentum against time#
plt.xlabel("Time $t$ $\mathrm{(s)}$")                                                                                        
plt.ylabel("Total Linear Momentum $p_{TOT}$ $\mathrm{(kgms^{-1})}$")
plt.show()

for j in range(len(DataIn[0][1])):                                                                         #two-dimensional orbit diagram for all planets#
    plt.plot(xdata[j], ydata[j])
plt.xlabel("$x$ position of planet $\mathrm{(m)}$")
plt.ylabel("$y$ position of planet $\mathrm{(m)}$")
plt.legend
plt.show()


