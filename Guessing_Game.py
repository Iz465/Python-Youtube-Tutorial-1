
Num = int(input("Guess the number: "))
Guesses = 0
Guess_Limit = 2
while (Guesses < Guess_Limit) and (Num != 9):
  Num = int(input("Wrong. Again: "))
  Guesses += 1
   
if (Num == 9):
  print(f"Correct! The number was {Num}")

else: # While statements can have an else. In the above since I put break for guessing correctly this wont run as this is still part of the while loop 
 print("Game Over. Answer was 9")
  



