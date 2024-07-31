numbers= [5,2,1,7,4,5]

numbers.append(20) # This adds an item to the end of the list, 20 will be added.

numbers.insert(0,10) # Insert command makes it so it adds a new item to the list in whichever index you want
# So the index im using will add the number 10 to index 0. The original index 0 item 5 and every index item after
# will be pushed one index higher.

numbers.remove(5) # This will remove the number, not the index. As we have a 5 in the list, that 5 will be removed.

numbers.clear() # This clears every item from the list, making the list empty.

numbers.pop() # Removes the last item of the list. In other words the item in the highest index.

print(numbers.index(7)) # This will print the index of number 7 in the list. Number 7 is in index 3 therefore 3 will be printed

print(numbers.index(50)) # This item is not in the list, therefore there will be an error

print(50 in numbers) # This checks if the number 50 is in the list. It will give a boolean of either truth or false

print(numbers.count[5]) # This will print the amount of 5 numbers in the list. As there are two 5 numbers it will print 2.

numbers.sort() # This will sort the list from lowest to highest. so if i print the list it will now have the lowest numbers first and highest last

numbers.reverse() # This does the opposite of sort, making the numbers in the list start from highest to lowest

numbers2 = numbers.copy # This is how you make a copy of a list. Any changes done to either of these lists will not affect the other list
