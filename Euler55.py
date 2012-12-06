def ispalindrome(n):
  ispal = True
  strn = str(n)
  for i in range(0,len(strn)/2):
    if strn[i] != strn[-i-1]:
      ispal = False
      break
  return ispal
  
def lychrel(n,d): # d - depth of recursion
  l = True
  strn = str(n)
  revn = strn[::-1]
  ans = int(strn) + int(revn)
  if ispalindrome(ans):
    l = False
  elif d >= 50:
    l = True
  else:
    l = lychrel(ans,d+1)
  return l    

#print ispalindrome(887)
c = 0
for i in range(1,10000):
  if lychrel(i,1) == True:
    print i,
    c += 1
print c
