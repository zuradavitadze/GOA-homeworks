list_of_names = ["დავით", "გიორგი", "ანა", "დავით"]

name_to_count = "დავით"
count = list_of_names.count(name_to_count)
print(f"სახელი '{name_to_count}' სიაში {count} ჯერ მეორდება.")  


numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


list_of_numbers = [1, 2, 3]
result = list_of_numbers * len(list_of_numbers)
print(result)


programming_languages = ["Python", "Java", "C++"]
programming_languages.insert(1, "JavaScript")
print(programming_languages)


fruits = ["apple", "banana", "apple", "orange"]
count = fruits.count("apple")
fruits.remove("apple")
print(count)
print(fruits)