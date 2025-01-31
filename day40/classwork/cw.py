import   test
from import friend  # Assuming friend function is in solution.py

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(friend(["Ryan", "Kieran", "Mark"]), ["Ryan", "Kieran", "Mark"])
        test.assert_equals(friend(["Ryan", "Kieran", "Mark", "123"]), ["Ryan", "Kieran", "Mark"]) # Example with a non-name

# Example implementation of the friend function (in solution.py)
def friend(friends):
    return [name for name in friends if name.isalpha()]

# You can add more test cases here as needed

def validate_pin(pin):
    try:
        if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
            return True
        else:
            return False
    except TypeError:  # In case pin is not a string
        return False