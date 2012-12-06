n = 1001
rightup = [1]
leftup = [1]
leftdown = [1]
rightdown = [1]
for i in range(1,n/2+1):
  rightup.append(rightup[-1]+2*i*4)
  leftup.append(leftup[-1]+2*i*4-2)
  leftdown.append(leftdown[-1]+2*i*4-4)
  rightdown.append(rightdown[-1]+2*i*4-6)

diagonals = rightup+leftup+leftdown+rightdown
answer = 0
for el in diagonals:
  answer += el
answer -= 3
print answer
