def count_arara(n):
    adak_count = n // 2
    anane_count = n % 2
    result = ""
    if adak_count > 0:
        result += "adak " * adak_count
    if anane_count > 0:
        result += "anane"
    return result.strip()


def is_planet_mnemonic_correct(planets, mnemonic):
    if not planets and not mnemonic:
        return True
    if not planets:
        return False
    
    planet_first_letters = [planet[0] for planet in planets if planet[0].isalpha()]
    mnemonic_words = mnemonic.split()
    mnemonic_first_letters = [word[0] for word in mnemonic_words if word[0].isalpha()]
    
    return planet_first_letters == mnemonic_first_letters



def max_possible_score(obj, arr):
    """
    Calculates the maximum possible score based on the given object and array.

    Args:
        obj (dict): A dictionary where keys are strings and values are integers.
        arr (list): A list of strings.

    Returns:
        int: The maximum possible score.
    """
    total_score = sum(obj.values())
    bonus_score = sum(obj[key] for key in arr if key in obj)
    return total_score + bonus_score