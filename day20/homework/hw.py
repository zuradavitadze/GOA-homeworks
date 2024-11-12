def count_vowels(words):
  vowels = "აეიოუ"
  for word in words:
    vowel_count = 0
    for char in word:
      if char in vowels:
        vowel_count += 1
    print(f"სიტყვა '{word}' შეიცავს {vowel_count} ხმოვანს.")

words = ["კომპიუტერი", "პროგრამირება", "პითონი"]
count_vowels(words)


def multiples_of_5_and_3(limit):
  for num in range(1, limit + 1):
    if num % 5 == 0 and num % 3 == 0:
      print(num)

multiples_of_5_and_3(30)


def combine_chars_and_nums():
  chars = "abcdefg"
  nums = "1234567"
  combined_string = ""
  for char in chars:
    for num in nums:
      combined_string += char + num
  print(combined_string)

combine_chars_and_nums()


def print_diamond(size):
  for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))
  for i in range(size - 2, -1, -1):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))

print_diamond(4)


def check_age():
  age = int(input("რამდენი წლის ხარ? "))
  if age > 12:
    print("შენ არ ხარ 12 წლის")

check_age()