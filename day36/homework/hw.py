def int_to_digit_list(n):
    """Converts an integer to a list of its digits.

    Args:
        n: The integer to convert.

    Returns:
        A list of integers representing the digits, or [0] if n is 0.
        Returns an empty list if n is not an integer.
    """

    if not isinstance(n, int):  # Check if n is an integer
        return []

    if n == 0:
        return [0]

    digits = []
    if n < 0:
        n = abs(n)
        sign = -1
    else:
        sign = 1

    while n > 0:
        digits.insert(0, n % 10) # Insert at the beginning to maintain correct order.
        n //= 10

    return digits

# Test cases
print(int_to_digit_list(35231))  # Output: [3, 5, 2, 3, 1]
print(int_to_digit_list(0))      # Output: [0]
print(int_to_digit_list(123456789)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(int_to_digit_list(-123)) # Output: [1, 2, 3]
print(int_to_digit_list("not an int")) #Output: []