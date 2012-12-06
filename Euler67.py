f = open("triangle.txt","r")
textfile = f.readline()
t = eval(textfile)
memory = {} 
def maximize(x,y):
  # x = place in row
  # y = row
  if (x,y) in memory:
    return memory[(x,y)]
  
  if y == len(t)-1:
    result = t[y][x]
  else:
    left_price = maximize(x,y+1)
    right_price = maximize(x+1,y+1)
    result = max(left_price, right_price) + t[y][x]
  
  memory[(x, y)] = result
  return result

print maximize(0,0)
