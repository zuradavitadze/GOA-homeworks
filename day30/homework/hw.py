def high_and_low(numbers):
    try:
        nums = [int(num) for num in numbers.split()]
        if not nums:  # Handle empty input
            return ""
        return f"{max(nums)} {min(nums)}"
    except ValueError:  # Handle non-numeric input
        return "Invalid input"

# Test cases
print(high_and_low("1 2 3 4 5"))        # Output: "5 1"
print(high_and_low("1 2 -3 4 5"))       # Output: "5 -3"
print(high_and_low(""))                 # Output: ""
print(high_and_low("1"))                # Output: "1 1"
print(high_and_low("1 2 abc 4"))      # Output: "Invalid input"
print(high_and_low("   1   2   3  ")) # Output: "3 1" (handles extra spaces)