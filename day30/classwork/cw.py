def high_and_low(numbers):
    nums = [int(num) for num in numbers.split()]
    return f"{max(nums)} {min(nums)}"

# Example
print(high_and_low("1 2 3 4 5"))   # Output: "5 1"
print(high_and_low("1 2 -3 4 5"))  # Output: "5 -3"
print(high_and_low("1 9 3 4 -13")) # Output: "9 -13"