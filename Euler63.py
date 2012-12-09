ans = []
for a in range(1,500):
  for i in range(1,500):
    n = a**i
    if len(str(n)) == i:
      ans.append((n,a,i))
print len(ans)
# biggest such number is
# 109418989131512359209 = 9^21
