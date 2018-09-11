"""
Created on Sep 5, 2018
@author: Nick Geary

This module is used to solve ordinary differential equations (ODEs) using the
Euler Method (https://en.wikipedia.org/wiki/Euler_method).
"""

def new_state(x, xp, xpp, increment):
    """Given an initial state, calculate a new state for the next step.
    
    Parameters
    ----------
        x : list of float
            A vector that represents the dependent variable. This should have 1
            to N dimensions. For example, it could be a position vector that
            represents the 3-D coordinates of an object.
        xp : list of float
            ``X prime.`` A vector that represents the first derivative of the
            dependent variable with respect to the independent variable. This
            must have the same number of dimensions as x. For example, if x is
            position and the independent variable is time, xp would be the
            velocity vector.
        xpp : list of float
            ``X double prime.`` A vector that represents the second derivative
            of the dependent variable with respect to the independent variable.
            This must have the same number of dimensions as x. For example, if
            x is position and the independent variable is time, xpp would be
            the acceleration vector.
        increment : float
            The step size by which to increase the independent variable. The
            smaller the increment, the more accurate the solution to the
            equation.
            
    Returns
    -------
        (list of float, list of float)
            The new dependent variable (e.g. position) and first derivative
            (e.g. velocity), respectively.
        
    Examples
    --------
        >>> x = [10.0, 12.5, 7.2]
        >>> v = [1.4, -2.9, 2.0]
        >>> a = [0.1, -0.2, -1.0]
        >>> dt = 0.5
        >>> euler.new_state(x, v, a, dt)
        ([10.7, 11.05, 8.2], [1.45, -3.0, 1.5])
    """
    
    # ex: x = x + x' dt
    new_x = [a + b for a, b in zip(x, [each_xp * increment for each_xp in xp])]

    # ex: x' = x' + x'' dt
    new_xp = [a + b for a, b in zip(
                               xp, [each_xpp * increment for each_xpp in xpp])]

    return new_x, new_xp