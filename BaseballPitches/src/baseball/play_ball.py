"""
Created on Sep 5, 2018
@author: Nick Geary

This module is used as the main program to simulate baseball pitches.
"""

from baseball import pitches, baseball_plotter as bp

distance = 18               # distance to throw the ball in meters
default_increment = 0.001   # in seconds

def lets_play(increment = default_increment):
    """This function simulates seven predefined pitches and plots their
    trajectories.
    
    Parameters
    ----------
        increment : float
            The time in seconds to let the ball travel before making a new
            calculation. An increment of 0.001 s with a distance of 18 m
            results in approximately 485 calculations per pitch. The number of
            calculations grows linearly as the increment is reduced. 
    """
    
    my_plotter = bp.BaseballPlotter()
    my_pitches = [pitches.Knuckleball(),pitches.FourSeamFastball(),
                  pitches.TwoSeamFastball(),pitches.Slider(),pitches.Curveball(),
                  pitches.Changeup(),pitches.Screwball()]

    for p in my_pitches:
        p.throw(distance,increment)
        my_plotter.add_to_plot(p)
            
    my_plotter.plot_strike_zone()
    my_plotter.show_plots()
    
def just_throw(increment = default_increment):
    """This function simulates seven predefined pitches but does not plot their
    trajectories. It is mainly been used for performance testing.
    
    Parameters
    ----------
        increment : float
            The time in seconds to let the ball travel before making a new
            calculation. An increment of 0.001 s with a distance of 18 m
            results in approximately 485 calculations per pitch. The number of
            calculations grows linearly as the increment is reduced. 
    """
    
    my_pitches = [pitches.Knuckleball(),pitches.FourSeamFastball(),
                  pitches.TwoSeamFastball(),pitches.Slider(),pitches.Curveball(),
                  pitches.Changeup(),pitches.Screwball()]
    
    for p in my_pitches:
        p.throw(distance,increment)
        
lets_play()