<!DOCTYPE html>
<html>
<head>
    <title>მომხმარებლის რეგისტრაცია</title>
</head>
<body>
    <form>
        <label for="fname">სახელი:</label><br>
        <input type="text" id="fname" name="fname"><br>
        <label for="lname">გვარი:</label><br>
        <input type="text" id="lname" name="lname"><br>
        <label for="age">ასაკი:</label><br>
        <input type="number" id="age" name="age"><br>
        <p>სქესი:</p>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">მამაკაცი</label><br>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">ქალი</label><br>
        <p>პირობებს ვეთანხმები:</p>
        <input type="checkbox" id="terms" name="terms" required>
        <label for="terms">პირობების მიღება</label><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>


<!DOCTYPE html>
<html>
<head>
    <title>Dropdown მენიუ</title>
</head>
<body>
    <label for="interests">აირჩიეთ თქვენი ინტერესები:</label>
    <select name="interests" id="interests">
        <option value="films">ფილმები</option>
        <option value="books">წიგნები</option>
        <option value="music">მუსიკა</option>
        <option value="sports">სპორტი</option>
        <option value="food">საჭმელი</option>
        <option value="travel">მოგზაურობა</option>
    </select>
</body>
</html>
