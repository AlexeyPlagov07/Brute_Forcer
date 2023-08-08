import itertools
def foo(l):
  for i in range(1, 101):
    yield from itertools.product(*([l] * i)) 

for x in foo('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()[]{},.<>?|;:`~'):
  print(''.join(x))
