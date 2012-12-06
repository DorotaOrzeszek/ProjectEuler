strn = ''
i = 1
while len(strn) < 1000000:
  strn += str(i)
  i += 1
d = [strn[0],strn[9],strn[99],strn[999],strn[9999],strn[99999],strn[999999]]
p = 1
for el in d:
  p *= int(el)
print p
