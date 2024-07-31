numbers = [1,4,3,2,9,1,3,4,6,1,5]
uniques = []

# Below makes a new list which shows the original list with out any duplicates
for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)