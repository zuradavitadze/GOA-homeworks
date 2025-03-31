<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Time tracking dashboard</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 20px;
            display: flex;
            gap: 40px;
        }

        .left-section {
            max-width: 500px;
        }

        .free-badges {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
        }

        .free-badges span {
            background-color: #f0f0f0;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.9em;
        }

        .junior-badge {
            background-color: #a0d468;
            color: white;
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 15px;
        }

        .description {
            color: #555;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .start-challenge-button {
            background-color: #e74c3c;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 30px;
            font-size: 1.1em;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .start-challenge-button:hover {
            background-color: #c0392b;
        }

        .join-count {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #3498db;
            font-weight: bold;
        }

        .join-count svg {
            width: 20px;
            height: 20px;
            fill: #3498db;
        }

        .right-section {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            max-width: 600px;
        }

        .dashboard-card {
            background-color: #34495e;
            color: white;
            border-radius: 10px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 150px; /* Approximate height */
        }

        .profile-card {
            background-color: #5c6bc0;
            height: auto;
        }

        .profile-info {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }

        .profile-image {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #7986cb; /* Placeholder */
        }

        .profile-name {
            font-size: 1.2em;
            font-weight: bold;
        }

        .time-period {
            color: #9fa8da;
        }

        .activity-info {
            text-align: right;
        }

        .current-time {
            font-size: 1.8em;
            font-weight: bold;
        }

        .previous-time {
            color: #9fa8da;
            font-size: 0.9em;
        }

        .activity-icon {
            text-align: right;
            margin-bottom: 10px;
        }

        .activity-icon img {
            width: 40px; /* Approximate size */
            height: 40px;
            opacity: 0.8;
        }

        .work-card { background-color: #ff8a65; }
        .play-card { background-color: #5c6bc0; }
        .study-card { background-color: #9ccc65; }
        .exercise-card { background-color: #4dd0e1; }
        .social-card { background-color: #ba68c8; }
        .self-care-card { background-color: #fdd835; }

        .design-toggles {
            margin-top: 20px;
        }

        .design-toggles button {
            padding: 10px 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            cursor: pointer;
            background-color: white;
            color: #333;
        }

        .design-toggles button.active {
            background-color: #3498db;
            color: white;
            border-color: #3498db;
        }
    </style>
</head>
<body>
    <div class="left-section">
        <div class="free-badges">
            <span>FREE</span>
            <span>HTML</span>
            <span>CSS</span>
            <span>JS</span>
            <span class="junior-badge">2 JUNIOR</span>
        </div>
        <h1>Time tracking dashboard</h1>
        <p class="description">A perfect opportunity to practice your CSS Grid skills. For anyone wanting to take it up a notch, we provide a JSON data file to practice working with data.</p>
        <button class="start-challenge-button">START CHALLENGE</button>
        <div class="join-count">
            <svg viewBox="0 0 24 24">
                <path fill="currentColor" d="M12 4a4 4 0 0 1 4 4 4 4 0 0 1-4 4 4 4 0 0 1-4-4 4 4 0 0 1 4-4m0 10c4.42 0 8 1.79 8 4v2H4v-2c0-2.21 3.58-4 8-4m0-12a2 2 0 0 0-2 2 2 2 0 0 0 2 2 2 2 0 0 0 2-2 2 2 0 0 0-2-2m0 10c-2.21 0-4-1.79-4-4v2h8v-2c0 2.21-3.58 4-8 4"/>
            </svg>
            Join 31,691 people who have taken this challenge
        </div>
    </div>

    <div class="right-section">
        <div class="dashboard-card profile-card">
            <div class="profile-info">
                <div class="profile-image"></div>
                <div>
                    <p class="time-period">Daily</p>
                    <p class="profile-name">Jeremy Robson</p>
                </div>
            </div>
            <div>
                <p class="time-period">Weekly</p>
                <p class="time-period">Monthly</p>
            </div>
        </div>

        <div class="dashboard-card work-card">
            <div class="activity-icon"><img src="images/icon-work.svg" alt="Work"></div>
            <div>
                <p>Work</p>
                <p class="current-time">32hrs</p>
                <p class="previous-time">Last Week - 36hrs</p>
            </div>
        </div>

        <div class="dashboard-card play-card">
            <div class="activity-icon"><img src="images/icon-play.svg" alt="Play"></div>
            <div>
                <p>Play</p>
                <p class="current-time">10hrs</p>
                <p class="previous-time">Last Week - 8hrs</p>
            </div>
        </div>

        <div class="dashboard-card study-card">
            <div class="activity-icon"><img src="images/icon-study.svg" alt="Study"></div>
            <div>
                <p>Study</p>
                <p class="current-time">4hrs</p>
                <p class="previous-time">Last Week - 7hrs</p>
            </div>
        </div>

        <div class="dashboard-card exercise-card">
            <div class="activity-icon"><img src="images/icon-exercise.svg" alt="Exercise"></div>
            <div>
                <p>Exercise</p>
                <p class="current-time">4hrs</p>
                <p class="previous-time">Last Week - 5hrs</p>
            </div>
        </div>

        <div class="dashboard-card social-card">
            <div class="activity-icon"><img src="images/icon-social.svg" alt="Social"></div>
            <div>
                <p>Social</p>
                <p class="current-time">5hrs</p>
                <p class="previous-time">Last Week - 10hrs</p>
            </div>
        </div>

        <div class="dashboard-card self-care-card">
            <div class="activity-icon"><img src="images/icon-self-care.svg" alt="Self Care"></div>
            <div>
                <p>Self Care</p>
                <p class="current-time">2hrs</p>
                <p class="previous-time">Last Week - 2hrs</p>
            </div>
        </div>
    </div>

    <div class="design-toggles">
        <button class="active">DESKTOP DESIGN</button>
        <button>MOBILE DESIGN</button>
    </div>

    </body>
</html>