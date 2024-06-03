from sympy import *
import numpy as np
import matplotlib.pyplot as plt

init_printing()

x, y, z = symbols('x y z')

expression = input('Write your function')

# convert it to sympy expression object
func = sympify(expression).expand()

# Converted to a function
f = lambdify(x, func)

# compute the first derivate
df = lambdify(x, func.diff(x))

print(f"f(x) = {func} \nf'(x) = {func.diff(x)}")



# x = np.linspace(-10,10,100)
# y = x**2

# plt.plot(x,y)
# plt.show()