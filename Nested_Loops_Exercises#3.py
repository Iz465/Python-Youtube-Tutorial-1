

rows = 5
for i in range(rows): # this will iterate 5 times
  for j in range(rows - i - 1): # this will choose when the star starts by choosing how many leading spaces there will be so for this, it will first print 4 spaces, then 3 then 2 etc for each line.
    print(" ", end ="")
  for k in range(2 * i + 1):
    print("*", end="")
  print()