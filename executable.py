from sympy import *
import numpy as np
import time

# Symbol instance for the variable
x = Symbol('x')

# A string as an input to convert to a mathematical expression
func_str = input('Type your function expression. Use Python Syntax: ')

# The input function is converted to a SymPy expression
func = sympify(func_str).expand()
print(f"f(x) = {func} \nf'(x) = {func.diff(x)}")

# Converted to a function
f = lambdify(x, func)

# compute the first derivate
df = lambdify(x, func.diff(x))

# Compute second derivate
df2 = lambdify(x, func.diff(x,2))

def Newton_Raphson(x_i, i, **kwargs):
    """## Newton Raphson Method
    Using the formula for Newton-Rapshon recursion to compute 
    the roots of a real-valued continuous and differentiable 
    function, given an initial value.

    ### Parametters
    - func_expr: The function's expression. A function of the independent variable ' x '.

    - x_i: Short for 'x initial'. The initial value for the recursion
    to start with.

    - i: The number of iterations desired.

    - *args: When being used in third party programs, pass the functions and its derivates as 
    additional arguments (f, df, *df2)
    """
    mod = kwargs.get('modified', False)

    # If the initial value x_i is already a root
    if f(x_i) == 0:
        print('A root was passed as initial value x_0')
        return None

    if i == 0:
        print('Initial value: x_0 =', x_i)
        return x_i
    else:
        # Reduce the iteration number progresively
        i -= 1
        
        # Compute for the immediately previous value
        x_I = Newton_Raphson(x_i, i, **kwargs)

        if mod:
            # Modified NR formula 
            x_II = x_I - (f(x_I)*df(x_I))/(df(x_I)**2 - f(x_I)*df2(x_I))
        else:
            # Simple NR formula
            x_II = x_I - (f(x_I) / df(x_I))

        # relative error
        rel_error = (abs(x_II - x_I) / abs(x_II))
        
        time.sleep(0.5)

        print(f'Iteration {i+1}  |  x_{i+1} = {x_II}, Normalized Error: {round(rel_error, 8)}')
        return x_II
    
# choose between simple and modified method
formula = input('Use modified NR? yes or no: [y/n]: ')
while formula not in ['y', 'n']:
    formula = input('Use modified NR? yes or no: [y/n]: ')

# ask for parametters
initial_value = float(input('Type the initial vale for x_0: '))
num_iterations = int(input('Type the number of iterations (an integer): '))

if formula == 'y':
    aprox = Newton_Raphson(
        initial_value,
        num_iterations,
        modified=True
    )
elif formula == 'n':
    aprox = Newton_Raphson(
        initial_value,
        num_iterations
    )

print('- -' * 10)
print('f(x) has a root in x =', aprox)