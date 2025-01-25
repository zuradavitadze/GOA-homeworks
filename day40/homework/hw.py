import codewars_test as test
from solution import remove_duplicate_words

@test.describe("Fixed Tests")
def fixed_tests():
  @test.it('Basic Test Cases')
  def basic_test_cases():
    test.assert_equals(remove_duplicate_words("alpha beta gamma gamma"), "alpha beta gamma")
    test.assert_equals(remove_duplicate_words("alpha alpha beta beta gamma gamma"), "alpha beta gamma")
    test.assert_equals(remove_duplicate_words("you repeat you repeat"), "you repeat")


    import codewars_test as test
from solution import solution

@test.describe("Fixed Tests")
def fixed_tests():
  @test.it('Basic Test Cases')
  def basic_test_cases():
    test.assert_equals(solution([1, 2, 3, 4, 0]), [0, 1, 2, 3, 4])
    test.assert_equals(solution([1, 4, 0, 0, 3, 10, 5]), [0, 0, 1, 3, 4, 5, 10])
    test.assert_equals(solution([8, 9, 0, 0, 2]), [0, 0, 2, 8, 9])