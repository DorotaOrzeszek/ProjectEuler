# matrix.txt -> datafile
f = open("matrix.txt","r")
textfile = f.readline()
t = eval(textfile)
memory = {} 
def minimize(x,y):
  # x = place in row
  # y = row
  if (x,y) in memory:
    return memory[(x,y)]
  
  if y == len(t)-1 and x == len(t)-1:
    result = t[y][x]
  elif y == len(t)-1:
    result = minimize(x+1,y) + t[y][x]
  elif x == len(t)-1:
    result = minimize(x,y+1) + t[y][x]
  else:
    left_price = minimize(x,y+1)
    right_price = minimize(x+1,y)
    result = min(left_price, right_price) + t[y][x]
  memory[(x, y)] = result
  return result

print minimize(0,0)
