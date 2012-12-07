f = open("50digitnumbers.txt","r")
grid = []
for line in f:
  numbers = line.split(" ")
  numbers[-1] = numbers[-1][:2]
  grid.append(numbers)

def maxrow(grid):
  rowsum = 0
  for row in grid:
    for i in range(0,len(grid)-3):
      sum = int(row[i])*int(row[i+1])*int(row[i+2])*int(row[i+3])
      if sum > rowsum:
        rowsum = sum
  return rowsum

def maxcol(grid):
  colsum = 0
  for i in range(0,len(grid)-3):
    for j in range(0,len(grid)):
      sum = int(grid[i][j])*int(grid[i+1][j])*int(grid[i+2][j])*int(grid[i+3][j])
      if sum > colsum:
        colsum = sum
  return colsum

def maxdiagr(grid):
  diagrsum = 0
  for i in range(0,len(grid)-3):
    for j in range(0,len(grid)-3):
      sum = int(grid[i][j])*int(grid[i+1][j+1])*int(grid[i+2][j+2])*int(grid[i+3][j+3])
      if sum > diagrsum:
        diagrsum = sum
  return diagrsum

def maxdiagl(grid):
  diaglsum = 0
  for i in range(0,len(grid)-3):
    for j in range(3,len(grid)):
      sum = int(grid[i][j])*int(grid[i+1][j-1])*int(grid[i+2][j-2])*int(grid[i+3][j-3])
      if sum > diaglsum:
        diaglsum = sum
  return diaglsum

answer = [maxrow(grid),maxcol(grid),maxdiagr(grid),maxdiagl(grid)]
print max(answer)
