high_income = True
good_credit = False 

if(high_income ) and (good_credit):
  print("Eligible for loan")

if(high_income ) or (good_credit):
  print("Eligible for one")

if(high_income) and not (good_credit): # and not wil reverse good_credit boolen value. As it is currently false it will reverse it to true. if it were true it would be reversed to false
  print("Good for loan")