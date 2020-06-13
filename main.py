import numpy as np
import src.module as m

a = np.array([1, 2, 3])
b = np.array([100, 200, 300])
c = m.f1(a, b)
print(c)

a = m.f2(3)
print(a)