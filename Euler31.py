coins = [200, 100, 50, 20, 10, 5, 2, 1]
def maken(n,m): # m - max coin
  if n <= 1:
    return 1 # way of choosing coin
  count = 0
  for coin in coins:
    if (n >= coin) and (coin <= m):
      count += maken(n-coin,coin)
  return count
    
print maken(200,200)
