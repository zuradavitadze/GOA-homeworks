<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frontend Mentor Challenge</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            background-color: #f2f2f7; /* Light grey background */
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header-steps {
            display: flex;
            justify-content: center;
            width: 100%;
            padding: 20px 0;
            background-color: white;
            border-bottom: 1px solid #e0e0e0;
        }

        .step {
            color: #868e96; /* Grey text */
            margin: 0 20px;
            cursor: pointer;
        }

        .step.active {
            color: #212529; /* Dark text for active step */
            font-weight: bold;
        }

        .challenge-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            padding: 30px;
            width: 80%;
            max-width: 960px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        .badges {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        .badge {
            background-color: #e9ecef; /* Light grey badge */
            color: #495057; /* Dark grey text */
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.8em;
        }

        .badge.free {
            background-color: #d3f8e2; /* Light green */
            color: #38b000; /* Green */
        }

        .badge.newbie {
            background-color: #ffe0b2; /* Light orange */
            color: #f57c00; /* Orange */
        }

        .challenge-title {
            font-size: 2em;
            color: #212529;
            margin-bottom: 10px;
        }

        .challenge-description {
            color: #495057;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .start-button {
            background-color: #e63946; /* Red button */
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 1em;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-bottom: 20px;
        }

        .start-button:hover {
            background-color: #c21807; /* Darker red */
        }

        .community-info {
            display: flex;
            align-items: center;
            color: #495057;
            font-size: 0.9em;
        }

        .community-icon {
            width: 24px;
            height: 24px;
            margin-right: 10px;
            /* You might need to use an actual icon here, e.g., an SVG or font icon */
            background-color: #adb5bd; /* Placeholder for icon background */
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .preview-image {
            margin-top: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
            max-width: 100%; /* Make image responsive */
            height: auto;
        }
    </style>
</head>
<body>
    <div class="header-steps">
        <div class="step active">STEP 1<br>Start challenge</div>
        <div class="step">STEP 2<br>Download assets</div>
        <div class="step">STEP 3<br>Submit solution</div>
        <div class="step">STEP 4<br>Review solutions</div>
    </div>

    <div class="challenge-container">
        <div class="badges">
            <span class="badge free">FREE</span>
            <span class="badge">HTML</span>
            <span class="badge">CSS</span>
            <span class="badge newbie">1 NEWBIE</span>
        </div>
        <h1 class="challenge-title">Order summary component</h1>
        <p class="challenge-description">A perfect project for newbies who are starting to build confidence with layouts!</p>
        <button class="start-button">START CHALLENGE</button>
        <div class="community-info">
            <div class="community