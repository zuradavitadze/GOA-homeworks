# ვქმნით tuple-ს 6 საყვარელი ფილმით
my_favorite_movies = (
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King"
)

# tuple unpacking: პირველი ფილმი ცალკე, დანარჩენი - სიაში
first_movie, *remaining_movies = my_favorite_movies

# შედეგის გამოტანა
print(f"ჩემი პირველი საყვარელი ფილმია: {first_movie}")
print(f"დანარჩენი ჩემი საყვარელი ფილმებია: {remaining_movies}")

# სიაში არსებული ფილმების ცალ-ცალკე გამოტანა ციკლის გამოყენებით
print("დანარჩენი ფილმები ციკლით:")
for movie in remaining_movies:
    print(movie)