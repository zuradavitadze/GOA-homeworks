def reverse_string(text):
  """
  Reverses a string using slicing.

  Args:
    text: The string to be reversed.

  Returns:
    The reversed string.
  """

  return text[::-1]

def reverse_string(text):
  """
  Reverses a string using a for loop.

  Args:
    text: The string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_text = ""
  for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
  return reversed_text

def reverse_string(text):
  """
  Reverses a string using a while loop.

  Args:
    text: The string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_text = ""
  i = len(text) - 1
  while i >= 0:
    reversed_text += text[i]
    i -= 1
  return reversed_text

def is_palindrome(text):
  return text == text[::-1]

def reverse_words(words):
  return [word[::-1] for word in words]