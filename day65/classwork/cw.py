<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Grid ვებსაიტი</title>
    <style>
        /* გლობალური სტილები */
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .container {
            padding: 20px;
            /* 10 სვეტი დიდ ეკრანზე */
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 10px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .item {
            background-color: #f0f0f0;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            text-align: center;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        /* მედია მოთხოვნა ტელეფონებისთვის */
        @media (max-width: 768px) {
            .container {
                /* 1 სვეტი ტელეფონზე */
                grid-template-columns: 1fr;
                gap: 15px; /* გაზრდილი ინტერვალი უკეთესი ვიზუალისთვის */
            }
            .item:nth-child(3) {
                order: -1; /* მე-3 ელემენტი პირველია ტელეფონებზე */
            }
            .item {
                padding: 15px; /* ოდნავ მეტი padding ტელეფონებზე */
            }
        }
        /* მედია მოთხოვნა ტაბლეტებისთვის */
        @media (min-width: 769px) and (max-width: 1200px) {
            .container {
                /* 4 სვეტი ტაბლეტზე */
                grid-template-columns: repeat(4, 1fr);
                gap: 12px; /* ოდნავ შეცვლილი ინტერვალი ტაბლეტებზე */
            }
            .item {
                padding: 18px; /* მცირე padding ტაბლეტებზე */
            }
        }
        /* დამატებითი სტილები */
        .container {
            background-color: #e0e0e0;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .item {
            background-color: #fff;
            transition: transform 0.3s ease;
        }
        .item:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <h1>ჩემი Responsive Grid გვერდი</h1>
    <div class="container">
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
        <div class="item">4</div>
        <div class="item">5</div>
        <div class="item">6</div>
        <div class="item">7</div>
        <div class="item">8</div>
        <div class="item">9</div>
        <div class="item">10</div>
    </div>
</body>
</html>