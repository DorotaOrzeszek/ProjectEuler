def fibo(n):
  memo = {1:1, 2:2}
  if n not in memo:
    memo[n] = fibo(n-1) + fibo(n-2)
  return memo[n]

summ = 0
i = 1
while True:
  value = fibo(i)
  if value > 4000000:
    break
  else:
    if value % 2 == 0:
      summ += value
  i += 1
print summ
