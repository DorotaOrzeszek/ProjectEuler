def ispalindrome(x):
  ispalindrome = False
  digits = list(x)
  if digits[0]==digits[-1] and digits[1]==digits[-2] and digits[2]==digits[-3]:
    ispalindrome = True
  return ispalindrome

palindromes = []
for a in range(100,1000):
  for b in range(100,1000):
    product = a*b
    if ispalindrome(str(product)):
      palindromes.append(product)
print max(palindromes)
