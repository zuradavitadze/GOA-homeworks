<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Social Links Profile</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #121212;
            font-family: Arial, sans-serif;
            color: #fff;
        }
        .profile-card {
            background: #1f1f1f;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 300px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
        }
        .profile-card img {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            object-fit: cover;
        }
        .profile-card h1, .profile-card p {
            margin: 10px 0;
        }
        .links a {
            display: block;
            background: #333;
            color: #fff;
            text-decoration: none;
            margin: 8px 0;
            padding: 10px;
            border-radius: 5px;
            transition: background 0.2s;
        }
        .links a:hover {
            background: #555;
        }
    </style>
</head>
<body>
    <div class="profile-card">
        <img src="https://via.placeholder.com/100" alt="Profile Picture">
        <h1>Jessica Randall</h1>
        <p>London, United Kingdom</p>
        <p>"Front-end developer and avid reader"</p>
        <div class="links">
            <a href="#">GitHub</a>
            <a href="#">Frontend Mentor</a>
            <a href="#">LinkedIn</a>
            <a href="#">Twitter</a>
            <a href="#">Instagram</a>
        </div>
    </div>
</body>
</html>
