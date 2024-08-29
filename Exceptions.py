try:
  age = int(input("Age: "))
  income = 20000
  risk = income / age
  print(age)
except ValueError:
  print("Invalid value")
except ZeroDivisionError: # This except block occurs if age input is 0
  print("Age can't be zero")
