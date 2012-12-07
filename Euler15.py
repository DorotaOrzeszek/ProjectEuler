n = 20 # grid size
memory = {} 
def step(x,y):
  # x - column
  # y - row
  if (x,y) in memory:
    return memory[(x,y)]
  if x==n or y==n:
    return 1
  else:
    down = step(x,y+1)
    right = step(x+1,y)
    result = down + right
    memory[(x,y)] = result
    return result 
print step(0,0)

