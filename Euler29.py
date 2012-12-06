n = 100
terms = []
for a in range(2,n+1):
  for b in range(2,n+1):
    terms.append(a**b)
    terms.append(b**a)
answer = set(terms)
print len(answer)
