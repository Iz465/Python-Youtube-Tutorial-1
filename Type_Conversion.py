birth_year = int(input('Birth Year: ')) #must convert number to int or it will be '10' instead of 10
print(type(birth_year))
age = 2024 - birth_year
print(age)
print(type(age))
int()
float()
bool()

pounds = input("What is your weight in pounds? ")
kilograms = float(pounds) * 0.45
print("Your weight in kilograms is ", kilograms)