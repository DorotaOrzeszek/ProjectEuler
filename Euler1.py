stop = 1000
summ = 0

for n in range(stop):
  if n % 3 == 0 and n % 5 == 0:
    summ += n
    continue
  elif n % 3 == 0:
    summ += n
  elif n % 5 == 0:
    summ += n
  else:
    continue

print summ
