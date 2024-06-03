from sympy import *
import argparse

x = Symbol('x')
f, df, df2 = symbols('f, df, df2', cls=Function)

# Implementation of Newton's method

# f = function
# df = function

# The system
def Newton_Raphson(x_i, i):
    """## Newton Raphson Method
    Using the formula for Newton-Rapshon recursion to compute 
    the roots of a real-valued continuous and differentiable 
    function, given an initial value.

    ### Parametters
    - func_expr: The function's expression. A function of the independent variable ' x '.

    - x_i: Short for 'x initial'. The initial value for the recursion
    to start with.

    - i: The number of iterations desired.
    """

    if i == 0:
        print('Initial value: x_0 =', x_i)
        return x_i
    else:
        # Reduce the iteration number progresively
        i -= 1
        
        # Compute for the immediately previous value
        x_I = Newton_Raphson(x_i, i)

        # NR formula 
        x_II = x_I - (f(x_I) / df(x_I))

        # relative error
        rel_error = (abs(x_II - x_I) / abs(x_II))

        print(f'Iteration {i+1}  |  x_{i+1} = {x_II}, relative error: {round(rel_error, 6)}')
        return x_II
    
# Modified method
def Newton_Raphson_modified(x_i, i):
    """## Newton Raphson Method
    Using the formula for Newton-Rapshon recursion to compute 
    the roots of a real-valued continuous and differentiable 
    function, given an initial value.

    ### Parametters
    - func_expr: The function's expression. A function of the independent variable ' x '.

    - x_i: Short for 'x initial'. The initial value for the recursion
    to start with.

    - i: The number of iterations desired.
    """

    if i == 0:
        print('Initial value: x_0 =', x_i)
        return x_i
    else:
        # Reduce the iteration number progresively
        i -= 1
        
        # Compute for the immediately previous value
        x_I = Newton_Raphson_modified(x_i, i)

        # NR formula 
        x_II = x_I - (f(x_I)*df(x_I)) / (df(x_I)**2 - f(x_I)*df2(x_I))

        # relative error
        rel_error = (abs(x_II - x_I) / abs(x_II))

        print(f'Iteration {i+1}  |  x_{i+1} = {x_II}, relative error: {round(rel_error, 6)}')
        return x_II
    

if __name__ == '__main__':

    x, y, z = symbols('x y z')

    # Ask for the function expression
    expr = input('Write your function (acordding to python syntax): ')

    # convert it to sympy expression object and print
    func = sympify(expr).expand()
    print(f"f(x) = {func} \nf'(x) = {func.diff(x)}")

    # Converted to a python function
    f = lambdify(x, func)

    # compute the first derivate and convert to a python function
    df = lambdify(x, func.diff(x))


    # Ask for the parametters
    init_val = float(input('Type the initial value X_0 =  '))
    iters = int(input('How many iterations of the method? Enter an integer value: '))

    # execute the function
    Newton_Raphson(
        x_i=init_val,
        i=iters)