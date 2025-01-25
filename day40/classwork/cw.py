import codewars_test as test
from solution import is_isogram

@test.describe("Fixed Tests")
def fixed_tests():
  @test.it('Basic Test Cases')
  def basic_test_cases():
    test.assert_equals(is_isogram("Dermatoglyphics"), True)
    test.assert_equals(is_isogram("isogram"), True)
    test.assert_equals(is_isogram("Elevate"), False)
    test.assert_equals(is_isogram("Consecutive"), False)



    import codewars_test as test
from solution import validate_pin

@test.describe("Fixed Tests")
def fixed_tests():
  @test.it("should return False for pins with length other than 4 or 6")
  def test_invalid_length():
    test.assert_equals(validate_pin("123"), False)
    test.assert_equals(validate_pin("12345"), False)
    test.assert_equals(validate_pin("1234567"), False)
    test.assert_equals(validate_pin(""), False)
  
  @test.it("should return False for pins with non-numeric characters")
  def test_non_numeric_characters():
    test.assert_equals(validate_pin("123a"), False)
    test.assert_equals(validate_pin("1234!"), False)
  
  @test.it("should return True for valid pins")
  def test_valid_pins():
    test.assert_equals(validate_pin("1234"), True)
    test.assert_equals(validate_pin("0000"), True)
    test.assert_equals(validate_pin("123456"), True)