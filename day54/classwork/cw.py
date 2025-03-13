import codewars_test as test
from solution import angle

def angle(n):
    """
    Calculates the total sum of internal angles (in degrees) in an n-sided simple polygon.
    """
    return (n - 2) * 180

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(angle(3), 180)
        test.assert_equals(angle(4), 360)
        test.assert_equals(angle(5), 540)
        test.assert_equals(angle(6), 720)
        test.assert_equals(angle(7), 900)
        test.assert_equals(angle(8), 1080)
        test.assert_equals(angle(9), 1260)
        test.assert_equals(angle(10), 1440)




        import codewars_test as test

def solution(arr):
    """
    Sorts a list of numbers in ascending order.
    Returns an empty list if the input is None or an empty list.
    """
    if arr is None or len(arr) == 0:
        return []
    return sorted(arr)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution([1,2,3,10,5]), [1,2,3,5,10])
        test.assert_equals(solution(None), [])
        test.assert_equals(solution([]), [])
        test.assert_equals(solution([20,2,10]), [2,10,20])
        test.assert_equals(solution([2,20,10]), [2,10,20])




        import codewars_test as test

def in_asc_order(arr):
    """
    Checks if a list of numbers is in ascending order.
    Returns True if the list is in ascending order, False otherwise.
    """
    if not arr:
        return True  # Empty lists are considered sorted

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        arr = [1, 2]
        test.assert_equals(in_asc_order(arr), True)

        arr = [2, 1]
        test.assert_equals(in_asc_order(arr), False)

        # Array of 3 integers
        arr = [1, 2, 3]
        test.assert_equals(in_asc_order(arr), True)

        arr = [1, 3, 2]
        test.assert_equals(in_asc_order(arr), False)

        # More complex cases
        arr = [1,4,13,97,508,1047,20058]
        test.assert_equals(in_asc_order(arr), True)

        arr = [56,98,123,67,742,1024,32,90969]
        test.assert_equals(in_asc_order(arr), False)
    
    @test.it('Empty List Test')
    def empty_list_test():
        test.assert_equals(in_asc_order([]), True)


        