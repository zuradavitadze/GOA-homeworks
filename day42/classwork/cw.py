import codewars_test as test
from solution import points

@test.describe("Fixed Tests")
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(points([
            "3:1", "2:2", "1:1", "0:1", "0:2", "2:0"
        ]), 11)
        test.assert_equals(points([
            "1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"
        ]), 30)
        test.assert_equals(points([
            "1:1", "2:2", "3:3"
        ]), 0)
        test.assert_equals(points([
            "0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4"
        ]), 0)



        import codewars_test as test
from solution import fake_bin

@test.describe("Fixed Tests")
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(fake_bin('45325'), '01001')
        test.assert_equals(fake_bin('50987'), '10111')
        test.assert_equals(fake_bin('3660555'), '0110000')
        test.assert_equals(fake_bin('17668889'), '00111111')