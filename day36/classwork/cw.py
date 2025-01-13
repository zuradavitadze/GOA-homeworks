def filter_list(l):
    """Filters a list to keep only integer elements.

    Args:
        l: The input list.

    Returns:
        A new list containing only the integers from the input list.
    """
    return [i for i in l if isinstance(i, int)]

# Test cases (from the image)
print(filter_list([1, 2, 'a', 'b']))        # Output: [1, 2]
print(filter_list([1, 'a', 'b', 0, 15]))    # Output: [1, 0, 15]
print(filter_list([1, 2, 'aasf', '1', '123', 123])) # Output: [1, 2, 123]

# More test cases
print(filter_list([])) # Output: []
print(filter_list([1,2,3,4,5])) # Output: [1, 2, 3, 4, 5]
print(filter_list(['a', 'b', 'c'])) # Output: []
print(filter_list([1, '2', 3.0, 4])) # Output: [1, 4] (3.0 is a float, not an int)