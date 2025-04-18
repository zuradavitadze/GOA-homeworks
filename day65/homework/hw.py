<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Flexbox განლაგება</title>
    <style>
        /* გლობალური სტილები */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .container {
            display: flex; /* ჩართავს flexbox-ს */
            justify-content: space-between; /* ბლოკებს შორის თანაბარი მანძილი */
            align-items: center; /* ბლოკების ვერტიკალური ცენტრირება */
            padding: 20px;
            background-color: #f0f0f0;
            flex-wrap: wrap; /* გადააქვს ბლოკები ახალ ხაზზე, თუ არ ეტევა */
            gap: 20px; /* добавляет отступ между элементами */
        }

        .block {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            flex: 1; /* ბლოკები იკავებენ თანაბარ ადგილს */
            min-width: 200px; /* ბლოკის მინიმალური სიგანე */
        }

        /* სტილები მცირე ეკრანებისთვის (მაგალითად, ტელეფონებისთვის) */
        @media screen and (max-width: 600px) {
            .container {
                flex-direction: column; /* ბლოკები განლაგდებიან ვერტიკალურად */
                align-items: stretch; /* ბლოკები იჭიმებიან მთელ სიგანეზე */
            }
            .block {
                min-width: auto; /* შლის მინიმალურ სიგანეს, რომ გაიჭიმოს */
            }
        }
        /* სტილები საშუალო ეკრანებისთვის (მაგალითად, ტაბლეტებისთვის) */
        @media screen and (min-width: 601px) and (max-width: 900px) {
            .container{
                flex-direction: column;
                align-items: stretch;
            }
            .block{
               min-width: auto;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="block">ბლოკი 1</div>
        <div class="block">ბლოკი 2</div>
        <div class="block">ბლოკი 3</div>
    </div>
</body>
</html>




<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>4-სვეტიანი Grid განლაგება</title>
    <style>
      .container {
        display: grid;
        /* ოთხი სვეტი დესკტოპზე */
        grid-template-columns: repeat(4, 1fr);
        gap: 10px; /* სვეტებს შორის მანძილი */
        padding: 20px;
      }

      .item {
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 8px;
      }

      /* მობილური მოწყობილობებისთვის (მაქსიმალური სიგანე 600px) */
      @media screen and (max-width: 600px) {
        .container {
          /* ერთი სვეტი მობილურზე */
          grid-template-columns: 1fr;
        }
      }
    </style>
</head>
<body>
    <div class="container">
      <div class="item">1</div>
      <div class="item">2</div>
      <div class="item">3</div>
      <div class="item">4</div>
      <div class="item">5</div>
      <div class="item">6</div>
      <div class="item">7</div>
      <div class="item">8</div>
    </div>
</body>
</html>
