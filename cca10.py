l = list(range(1,101))
lEven = filter(lambda f: True if(f%2 == 0) else False, l)
# OR
# lEven = filter(lambda f: f%2 == 0, l)
print(lEven)
# OR
for i in lEven: print(i)

lOdd = filter(lambda f: f%2 != 0, l)
print(lOdd)
for i in lOdd: print(i)

lSqr = map(lambda f: f**2, lEven)
print(lSqr)

import functools as ft

lSumSqr = ft.reduce(lambda x, y: x+y, lSqr)
print(lSumSqr)
