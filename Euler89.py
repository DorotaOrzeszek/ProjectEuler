import copy

f = open("roman.txt","r")

romans = []
for line in f:
  fixedline = line.replace('\n','')
  romans.append(fixedline)
romanscopy = copy.copy(romans)

substitutes = [('DCCCC','CM'), ('CCCC','CD'), ('LXXXX','XC'), ('XXXX','XL'), ('VIIII','IX'),('IIII','IV')]

for k in range(len(romans)):
  for i in range(len(substitutes)):
    if substitutes[i][0] in romans[k]:
      replacement = romans[k].replace(substitutes[i][0],substitutes[i][1])
      romans[k] = replacement

summ = 0
for j in range(len(romans)):
  if romanscopy[j] != romans[j]:
    difference = (len(romanscopy[j]) - len(romans[j]))
    summ += difference

print summ
