message = input("> ")
words = message.split(' ') # Anywhere a space is found, it will separate the strings into multiple words and add each to a list called words
# print(words)

emojis = {
  ":)": "😊",
  ":(": "😢"
}
output = ""
for word in words:
  output += emojis.get(word, word) + " "
print(output)