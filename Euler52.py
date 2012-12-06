p = []
for i in range(1,7):
  p += range(int(10**(i-1)),int(10**(i-1)*1.6666666666)+1)
for x in p:
  digits = set(str(x))
  if digits == set(str(2*x)) == set(str(3*x)) == set(str(4*x)) == set(str(5*x)) == set(str(6*x)):
    print x
    break
