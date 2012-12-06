factorials = [1]
def factorial(n):
  fact = 0
  if n == 1:
    fact = 1
  else:
    fact = factorial(n-1)*n
  return fact
  
n = 100
number = factorial(n)
sum = 0
for char in str(number):
  sum += int(char)
print sum
