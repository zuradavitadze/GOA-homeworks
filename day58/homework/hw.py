import codewars_test as test
from solution import vowel_one

@test.describe("Example Tests")
def example_tests():
    
    @test.it("Example Tests")
    def example_tests():

        tests = [
            # [input, expected],
            ["vowelOne", "01010101"],
            ["123, arou", "000001011"],
            ["Codewars", "01010100"],
            ["Python", "000010"]
        ]

        for inp, exp in tests:
            test.assert_equals(vowel_one(inp), exp, f"Input string = {inp !r}")


            from solution import solution
import codewars_test as test
from random import randint

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

@test.describe("Fixed Tests")
def test_group():
    @test.it("True Cases")
    def test_true_cases():
        for text, ending in fixed_tests_True:
            test.assert_equals(solution(text, ending), True)
    @test.it("False Cases")
    def test_false_cases():
        for text, ending in fixed_tests_False:
            test.assert_equals(solution(text, ending), False)
            