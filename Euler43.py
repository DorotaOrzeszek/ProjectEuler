import itertools
p = itertools.permutations('0123456789')
plist = list(p)
lenplist = len(plist)
for i in range(0,lenplist):
  perm = "".join(plist[i])
  plist[i] = perm
anssum = 0
for el in plist:
  if el[0] == '0':
    continue
  d234 = int(el[1]+el[2]+el[3])
  d345 = int(el[2]+el[3]+el[4])
  d456 = int(el[3]+el[4]+el[5])
  d567 = int(el[4]+el[5]+el[6])
  d678 = int(el[5]+el[6]+el[7])
  d789 = int(el[6]+el[7]+el[8])
  d8910 = int(el[7]+el[8]+el[9])
  if d234%2==0 and d345%3==0 and d456%5==0 and d567%7==0 and d678%11==0 and d789%13==0 and d8910%17==0:
    anssum += int(el)
print anssum  

