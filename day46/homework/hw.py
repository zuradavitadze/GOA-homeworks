def fizz_buzz(n):
    return ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, n+1)]


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


def solution(nums):
    return sorted(nums) if nums else []


def compare(s1, s2):
    sum_chars = lambda s: sum(ord(c) for c in s.upper()) if s and s.isalpha() else 0
    return sum_chars(s1) == sum_chars(s2)
