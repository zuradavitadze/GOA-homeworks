def is_valid_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

# Test cases (from your example):
print(is_valid_pin("1234"))  # Output: True
print(is_valid_pin("12345")) # Output: False
print(is_valid_pin("a234"))  # Output: False

# Additional test cases:
print(is_valid_pin("123456")) # Output: True (6 digits - often allowed)
print(is_valid_pin(""))       # Output: False (empty string)
print(is_valid_pin("123"))      # Output: False (3 digits)
print(is_valid_pin("12.4"))    # Output: False (contains a non-digit)


def generate_triangle(rows):
    """Generates a triangle pattern of odd numbers.

    Args:
        rows: The number of rows in the triangle.
    """

    num = 1  # Start with the first odd number

    for i in range(1, rows + 1):  # Iterate through each row
        row_str = ""
        for j in range(i):  # Iterate for the number of elements in the row
            row_str += str(num) + "  "  # Add the number and spacing
            num += 2  # Increment to the next odd number
        print(row_str.center(rows * 4))  # Center the row and print


# Example usage:
generate_triangle(5)  # Generates the triangle with 5 rows

# To generate a triangle with a different number of rows, 
# simply change the argument:
# generate_triangle(10)  # Generates the triangle with 10 rows


