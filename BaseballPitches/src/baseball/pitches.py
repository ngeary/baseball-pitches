"""
Created on Sep 5, 2018
@author: Nick Geary

This module defines the attributes and behavior of baseball pitches.
"""

from npgphysics import forces
from npgmath import euler
from scipy.constants import pi

class Pitch:
    """A customizeable baseball pitch. For predefined pitches, use a subclass
    instead.
    """

    mass = 0.14529                          # in kilograms
    drag_coefficient = 0.4                  # unitless
    radius = 0.03633                        # in meters
    area = pi * radius**2                   # cross-sectional surface area in
                                            # square-meters
    default_position = [0.0, 1.90, -0.6]    # release point of the pitch from
                                            # the pitcher's hand in meters
    default_velocity = [42.0, -0.2, 1.3]    # initial velocity of the pitch in
                                            # meters per second
    
    def __init__(self, p, v, s, l="Custom Pitch", c='gray'):
        """Initialize a baseball pitch to be thrown.
        
        Parameters
        ----------
            p : list of float
                A list with the x-, y-, and z-coordinate of the release point
                (a.k.a. the intial position of the pitch).
            v : list of float
                A list with the x-, y-, and z-components of the initial
                velocity.
            s : list of float
                A list with the x-, y-, and z-components of the initial spin.
            l : string
                The label to use when plotting this pitch.
            c : color constant
                The color constant to use when plotting this pitch. Must be
                recognized by the matplotlib library.            
        """
        self.label = l
        self.color = c
        self.position = p
        self.trail = [self.position]
        self.velocity = v
        self.spin = s
        
    def throw(self,distance,dt):
        """Calculate the trajectory of the pitch from the release point to the
        specified distance towards the batter using the Euler Method
        (https://en.wikipedia.org/wiki/Euler_method). Store the trajectory as a
        list of positions in the trail attribute of the Pitch object.
        
        Parameters
        ----------
            distance : float
                The distance (in meters) to throw the pitch.
            dt : float
                The time (in seconds) to let the ball travel before making a
                new calculation.
        """
        
        f_gravity = forces.calculate_gravity(self.mass)
        
        # while baseball hasn't crossed the plate (x = distance) or hit the
        # ground (y = 0)
        while (self.position[0] < distance and self.position[1] > 0):    
            net_force = forces.add_forces([f_gravity,
                                           forces.calculate_drag(
                                               self.velocity,
                                               self.area,
                                               self.drag_coefficient),
                                           forces.calculate_magnus(
                                               self.velocity,
                                               self.spin)])
            acceleration = [f / self.mass for f in net_force]
            self.position, self.velocity = euler.new_state(self.position,
                                                           self.velocity,
                                                           acceleration,
                                                           dt)
            self.trail.append(self.position)
            
class FourSeamFastball(Pitch):
    """This is a predefined pitch. The spin makes the pitch stay high and
    travel straight.
    """
    
    def __init__(self, color='black'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.05, 0.0, -0.03]
        super(FourSeamFastball, self).__init__(position, velocity, spin,
                                               "4-Seam Fastball", color)
        
class Slider(Pitch):
    """This is a predefined pitch. The spin makes the pitch curve down and
    sharply to the left from the perspective of a right-handed pitcher.
    """
    
    def __init__(self, color='green'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, 0.024, 0.02]
        super(Slider, self).__init__(position, velocity, spin,
                                     "Slider", color)
        
class TwoSeamFastball(Pitch):
    """This is a predefined pitch. The spin makes the pitch stay high and
    curve slightly to the right from the perspective of a right-handed pitcher.
    """
    
    def __init__(self, color='blue'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, -0.008, -0.02]
        super(TwoSeamFastball, self).__init__(position, velocity, spin,
                                              "2-Seam Fastball", color)
        
class Changeup(Pitch):
    """This is a predefined pitch. The spin makes the pitch travel almost
    completely straight, staying slightly higher and curving a tiny bit
    more to the right than a pitch with no spin, from the perspective of a
    right-handed pitcher.
    """
    
    def __init__(self, color='orange'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, -0.002, -0.01]
        super(Changeup, self).__init__(position, velocity, spin,
                                       "Changeup", color)
        
class Curveball(Pitch):
    """This is a predefined pitch. The spin makes the pitch curve sharply down
    and to the left from the perspective of a right-handed pitcher.
    """
    
    def __init__(self, color='mediumorchid'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, 0.016, 0.03]
        super(Curveball, self).__init__(position, velocity, spin,
                                        "Curveball", color)
        
class Screwball(Pitch):
    """This is a predefined pitch. The spin makes the pitch curve down and
    sharply to the right from the perspective of a right-handed pitcher.
    """
    
    def __init__(self, color='teal'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, -0.016, 0.018]
        super(Screwball, self).__init__(position, velocity, spin,
                                        "Screwball", color)
        
class Knuckleball(Pitch):
    """This is a predefined pitch. There is almost no spin so the trajectory
    is largely affected by minor fluctuations in the wind. Note that wind
    effects have not yet been added to this pitching simulator.
    """
    
    def __init__(self, color='deeppink'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, 0.0015, 0.00]
        super(Knuckleball, self).__init__(position, velocity, spin,
                                          "Knuckleball", color)
        
class Testball(Pitch):
    """This class can be edited to test pitches with arbitrary positions,
    velocity, and spin. Alternatively, customized objects from the base class
    can also be used.
    """
    
    def __init__(self, color='green'):
        position = self.default_position
        velocity = self.default_velocity
        spin = [0.00, 0.00, -0.03]
        super(Testball, self).__init__(position, velocity, spin,
                                       "Testball", color)      
        