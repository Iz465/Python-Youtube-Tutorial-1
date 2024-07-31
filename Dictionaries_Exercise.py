

Phone = input("Phone: ")

phone_map = {
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four"
}
output = ""
for ch in Phone:
  output += phone_map.get(ch, "!") + " "
print(output)

