import codewars_test as test
from solution import lottery

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(lottery("wQ8Hy0y5m5oshQPeRCkG"), "805")
        test.assert_equals(lottery("ffaQtaRFKeGIIBIcSJtg"), "One more run!")
        test.assert_equals(lottery("555"), "5")
        test.assert_equals(lottery("HappyNewYear2020"), "20")
        test.assert_equals(lottery("20191224isXmas"), "20194")
        test.assert_equals(lottery(""), "One more run!")


        import codewars_test as test
from solution import longest_word

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals( longest_word('a b c d each') , "each" )
        test.assert_equals( longest_word('each step') , "step" )
        test.assert_equals( longest_word('forward each step going') , "forward" )
        test.assert_equals( longest_word('brings each step going') , "brings" )
        test.assert_equals( longest_word('each step forward brings opportunity') , "opportunity" )