import fractions
ans = []
for i in range(1,10):
  for j in range(1,10):
    for n in range(1,10):
      if (10*i+j)/i == (10*j+n)/n:
        a = 10*i+j
        b = 10*j+n
        ans.append((a,b))

for el in list(ans):
  print el,'==>'
  if (fractions.gcd(el[0],el[1])==1) or (el[0]%11==0 and el[1]%11==0):
    ans.remove(el)
print "Candidate fractions:", ans
# answer to problem = 100
