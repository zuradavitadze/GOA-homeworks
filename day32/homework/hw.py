def string_to_number(s):
  """Transforms a string into a number.

  Args:
    s: A string representing an integer.

  Returns:
    The integer represented by the string.
  """
  return int(s)

# Examples
print(string_to_number("1234"))  # Output: 1234
print(string_to_number("605"))   # Output: 605
print(string_to_number("1405"))  # Output: 1405


def high_and_low(numbers):
    """
    Finds the highest and lowest numbers in a string of space-separated numbers.

    Args:
        numbers: A string of space-separated numbers.

    Returns:
        A string containing the highest and lowest numbers, separated by a space.
        Returns an empty string if the input string is empty or contains no valid numbers.
    """
    if not numbers:  # Handle empty input
        return ""
    
    num_list = [int(x) for x in numbers.split()]
    
    if not num_list: # Handle input with no valid numbers
        return ""
        
    return str(max(num_list)) + " " + str(min(num_list))

# Examples
print(high_and_low("1 2 3 4 5"))      # Output: 5 1
print(high_and_low("1 2 -3 4 5"))     # Output: 5 -3
print(high_and_low("1 9 3 4 -5"))    # Output: 9 -5
print(high_and_low(""))              # Output: ""
print(high_and_low(" "))              # Output: ""
print(high_and_low("a b c"))        # Output: ""
