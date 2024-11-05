def reverse_word(text, word_to_reverse):
  """
  This function reverses a specified word in a given text.

  Args:
    text: The input text.
    word_to_reverse: The word to be reversed.

  Returns:
    The modified text with the reversed word.
  """

  words = text.split()
  reversed_word = word_to_reverse[::-1]
  result = []
  for word in words:
    if word == word_to_reverse:
      result.append(reversed_word)
    else:
      result.append(word)
  return ' '.join(result)

# ტექსტი, რომელშიც სიტყვა უნდა შეიცვალოს
text = "დღეს მიერ წსწავლი მასალთ შევატრიალკთ სიტყვა "name" შეატრიალეთ უკუთღმა"

# სიტყვა, რომელიც უნდა შეიცვალოს
word_to_reverse = "name"

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
result = reverse_word(text, word_to_reverse)
print(result)