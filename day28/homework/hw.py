def search(text, word):
  """Checks if word is a substring of text."""
  if word in text:
    return True  # Or the starting index if needed: return text.find(word)
  else:
    return False

text = input()
word = input()
print(search(text, word))