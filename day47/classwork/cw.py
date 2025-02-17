<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Grid</title>
    <style>
        .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 80%;
            height: 300px;
            border: 2px solid black;
            margin: 20px auto;
            padding: 10px;
        }
        
        .column {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }

        .box {
            width: 50px;
            height: 50px;
            border: 2px solid cyan;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="column">
            <div class="box"></div>
            <div class="box"></div>
        </div>
        <div class="column">
            <div class="box"></div>
            <div class="box"></div>
            <div class="box"></div>
        </div>
        <div class="column">
            <div class="box"></div>
            <div class="box"></div>
            <div class="box"></div>
        </div>
    </div>
</body>
</html>
