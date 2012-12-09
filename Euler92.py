d = {1:1, 89:89}
for n in range(1,10000000):
  strn = str(n)
  if n in d:
    continue
  destiny = n
  while destiny != 1 and destiny != 89:
    if destiny in d:
      destiny = d[destiny]
      break
    strdestiny = str(destiny)
    destiny = 0
    for digit in strdestiny:
      destiny += int(digit)**2
  d[n] = destiny

count89 = 0
for element in d:
  if d[element] == 89:
    count89 += 1
print count89
