# open file with 100 50-digit numbers
f = open("50digitnumbers.txt",'r')
sum = long(0)
for line in f:
  sum += long(line)
print str(sum)[:10]
