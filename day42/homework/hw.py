import codewars_test as test
from solution import sum_mix

@test.describe("Fixed Tests")
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_mix([9, 3, '7', '3']), 22)
        test.assert_equals(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
        test.assert_equals(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)

        import codewars_test as test
from solution import double_char

@test.describe("Fixed Tests")
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(double_char("String"), "SSttrriinngg")
        test.assert_equals(double_char("abc"), "aabbcc")
        test.assert_equals(double_char("Hi-There"), "HHii--TThheerree")
        test.assert_equals(double_char("1234!_ "), "11223344!!__  ")