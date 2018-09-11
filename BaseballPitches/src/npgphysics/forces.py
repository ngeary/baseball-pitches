"""
Created on Sep 5, 2018
@author: Nick Geary

This module is used to calculate the forces acting on an object.
"""

from numpy import sqrt, cross, dot
from scipy.constants import g       # acceleration due to gravity

air_density = 1.2

def calculate_gravity(mass):
    """Calculate the force of gravity on an object.
    
    Parameters
    ----------
        mass : float
            The mass in kilograms of the object.
            
    Returns
    -------
        list of float
            A 3-D force vector in units of Newtons.
            
    Examples
    --------
        >>> m = 81.6
        >>> calculate_gravity(m)
        [0, -800.2226399999998, 0]
    """
    return [0, -1 * g * mass, 0]

def calculate_drag(velocity,area,drag_coefficient):
    """Calculate the force of air resistance on an object.
    
    Parameters
    ----------
        velocity : list of float
            A vector with 1 to N dimensions that describes the velocity of an
            object in units of meters per second.
        area : float
            The cross-sectional surface area of the object in square meters.
        drag_coefficient: float
            The drag coefficient of the object. This quantity is unitless.
            
    Returns
    -------
        list of float
            A 3-D force vector in units of Newtons.
            
    Examples
    --------
        >>> v = [1.4, -2.9, 0.6]
        >>> a = 0.4
        >>> d = 1.2
        >>> calculate_drag(v, a, d)
        [-1.32074929,  2.73583781, -0.56603541]
    """
    
    magnitude = sqrt(dot(velocity, velocity))
    unit_vector = velocity / magnitude
    force = ((-0.5 * drag_coefficient * area * air_density * magnitude**2)
             * unit_vector)
    return force.tolist()

def calculate_magnus(velocity,spin):
    """Calculate the Magnus force exerted on an object due to spin.
    
    Parameters
    ----------
        velocity : list of float
            A vector with 1 to N dimensions that describes the velocity of an
            object in units of meters per second.
        spin : list of float
            A vector with 1 to N dimensions that describes the spin of an
            object converted to units of kilograms per second.
            
    Returns
    -------
        list of float
            A 3-D force vector in units of Newtons.
            
    Examples
    --------
        >>> v = [42.0, -0.2, 1.3]
        >>> s = [0.01, 0.02, 0.03]
        >>> calculate_magnus(v, s)
        [-0.032, -1.247, 0.842]
    """
    return cross(velocity,spin).tolist()

def add_forces(forces):
    """Return the sum of a list of forces.
    
    Parameters
    ----------
        forces : 2-D list of float
            A list of force vectors, each of which contain 1 to N dimensions.
            All forces should have the same number of dimensions. The return
            value will only include the dimensions of the force with the fewest
            dimensions.
            
    Returns
    -------
        list of float
            A force vector that represents the sum of all input force vectors.
            
    Examples
    --------
        >>> f_grav = [0, -800.2226399999998, 0]
        >>> f_drag = [-1.32074929,  2.73583781, -0.56603541]
        >>> f_magnus = [-0.032, -1.247, 0.842]
        >>> forces = [f_grav, f_drag, f_magnus]
        >>> add_forces(forces)
        [-1.35274929, -798.7338021899998, 0.27596458999999995]            
    """
    net_force = [0,0,0]
    for f in forces:
        net_force = [a + b for a, b in zip(net_force, f)]
    return net_force

def calculate_net_force(mass,velocity,area,drag_coefficient,spin):
    """Calculate gravity, air resistance, and the Magnus effect for an object.
    This function should not be called repeatedly because it will recalculate
    the force of gravity, which usually stays constant.
    
    Parameters
    ----------
        mass : float
            The mass of the object in kilograms.
        velocity : list of float
            A vector with 1 to N dimensions that describes the velocity of an
            object in units of meters per second.
        area : float
            The cross-sectional surface area of the object in square meters.
        drag_coefficient: float
            The drag coefficient of the object. This quantity is unitless.
        spin : list of float
            A vector with 1 to N dimensions that describes the spin of an
            object converted to units of kilograms per second.
            
    Returns
    -------
        list of float
            A force vector that represents the sum of gravity, air resistance,
            and the Magnus effect for an object.
    """
    return add_forces([calculate_gravity(mass),
                       calculate_drag(velocity, area, drag_coefficient),
                       calculate_magnus(velocity, spin)])

def calculate_drag_and_magnus(velocity,area,drag_coefficient,spin):
    """Calculate air resistance, and the Magnus effect for an object.
    
    Parameters
    ----------
        velocity : list of float
            A vector with 1 to N dimensions that describes the velocity of an
            object in units of meters per second.
        area : float
            The cross-sectional surface area of the object in square meters.
        drag_coefficient: float
            The drag coefficient of the object. This quantity is unitless.
        spin : list of float
            A vector with 1 to N dimensions that describes the spin of an
            object converted to units of kilograms per second.
            
    Returns
    -------
        list of float
            A force vector that represents the sum of air resistance and the
            Magnus effect for an object.
    """
    return add_forces([calculate_drag(velocity, area, drag_coefficient),
                       calculate_magnus(velocity, spin)])