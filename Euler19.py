months = [31,28,31,30,31,30,31,31,30,31,30,31]
leapmonths = [31,29,31,30,31,30,31,31,30,31,30,31]

firstdayofmonth = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
firstdayofleapmonth = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

start = 1901
stop = 2000
leapyears = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000]

# creating daylist for 4-year slices:
d = [1]
j = 25
while j > 0:
  i = 3
  while i > 0:
    for el in months:
      d.append(d[-1]+el)
    i -= 1
  for el in leapmonths:
    d.append(d[-1]+el)
  j -= 1
firstdays = d

sundays = []
for i in range(1,firstdays[-1]):
  if (i+1) % 7 == 0:
    sundays.append(i)

count = 0
for el in firstdays:
  if el in sundays:
    count += 1
    
print count
