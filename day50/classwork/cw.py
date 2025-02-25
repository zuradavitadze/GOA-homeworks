import codewars_test as test

def is_isogram(string):
    return len(set(string.lower())) == len(string)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_isogram("Dermatoglyphics"), True)
        test.assert_equals(is_isogram("isogram"), True)
        test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent")
        test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case")
        test.assert_equals(is_isogram("isIsogram"), False)
        test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram")



        import codewars_test as test

def accum(s):
    result = []
    for i, char in enumerate(s):
        result.append(char.upper() + char.lower() * i)
    return "-".join(result)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        test.assert_equals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        test.assert_equals(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
        test.assert_equals(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
        test.assert_equals(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
