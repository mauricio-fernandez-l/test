import numpy as np
import sympy as sym
import src.module as m


class TestSrc:
    def test_module(self):
        a = np.array([1, 2, 3])
        b = np.array([100, 200, 300])
        c = m.f1(a, b)

        assert np.sum(c) == (101 + 202 + 303)

    def test_sym(self):
        a = m.f2(3)
        assert a == sym.Matrix([[3]])