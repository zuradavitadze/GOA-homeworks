<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stats Preview Card Component Challenge</title>
    <style>
        body {
            font-family: sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f0f0; /* Light background */
        }

        .main-container {
            display: flex;
            width: 80%; /* Adjust as needed */
            max-width: 1200px; /* Optional max width */
            background-color: white; /* White container */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden; /* Hide overflow from image */
        }

        .left-content {
            flex: 1;
            padding: 20px;
        }

        .right-content {
            flex: 1;
            background-color: purple; /* Placeholder for image area */
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .tags {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .tag {
            background-color: #e0e0e0;
            padding: 5px 10px;
            border-radius: 15px;
            margin-right: 5px;
            font-size: 0.8em;
        }

        .newbie-tag {
            background-color: #b0e0e6; /* Light blue */
        }

        .description {
            margin-bottom: 20px;
        }

        .status {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }

        .status img {
            width: 20px;
            margin-right: 10px;
        }

        .submit-button {
            background-color: #4a90e2; /* Blue */
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }

        .design-tabs {
            text-align: right;
            margin-top: 20px;
        }

        .design-tab {
            background-color: #f0f0f0;
            padding: 5px 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-left: 5px;
            cursor: pointer;
        }

        .design-tab.active {
            background-color: #ddd;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="left-content">
            <div class="tags">
                <span class="tag">FREE</span>
                <span class="tag">HTML</span>
                <span class="tag">CSS</span>
                <span class="tag newbie-tag">1 NEWBIE</span>
            </div>
            <h2>Stats preview card component</h2>
            <p class="description">This is a great small challenge to help get you used to building to a design. There's no JS in this project, so you'll be able to focus on your HTML & CSS skills.</p>
            <div class="status">
                <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACYSURBVDhPY/hPAz