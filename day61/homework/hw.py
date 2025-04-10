def to_alternating_case(string):
    """
    Converts a string to alternating case.

    Args:
        string (str): The input string.

    Returns:
        str: The string with alternating case.
    """
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

# Example Usage and Tests (using assert for simplicity)
assert to_alternating_case("hello world") == "HELLO WORLD"
assert to_alternating_case("HELLO WORLD") == "hello world"
assert to_alternating_case("hello WORLD") == "HELLO world"
assert to_alternating_case("HeLLo WoRLD") == "hEllO wOrld"
assert to_alternating_case("12345") == "12345"
assert to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E"
assert to_alternating_case("String.prototype.toAlternatingCase") == "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

print("All tests passed!") #if no assertion error occurs.



def first_non_consecutive(arr):
    """
    Finds the first non-consecutive number in an array.

    Args:
        arr (list): A list of unique, ascending numbers.

    Returns:
        int or None: The first non-consecutive number, or None if the array is consecutive.
    """
    if len(arr) < 2:
        return None  # Handle empty or single-element arrays (as requested in the note)

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]

    return None



def correct(s):
    """
    Corrects common character recognition errors in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The corrected string.
    """
    corrected_string = ""
    for char in s:
        if char == '5':
            corrected_string += 'S'
        elif char == '0':
            corrected_string += 'O'
        elif char == '1':
            corrected_string += 'I'
        else:
            corrected_string += char
    return corrected_string

# Example Usage and Tests (using assert for simplicity)
assert correct("L0ND0N") == "LONDON"
assert correct("DUBL1N") == "DUBLIN"
assert correct("51NGAP0RE") == "SINGAPORE"
assert correct("BUDAPE5T") == "BUDAPEST"
assert correct("PAR15") == "PARIS"

print("All tests passed!") #if no assertion error occurs.

