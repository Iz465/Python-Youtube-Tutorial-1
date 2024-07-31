

print("Start Game.")

start = False


while True: # True means while loop will continue untill a break statement is made in the loop
  answer = input("> ").lower() #Makes it so I don't have to repeat lower on each answer if statement
  if (answer == "help"):
    print("""
Start - to start the car.")
Stop - to stop the car.
Quit - to exit.""")
  elif(answer == "start"):
    if start: 
        print("Car already started!")
    else:
        start = True
        print("Car started...Ready to go!")
    
  elif(answer == "stop"):
    if not start:
      print("Car has already stopped!")
    else: 
      start = False
      print("Car stopped.")
    
  elif(answer == "quit"):
    break
  else:
    print("I don't understand that...")
  
