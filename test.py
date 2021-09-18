from Equation import Expression
from numpy import log as ln
from sympy import *
fn = Expression("np.log(4**4)",["x",])
print(fn)
# fn(3,5)
print(fn(2))