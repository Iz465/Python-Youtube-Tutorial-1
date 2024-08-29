def greet_user(first_name, last_name):
  print (f'Hi {first_name} {last_name}!')
  print('Welcome aboard')


# When functions have parameters with variables in them, the things you put in them are called arguments
# These arguments are called positional arguments as the order you put them in change what result you get

print('Start')
greet_user(last_name="Smith", first_name="John") # This is the use of keyword arguments, instead of positional arguments. Keyword arguments can improve readability
print("Finish")


def square(number):  # This functions use the return function.
  return number * number

print (square(5)) # You can pass it directly into the print function.