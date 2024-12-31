<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rounded Box</title>
    <style>
        body {
            display: flex;
            justify-content: center; /* ჰორიზონტალურად ცენტრირება */
            align-items: center;     /* ვერტიკალურად ცენტრირება */
            min-height: 100vh;      /* ეკრანის სრული სიმაღლის გამოყენება */
            margin: 0;             /* ნაგულისხმევი margin-ების მოშორება */
            background-color: #f0f0f0; /* ფონი უკეთესი ვიზუალური ეფექტისთვის */
        }

        .box {
            width: 200px;
            height: 100px;
            background-color: #4CAF50; /* მწვანე ფონი */
            border-radius: 50% 50% 0 0; /* ზედა კუთხეების დამრგვალება */
            /* თუ გინდათ border-ი დაამატეთ ეს ხაზი */
            /* border: 2px solid black; */
            box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>