matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# matrix[0][1] = 20 # changes 2 to 20
# print(matrix[0][1])

# This nested loop will give all the items in the 2D list.
for row in matrix: # row is the three lists.
  for item in row: # item in row is the contents in each list
    print(item)