customer = { # This is a dictionary
  "name": "John Smith",
  "age": 30,
  "is_verified": True
} 
customer["name"] # This will give name of the customer dictionary, so John Smith
print(customer.get("name")) # This is a method to print it out without causing an error if it doesnt exist
print(customer.get("name", "Jan 1980"))

customer["name"] = "Jack Smith"
print(customer["name"]) # will print Jack Smith