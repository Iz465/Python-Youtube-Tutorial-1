numbers = [5,2,5,2,2]

# for x in numbers: # This gives me the answer, I need this done in a nested loop though
#   print('x' * x)


# The below is the answer using nested strings
for x_count in numbers: # This does the number list. As the list has 5 things in it, the x loop will happen 5 times
  output = '' # Every time the x_count loop starts output will become nothing
  for count in range(x_count): # This will do the loop depending on what the x_count number is. So x count is five the first time, so the count will repeat five times. as it is 2 the second time it will repeat twice etc.
    output += 'x' #output will change from '' to the amount of x in the count loop. as the first count loop is 5 output will become 'xxxxx' as the second count loop is 2 it will become 'xx' and so on
  print(output) # after the count loop is done it will print the output. first count loop will be 'xxxxx' second will be 'xx' third 'xxxxx' fourth 'xx' and fifth 'xx'


print("\nSecond Exercise \n")

numbers = [1,1,1,1,5]

for x in numbers:
  output = ''
  for y in range(x):
    output+= 'x'
  print(output)