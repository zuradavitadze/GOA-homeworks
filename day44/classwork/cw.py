def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
print(count_by(2, 5))  # [2, 4, 6, 8, 10]
print(count_by(3, 4))  # [3, 6, 9, 12]


def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
        return [human_years, cat_years, dog_years]
print(human_years_cat_years_dog_years(1))  # [1, 15, 15]
print(human_years_cat_years_dog_years(2))  # [2, 24, 24]
print(human_years_cat_years_dog_years(5))  # [5, 36, 39]
