from sympy import *
import math
from numpy import linspace
import matplotlib.pyplot as pl
from IPython.display import display

x=symbols('x')
f = (x**2+1)/(x-1)
display(f)  #this does not display Latex Rendering on pycharm output
# f=sin(x)  # f נגדיר את
g=cos(x)
display(f,g)
fx=lambdify(x,f,modules=['numpy'])
gx=lambdify(x,g,modules=['numpy'])
xVals=linspace(-10,10,100)
pl.plot(xVals,fx(xVals))
pl.plot(xVals,gx(xVals))
pl.xlabel('x')
pl.ylabel(f)
pl.show()