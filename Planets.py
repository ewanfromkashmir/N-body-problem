import numpy as np
from Particle import Particle
import copy

class Planets:

    """This class contains the data for the planets used in the simulation. Adding data to this class in the form of planets will update the simulation in the N-body program."""               

    #Sun initial conditions#
    Sun = Particle(np.array([-5.406880285838878E+08,1.119169453067436E+09,2.684806583454716E+06]), np.array([-1.455239383843301E+01,-3.042601933747618E+00,4.010136917074372E-01]), np.array([0,0,0]),'Sun', 1988500E+24)

    #Jupiter initial conditions#
    Jupiter = Particle([5.370006297319697E+10,-7.802281110962191E+11,2.034485476916492E+09], [1.287566479951585E+04,1.522201123032263E+03,-2.942442104413432E+02], np.array([0,0,0]), 'Jupiter', 1898.13E+24)

    #Saturn intial conditions#
    Saturn = Particle([5.514721401013178E+11,-1.395161142506884E+12,2.305294009631515E+09], [8.449070966068003E+03,3.521535558849704E+03,-3.972022987711142E+02], np.array([0,0,0]), "Saturn", 5.6834E+26)

    #Uranus initial conditions#
    Uranus = Particle([2.434241146819538E+12, 1.693385205917463E+12, -2.524662573134387E+10], [-3.939028567205058E+03, 5.272974258814238E+03, 7.040279437689700E+01], np.array([0,0,0]), "Uranus", 86.813E+24)

    #Neptune initial conditions#
    Neptune = Particle([4.371955206855778E+12, -9.615593394314837E+11, -8.095463131101966E+10], [1.130728600980438E+03, 5.340709944682925E+03, -1.354747576888777E+02], np.array([0, 0, 0]), "Neptune", 102.413E+24)

    #Planets list#
    SolarSystem = [Sun, Jupiter, Saturn, Uranus, Neptune]


