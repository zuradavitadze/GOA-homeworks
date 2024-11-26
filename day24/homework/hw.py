def my_split(string, separator):
  """
  Splits a string into a list of substrings based on a separator.

  Args:
    string: The string to split.
    separator: The separator to split the string by.

  Returns:
    A list of substrings.
  """

  result = []
  current_word = ""
  for char in string:
    if char == separator:
      result.append(current_word)
      current_word = ""
    else:
      current_word += char
  if current_word:
    result.append(current_word)
  return result

# მაგალითი
sentence = "This is a sample sentence"
words = my_split(sentence, " ")
print(words)  # ['This', 'is', 'a', 'sample', 'sentence']

def my_join(list_of_strings, separator):
  """
  Joins a list of strings into a single string using a separator.

  Args:
    list_of_strings: A list of strings.
    separator: The separator to join the strings with.

  Returns:
    A single string.
  """

  result = ""
  for i, word in enumerate(list_of_strings):
    result += word
    if i < len(list_of_strings) - 1:
      result += separator
  return result

# მაგალითი
words = ["Hello", "world"]
sentence = my_join(words, " ")
print(sentence)  # Hello world

def my_replace(string, old, new):
  """
  Replaces all occurrences of an old substring with a new substring.

  Args:
    string: The string to search and replace in.
    old: The substring to replace.
    new: The new substring to replace with.

  Returns:
    A new string with the replacements made.
  """

  result = ""
  i = 0
  while i < len(string):
    if string[i:].startswith(old):
      result += new
      i += len(old)
    else:
      result += string[i]
      i += 1
  return result

# მაგალითი
text = "I love apples"
new_text = my_replace(text, "apples", "bananas")
print(new_text)  # I love bananas

def mini_calculator(num1, num2, operator):
  """
  Performs a simple calculation.

  Args:
    num1: The first number.
    num2: The second number.
    operator: The operator (+, -, *, /).

  Returns:
    The result of the calculation.
  """

  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 == 0:
      return "Division by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operator"

# მაგალითი
result = mini_calculator(10, 5, '/')
print(result)  # 2.0

def get_words_from_user():
  """
  Gets a list of words from the user and joins them into a single string.
  """

  words = []
  while True:
    word = input("Enter a word (or 'q' to quit): ")
    if word == 'q':
      break
    words.append(word)

  sentence = my_join(words, " ")
  print(sentence)

get_words_from_user()