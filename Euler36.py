def palindrome10(n):
  strn = str(n)
  palindrome = True
  for k in range(0,len(strn)):
    if strn[k] != strn[-(k+1)]:
      palindrome = False
  return palindrome

def palindrome2(n):
  strn = bin(n)[2:]
  palindrome = True
  for k in range(0,len(strn)):
    if strn[k] != strn[-(k+1)]:
      palindrome = False
  return palindrome

s = 0
for i in range(1,1000000):
  if palindrome10(i) == True and palindrome2(i) == True:
    s += i
print s
