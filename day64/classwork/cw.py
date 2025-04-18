def make_upper_case(s):
  """Converts a string to uppercase.

  This function takes a string as input and returns a new string
  where all characters have been converted to their uppercase versions.

  Args:
    s: The input string that needs to be converted to uppercase.
       It can be any string, including empty strings, strings with
       only lowercase letters, strings with mixed-case letters,
       or strings with non-alphabetic characters.

  Returns:
    A new string that is the uppercase version of the input string `s`.
    If the input string is empty, an empty string is returned.
  """
  uppercase_string = s.upper()  # Use the built-in .upper() method
  return uppercase_string


def minimum(arr):
  """
  Finds the minimum value in a list of numbers.

  Args:
    arr: A list of numbers.

  Returns:
    The smallest number in the list.
  """
  min_val = arr[0]  # Initialize with the first element
  for num in arr:
    if num < min_val:
      min_val = num
  return min_val

def maximum(arr):
  """
  Finds the maximum value in a list of numbers.

  Args:
    arr: A list of numbers.

  Returns:
    The largest number in the list.
  """
  max_val = arr[0]  # Initialize with the first element
  for num in arr:
    if num > max_val:
      max_val = num
  return max_val