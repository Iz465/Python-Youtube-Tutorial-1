names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0]) # Will give index 0 of the list, so John
print(names[3]) # Index 3 is Sarah
print(names[-1]) # Index -1 is the last item in the list, so Mary
print(names[-3]) # Index -3 is Mosh as Mosh is the third last item
print(names[2:]) # Will give all items from index 2 and beyond. So Mosh and all other items after.
print(names[2:4]) # Will give all items from index 2 to index 3. Index 4 wont count, its always the one index under it.

# Every time we do the above, its making a new list, not modifying the original, so if I print  names now it will still give all the original names

names[0] = 'Jon' # This modifies the item in index one. When I print the list John will now be Jon. 
print(names)  

# Below is the solution for finding the largest number in the list
numbers = [4,1,2,9,3]
largest = numbers[0]

for number in numbers:
  if number > largest:
    largest = number
print(largest)

