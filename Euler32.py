pandigital = set('123456789')
ans = []
for m in range(1,1000):
  for n in range(100,10000):
    mn = m*n
    mnmn = (str(m)+str(n)+str(mn))
    if len(mnmn) == 9 and (set(mnmn) == pandigital):
      ans.append(mn)
ans2 = list(set(ans))
sumans = 0
for el in ans2:
  sumans += el
print sumans
