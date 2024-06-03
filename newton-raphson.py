from sympy import *
import numpy as np
import matplotlib.pyplot as plt

init_printing()

# let's print some functions in the terminal
x, y, z = symbols('x y z')

expression = y*exp(2*x) - 2*x*y + (y**2)*(x**3)

print(expression)

x = np.linspace(-10,10,100)
y = x**2

plt.plot(x,y)
plt.show()