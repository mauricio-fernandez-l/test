import numpy as np
import src.module as m


class TestSrc:
    def test_module(self):
        a = np.array([1, 2, 3])
        b = np.array([100, 200, 300])
        c = m.f(a, b)

        assert np.sum(c) == (101 + 202 + 303)
