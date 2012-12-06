n = 1000
sumn = 0
for i in range(1,n+1):
  sumn += i**i
print sumn % 10000000000
