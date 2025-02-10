<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layout Recreation</title>
    <style>
        body {
            width: 400px; /* Adjust as needed */
            height: 300px; /* Adjust as needed */
            border: 1px solid black;
            position: relative; /* For positioning children */
        }

        #div1 {
            width: 150px; /* Adjust as needed */
            height: 150px; /* Adjust as needed */
            border: 1px solid green;
            position: absolute;
            top: 20px;
            left: 20px;
        }

        .nested-rect {
            width: 70px; /* Adjust as needed */
            height: 50px; /* Adjust as needed */
            border: 1px solid black;
            position: absolute; /* To allow overlapping */
        }

        #rect1 {
            top: 20px;
            left: 10px;
        }

        #rect2 {
            top: 40px;
            left: 30px;
        }

        #level {
            position: absolute;
            top: 10px;
            left: 20px;
        }

        #note {
            position: absolute;
            bottom: 10px;
            left: 20px;
        }

        /* Styling for the "from" line */
        #from-line {
            position: absolute;
            top: 10px;
            left: 60px; /* Adjust as needed */
            width: 250px; /* Adjust as needed */
            height: 1px;
            background-color: black;
        }

        /* Styling for the arrows on the "from" line */
        .arrow {
            position: absolute;
            border-style: solid;
            font-size: 0; /* Make the arrow from border */
        }

        .arrow-left {
            left: -5px; /* Adjust as needed */
            top: -5px; /* Adjust as needed */
            border-width: 5px 5px 5px 0; /* Adjust as needed */
            border-color: transparent black transparent transparent; /* Adjust as needed */
        }

        .arrow-right {
            right: -5px; /* Adjust as needed */
            top: -5px; /* Adjust as needed */
            border-width: 5px 0 5px 5px; /* Adjust as needed */
            border-color: transparent transparent transparent black; /* Adjust as needed */
        }
    </style>
</head>
<body>

    <div id="level">level 45:</div>
    <div id="from-line">
        <div class="arrow arrow-left"></div>
        <div class="arrow arrow-right"></div>
    </div>

    <div id="div1">
        <div class="nested-rect" id="rect1"></div>
        <div class="nested-rect" id="rect2"></div>
    </div>

    <div id="note">Remember the current location is Batumi, Adjara, Georgia.</div>

</body>
</html>