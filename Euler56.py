maxs = 0
for a in range(1,100):
  for b in range(1,100):
    x = a**b
    strx = str(x)
    s = 0
    for char in strx:
      s += int(char)
    if s > maxs:
      maxs = s
    #print a, b, s
print maxs
