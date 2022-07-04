import numpy as np
import sympy as sym
import scipy as sci


def f1(x, y):
    return x + y + np.array([0])


def f2(x):
    return sym.Matrix([x])
