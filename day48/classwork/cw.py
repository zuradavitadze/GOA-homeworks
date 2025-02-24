def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


def find_short(s):
    return min(len(word) for word in s.split())


def solution(text, ending):
    return text.endswith(ending)


def accum(s):
    result = []
    for i, char in enumerate(s):
        result.append(char.upper() + char.lower() * i)
    return '-'.join(result)