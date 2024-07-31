
for i in range(1,11): # goes from 1 to 10
  for j in range(1,11): # goes from 1 to 10
    print(f"{i * j:3}", end = " ") # i * j makes it so each i number is * by the full y loop, so it will do 1 x 1,2,3,4,5 etc till 10. 
    # the j:3 makes it so each number takes the space of three digits, to format it better. end is a function that makes it so whatever is in it prints at the end of the y loop. 
    # the endline ignores the prints original new lines. End line is important as it makes it only do the end line once. Without it, it would do the end line 10 times.
  print() # This print line will make each loop start on a new line.


