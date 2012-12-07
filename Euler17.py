names = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'one thousand'}
def writen(n):
  ln = len(str(n))
  letters = 0
  if n < 20 or n in [20,30,40,50,60,70,80,90,1000]:
    number = names[n]
  elif 20 < n < 100:
    ones = n % 10
    tens = n - ones
    number = names[tens]+' '+names[ones]
  elif n == 100:
    number = names[1]+' '+names[n]
  else:
    hundreds = n / 100
    ones = n % 10
    tens = n % 100 - ones
    if ones == 0 and tens == 0:
      number = names[hundreds]+' '+names[100]
    elif tens == 0:
      number = names[hundreds]+' '+names[100]+' and '+names[ones]
    elif tens == 10:
      number = names[hundreds]+' '+names[100]+' and '+names[n%100]
    elif ones == 0:
      number = names[hundreds]+' '+names[100]+' and '+names[tens]
    else:
      number = names[hundreds]+' '+names[100]+' and '+names[tens]+' '+names[ones]
  for char in number:
    if char != ' ':
      letters += 1
  return letters

n = 1000
lettersn = [0]
for i in range(1,n+1):
  lettersn.append(writen(i))
#print 'lettersn =', lettersn
sum = 0
for el in lettersn:
  sum += el
print sum
