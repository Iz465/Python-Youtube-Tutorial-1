def emoji_convert(emojis):
  words = emojis.split(" ")
  emojis = {
    ":)": "lol",
    ":(": "Wah"
  }
  output = ""
  for word in words:
    output += emojis.get(word,word) + " "
  return output


message = input(">")
result = emoji_convert(message)
print(result)