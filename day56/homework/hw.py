def solution(text, ending):
    """
    Checks if the given text ends with the specified ending string.

    Args:
        text: The main string to check.
        ending: The substring to check if the text ends with.

    Returns:
        True if the text ends with the ending, False otherwise.
    """
    return text.endswith(ending)



def even_or_odd(s):
    even_sum = 0
    odd_sum = 0
    for digit in s:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
    


    def vowel_indices(word):
    vowels = "aeiouAEIOU"
    indices = []
    for i, char in enumerate(word):
        if char in vowels:
            indices.append(i + 1)
    return indices