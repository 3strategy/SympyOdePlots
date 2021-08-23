from sympy import *
from sympy.solvers.ode.systems import dsolve_system
from IPython.display import display
f, g = symbols("f g", cls=Function)
x = symbols("x")
eqs = [Eq(f(x).diff(x), g(x)), Eq(g(x).diff(x), f(x))]
sol=dsolve_system(eqs)
display(eqs[0],eqs[1],sol[0][0],sol[0][1])

display('next equation')
y = Function('y')
eq=Derivative(y(x), x,x) + 16*y(x) # took a long time to understand this is how you express a second derivative.
sol=dsolve(eq)
display(eq,sol)