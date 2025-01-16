def manual_difference(set1, set2):
    """
    აბრუნებს set-ს, რომელიც შეიცავს set1-ის იმ ელემენტებს, რომლებიც არ არიან set2-ში.
    მუშაობს .difference() მეთოდის ანალოგიურად.

    Args:
        set1: პირველი set.
        set2: მეორე set.

    Returns:
        set: ელემენტების განსხვავება set1-სა და set2-ს შორის.
    """
    difference_set = set()
    for element in set1:
        if element not in set2:
            difference_set.add(element)
    return difference_set

# მაგალითი
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

difference = manual_difference(set1, set2)
print(f"განსხვავება set1-სა და set2-ს შორის: {difference}")  # გამოიტანს {1, 2}

# შედარება ჩაშენებულ .difference() მეთოდთან
builtin_difference = set1.difference(set2)
print(f"ჩაშენებული განსხვავება: {builtin_difference}") # გამოიტანს {1, 2}

set3 = {"apple", "banana", "cherry"}
set4 = {"banana", "date"}

difference2 = manual_difference(set3, set4)
print(f"განსხვავება set3-სა და set4-ს შორის: {difference2}") #გამოიტანს {'apple', 'cherry'}

builtin_difference2 = set3.difference(set4)
print(f"ჩაშენებული განსხვავება: {builtin_difference2}") #გამოიტანს {'apple', 'cherry'}