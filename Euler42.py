f = open("words.txt","r")
data = f.read().split(',')
words = list(data)
triangles = [n*(n+1)/2 for n in range(0,1000)]

trianglewords = 0
for word in words:
  wordvalue = 0
  for char in word:
    if char == '"':
      continue
    wordvalue += ord(char)-64
  if wordvalue in triangles:
    trianglewords += 1
print trianglewords
