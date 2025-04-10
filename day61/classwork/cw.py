import codewars_test as test

def make_upper_case(s):
    return s.upper()

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(make_upper_case("hello"), "HELLO")



        import codewars_test as test

def repeat_str(repeat, string):
    """
    Repeats a given string a specified number of times.

    Args:
        repeat (int): The number of times to repeat the string.
        string (str): The string to be repeated.

    Returns:
        str: The repeated string.
    """

    if repeat == 0:
        return ""  # Handle the case where repeat is 0

    repeated_string = ""
    for _ in range(repeat):
        repeated_string += string

    return repeated_string

@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(repeat_str(4, 'a'), 'aaaa')
        test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
        test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
        test.assert_equals(repeat_str(0, ''), '')
        test.assert_equals(repeat_str(0, 'I'), '')
        test.assert_equals(repeat_str(5, ''), '')
        test.assert_equals(repeat_str(6, 'I'), 'IIIIII')
        test.assert_equals(repeat_str(5, 'Hello'), 'HelloHelloHelloHelloHello')




        