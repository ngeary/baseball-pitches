"""
Created on Sep 10, 2018
@author: Nick Geary

This module is used to plot empirical runtime data that was collected by
timing the execution of the play_ball.just_throw() method. 
"""

from matplotlib import pyplot
from numpy import arange, array, maximum

def f1(x):
    """This is a linear regression formula that approximately matches the
    runtime data for the version of the code that uses Python lists.
    """
    return 0.0001257049 * x - 0.05922626

def f2(x):
    """This is a quadratic regression formula that approximately matches the
    runtime data for the version of the code that uses Python lists.
    """
    y = 0.4037875 - 0.0003047912 * x + 3.598094 * 10**-8 * x**2
    return maximum(y, f1(x))

python_list_data = array([[5.333333333, 0.0006505298598],
                          [48.66666667, 0.005925580034],
                          [483.8333333, 0.0588020525],
                          [4834.166667, 0.5882792994],
                          [9668.666667, 1.183128028],
                          [12085.66667, 1.477727643],
                          [16114.16667, 2.012290417],
                          [24171, 2.950435183],
                          [32227.83333, 3.916890588],
                          [38673.16667, 4.759980076],
                          [48341.5, 5.939478808],
                          [96682.16667, 11.97368519],
                          [483409.6667, 60.74648483]])

x1, y1 = python_list_data.T
pyplot.scatter(x1, y1, marker='s', label='Python lists',
               facecolors='none', edgecolors='blue')

numpy_array_data = array([[5.333333333, 0.0007273493987],
                          [48.66666667, 0.0064366255],
                          [483.8333333, 0.06495003336],
                          [4834.166667, 0.7081057178],
                          [9668.666667, 1.703335227],
                          [12085.66667, 2.389831971],
                          [16114.16667, 4.285264105],
                          [24171, 12.36985018],
                          [32227.83333, 28.45259033],
                          [38673.16667, 43.25666966],
                          [48341.5, 69.41480786]])

x2, y2 = numpy_array_data.T
pyplot.scatter(x2, y2, marker='^', label='NumPy Arrays',
               facecolors='none', edgecolors='red')

xrange = arange(0.0, 50000.0, 1.0)

pyplot.plot(xrange, f2(xrange), linewidth=1.2,
            linestyle='--', color='red')
pyplot.plot(xrange, f1(xrange), linewidth=1.2,
            linestyle='--', color='blue')

pyplot.xlim(0.0, 50000.0)
pyplot.ylim(0.0, 75.0)

pyplot.xlabel('Iterations')
pyplot.ylabel('Runtime (s)')
pyplot.title('Runtime vs. Iterations')

pyplot.legend(loc='upper left')

pyplot.show()