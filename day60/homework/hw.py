def get_age(age):
  """
  Extracts the age from a string like "x years old".

  Args:
    age: A string representing the girl's age.

  Returns:
    The girl's age as an integer.
  """
  return int(age[0])


def feast(beast, dish):
    """
    Checks if the dish brought by the animal is allowed at the feast.

    Args:
        beast: The name of the animal (lowercase string).
        dish: The name of the dish (lowercase string).

    Returns:
        True if the dish is allowed, False otherwise.
    """
    return beast[0] == dish[0] and beast[-1] == dish[-1]



    def sum_of_arrays(array1, array2):
  """
  Calculates the sum of all elements in two arrays.

  Args:
    array1: The first array of integers.
    array2: The second array of integers.

  Returns:
    The sum of all elements in both arrays.
  """

  sum1 = sum(array1)
  sum2 = sum(array2)

  return sum1 + sum2

# Example usage:
array1 = [1, 2, 3]
array2 = [4, 5, 6]

result = sum_of_arrays(array1, array2)
print(result)  # Output: 21

array3 = [-1, 0, 1]
array4 = [10]

result2 = sum_of_arrays(array3, array4)
print(result2) #output: 11

array5 = []
array6 = []
result3 = sum_of_arrays(array5, array6)
print(result3) #output: 0