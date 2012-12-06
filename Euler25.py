fiblist = {0:0,1:1,2:1}
def f(n):
# calculates nth Fibonacci number
  fib = 0
  if n in fiblist:
    return fiblist[n]
  else:
    fib = f(n-1)+f(n-2)
    fiblist[n] = fib
  return fib 
  
n = 1000
f(n)
f(2*n-3)
f(3*n-6)
f(4*n-9)
f(5*n-12)
m = 5*n-12

for i in range(0,m):
  if len(str(fiblist[i])) == 1000:
    print i
    break
