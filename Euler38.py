pandigital = set('123456789')

def pal(i,j,m):
  s = 0
  maxpandigital = 0
  for k in range(i,j+1):
    p = ''
    for n in range(1,m+1):
      s = n*k
      p += str(s)
#      print 'k=',k,'n=',n,'s=',s,'p=',p
    if set(p) == pandigital:
      maxpandigital = p
  return maxpandigital
ans = max([int(pal(3,8,6)),int(pal(9,9,5)),int(pal(25,33,4)),int(pal(100,333,3)),int(pal(5000,9999,2))])

print ans
