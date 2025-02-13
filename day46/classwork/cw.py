import codewars_test as test
from solution import filter_list

@test.describe('Sample tests')
def sample_tests():
    @test.it('should work for basic examples')
    def basic_examples():
        test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
        test.assert_equals(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'For input [1, "a", "b", 0, 15]')
        test.assert_equals(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')



import codewars_test as test
from solution import disemvowel

@test.describe("Fixed Tests")
def basic_tests():
    @test.it("First fixed test")
    def fixed_test_1():
        test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

    @test.it("Second fixed test")
    def fixed_test_2():
        test.assert_equals(disemvowel("No offense but,\nYour writing is terrible."), "N ffns bt,\nYr wrtng s trrbl.")

    @test.it("Third fixed test")
    def fixed_test_3():
        test.assert_equals(disemvowel("What's up with the vowels?"), "Wht's p wth th vwls?")

@test.describe("Random Tests")  # Example of adding a test group for random tests
def random_tests():
    import random
    vowels = "aeiouAEIOU"
    for _ in range(40): # Run 40 random tests
        string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for _ in range(random.randint(0, 50)))
        expected = "".join(char for char in string if char not in vowels)
        @test.it(f"Testing for {string}") # Include the input in the test description
        def random_test():
            test.assert_equals(disemvowel(string), expected)