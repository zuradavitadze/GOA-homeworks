<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Layout</title>
    <style>
        .container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 80%;
            margin: auto;
        }

        .row {
            display: flex;
            background-color: blue;
            padding: 10px;
            gap: 5px;
        }

        .box {
            width: 50px;
            height: 50px;
            background-color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
        }

        .special {
            flex-direction: column;
            display: flex;
            gap: 5px;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- First layout -->
        <div class="row">
            <div class="special">
                <div class="box">9</div>
            </div>
            <div class="row">
                <div class="box">1</div>
                <div class="box">2</div>
                <div class="box">3</div>
                <div class="box">4</div>
                <div class="box">5</div>
                <div class="box">6</div>
                <div class="box">7</div>
                <div class="box">8</div>
            </div>
        </div>

        <!-- Second layout -->
        <div class="row">
            <div class="special">
                <div class="box">9</div>
            </div>
            <div class="row">
                <div class="box">1</div>
                <div class="box">2</div>
                <div class="box">3</div>
                <div class="box">4</div>
                <div class="box">5</div>
                <div class="box">6</div>
                <div class="box">7</div>
                <div class="box">8</div>
            </div>
        </div>
    </div>

</body>
</html>
