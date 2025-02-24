import codewars_test as test

def xo(s):
    """
    Function counts the number of 'x's and 'o's in a string and compares them.

    :param s: The string in which to count 'x's and 'o's.
    :return: True if the number of 'x's and 'o's is equal, otherwise False.
    """

    # Convert the string to lowercase for case-insensitive comparison.
    s = s.lower()

    # Count the number of 'x's and 'o's.
    x_count = s.count('x')
    o_count = s.count('o')

    # Compare the counts and return the result.
    return x_count == o_count

@test.describe("Sample tests")
def _():
    test_cases = [
        ("ooxx", True),
        ("xooxx", False),
        ("ooxXm", True),  # Case-insensitive comparison
        ("zpzpzpp", True),  # Should return True if no 'x' and 'o' are present
        ("zzoo", False),
        ("oxOx", True),
        ("", True),  # Empty string has equal number of 'x's and 'o's
    ]

    for s, expected in test_cases:
        @test.it(f"{s = }")
        def _():
            test.assert_equals(xo(s), expected)