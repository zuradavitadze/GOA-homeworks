<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ანიმაციური ბარათები</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="card card-fade-in">
            <h2>Fade In</h2>
            <p>ეს ბარათი ნელ-ნელა ჩნდება.</p>
        </div>

        <div class="card card-slide-up">
            <h2>Slide Up</h2>
            <p>ეს ბარათი ქვემოდან ზემოთ სრიალებს.</p>
        </div>

        <div class="card card-zoom-out">
            <h2>Zoom Out</h2>
            <p>ეს ბარათი თავიდან დიდია და მცირდება.</p>
        </div>

        <div class="card card-color-change">
            <h2>ფერისა და ზომის ცვლილება</h2>
            <p>ეს ბარათი იცვლის ფერს და ზომას.</p>
        </div>

        <div class="text-animation">
            <h2 class="color-change-text">ფერადი ტექსტი</h2>
        </div>

        <div class="card card-bounce">
            <h2>Bounce</h2>
            <p>ეს ბარათი ხტუნავს.</p>
        </div>

        <div class="card card-my-animation">
            <h2>ჩემი ანიმაცია</h2>
            <p>ეს ჩემი განსაკუთრებული ანიმაციაა!</p>
        </div>
    </div>
</body>
</html>



body {
    font-family: sans-serif;
    margin: 0;
    background-color: #f4f4f4;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    gap: 30px;
    padding: 30px;
}

.card {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    width: 250px;
    padding: 20px;
    text-align: center;
}

.card h2 {
    margin-top: 0;
}

/* 1. Fade In ანიმაცია */
.card-fade-in {
    opacity: 0;
    animation: fadeIn 1s ease-in-out forwards;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* 2. Slide Up ანიმაცია */
.card-slide-up {
    transform: translateY(50px);
    opacity: 0;
    animation: slideUp 1s ease-out forwards;
}

@keyframes slideUp {
    from { transform: translateY(50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

/* 3. Zoom Out ანიმაცია */
.card-zoom-out {
    transform: scale(1.2);
    opacity: 0;
    animation: zoomOut 1s ease-in forwards;
}

@keyframes zoomOut {
    from { transform: scale(1.2); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

/* 4. ფერისა და ზომის ცვლილების ანიმაცია */
.card-color-change {
    animation: colorSizeChange 2s infinite alternate;
}

@keyframes colorSizeChange {
    0% {
        background-color: #f0f8ff; /* AliceBlue */
        transform: scale(1);
    }
    50% {
        background-color: #add8e6; /* LightBlue */
        transform: scale(1.05);
    }
    100% {
        background-color: #87ceeb; /* SkyBlue */
        transform: scale(1);
    }
}

/* 5. ფერის შეცვლის ანიმაცია ტექსტზე */
.text-animation {
    text-align: center;
}

.color-change-text {
    animation: textColorChange 3s infinite alternate;
}

@keyframes textColorChange {
    0% { color: #ff69b4; /* HotPink */ }
    50% { color: #ba55d3; /* MediumOrchid */ }
    100% { color: #4682b4; /* SteelBlue */ }
}

/* 6. Bounce ანიმაცია */
.card-bounce {
    animation: bounce 1s infinite alternate;
}

@keyframes bounce {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
}

/* 7. ჩემი სასურველი ანიმაცია - ბრუნვა და ფერის შეცვლა */
.card-my-animation {
    animation: rotateColor 2s infinite linear;
}

@keyframes rotateColor {
    0% {
        transform: rotate(0deg);
        background-color: #ffd700; /* Gold */
    }
    50% {
        background-color: #ffa07a; /* LightSalmon */
    }
    100% {
        transform: rotate(360deg);
        background-color: #fa8072; /* Salmon */
    }
}