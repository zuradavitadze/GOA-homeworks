import codewars_test as test

def sort_by_length(arr):
    """
    Sorts an array of strings by length in descending order.
    """
    return sorted(arr, key=len, reverse=True)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():

        tests = [
            [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
            [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
            [["short", "longer", "longest"], ["longer", "longest", "short"]],
            [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
            [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
            [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
        ]
        
        for exp, inp in tests:
            test.assert_equals(sort_by_length(inp), exp)




            import codewars_test as test

def sequence_sum(begin_number, end_number, step):
    """
    Calculates the sum of a sequence of numbers.
    """
    if begin_number > end_number:
        return 0

    total_sum = 0
    current_number = begin_number

    while current_number <= end_number:
        total_sum += current_number
        current_number += step

    return total_sum

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sequence_sum(2, 6, 2), 12)
        test.assert_equals(sequence_sum(1, 5, 1), 15)
        test.assert_equals(sequence_sum(1, 5, 3), 5)
        test.assert_equals(sequence_sum(0, 15, 3), 45)
        test.assert_equals(sequence_sum(16, 15, 3), 0)
        test.assert_equals(sequence_sum(2, 24, 22), 26)
        test.assert_equals(sequence_sum(2, 2, 2), 2)
        test.assert_equals(sequence_sum(2, 2, 1), 2)
        test.assert_equals(sequence_sum(1, 15, 3), 35)
        test.assert_equals(sequence_sum(15, 1, 3), 0)




import codewars_test as test

def series_sum(n):
    """
    Calculates the sum of the following series up to nth term(inclusive).

    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...

    Rules:
    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return 0.00
    """
    if n == 0:
        return "0.00"

    total_sum = 0
    denominator = 1

    for _ in range(n):
        total_sum += 1 / denominator
        denominator += 3

    return "{:.2f}".format(total_sum)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(series_sum(1), "1.00")
        test.assert_equals(series_sum(2), "1.25")
        test.assert_equals(series_sum(3), "1.39")
        test.assert_equals(series_sum(4), "1.49")
        test.assert_equals(series_sum(5), "1.57")
        test.assert_equals(series_sum(0), "0.00")
        test.assert_equals(series_sum(15), "1.94")