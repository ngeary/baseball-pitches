"""
Created on Sep 6, 2018
@author: Nick Geary

This module plots the trajectory of pitches. 
"""

from matplotlib import pyplot

lw = 1.0    # line width

def get_axis(input_list, i):
    """Given a multi-dimensional list, return the i-th element of each
    constituent list.
    
    Parameters
    ----------
        input_list : list
            A list with 0 to N dimensions.
        i : int
            The axis to return. 0 <= i < N, where N is the number of
            dimensions in input_list.
    
    Examples
    --------
        >>> L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> print(get_axis(L, 1))
        [2, 5, 8]
    """
    return [a[i] for a in input_list]

class BaseballPlotter:
    """This class is used to build a figure with two subplots, add the
    trajectory of pitches to the subplots, and add an outline of the strike
    zone to the subplots.
    """
    
    def __init__(self):
        """Build a figure with two subplots. Set face color, min/max values,
        axis labels, and title.
        """
        self.figure, (self.axes_1, self.axes_2) = pyplot.subplots(2, 1)
        self.figure.patch.set_facecolor('tan')
        
        self.axes_1.set_ylim(ymin=0.0, ymax=2.0)
        self.axes_1.set_ylabel("Height (m)")
        self.axes_1.set_title("Side View of Trajectory")        
        
        self.axes_2.set_ylim(ymin=-0.75, ymax=0.75)
        self.axes_2.set_xlabel("Depth (m)")
        self.axes_2.set_ylabel("Width (m)")
        self.axes_2.set_title("Top View of Trajectory")        
        
    def add_to_plot(self, pitch):
        """Add a single pitch to both subplots.
        
        Parameters
        ----------
            pitch : baseball.Pitch
                The pitch to add to the subplots. The pitch.trail attribute
                should be populated before this function is called.        
        """
        # plot Y (height) versus X (depth)
        self.axes_1.plot(get_axis(pitch.trail, 0), get_axis(pitch.trail, 1), 
                         color=pitch.color, label=pitch.label, linewidth=lw)
        
        # plot Z (width) versus X (depth)
        self.axes_2.plot(get_axis(pitch.trail, 0), get_axis(pitch.trail, 2),
                         color=pitch.color, label=pitch.label, linewidth=lw)  
        
    def plot_strike_zone(self):
        """Add the outline of the strike zone to both subplots."""
        self.axes_1.axhline(y=0.45, linestyle='--', color='red',
                            label="Strike zone", linewidth=lw)
        self.axes_1.axhline(y=1.05, linestyle='--', color='red', linewidth=lw)
        self.axes_2.axhline(y=0.235, linestyle='--', color='red',
                            label="Strike zone", linewidth=lw)
        self.axes_2.axhline(y=-0.235, linestyle='--', color='red',
                            linewidth=lw)
    
    def show_plots(self):
        """Enable the legends and display the figure with two subplots."""
        self.axes_1.legend(loc="lower left")
        self.axes_2.legend(loc="upper left")
        pyplot.show()
