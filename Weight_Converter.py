Weight = float(input("Weight: "))
type = input("(L)bs or (K)g: ")

if(type.upper() == 'K'): # makes it so whatever they type becomes uppercase. this makes it so l and L will both count instead of just L.
   Weight /= 0.45 # Will make it 0.45 times bigger
   print(f"You are {Weight} pounds")

elif(type.upper() == 'L'):
  Weight *= 0.45
  print(f"You are {Weight} kilograms")

else:
  print("Incorrect input")
  
# all methods require paranthesis ()