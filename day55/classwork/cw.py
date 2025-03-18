<!DOCTYPE html>
<html>
<head>
<title>Design Replication</title>
<style>
body {
    font-family: sans-serif;
    background-color: #36393f;
    color: #dcddde;
    padding: 20px;
}

.container {
    margin-bottom: 20px;
}

.header {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: #5865f2; /* Placeholder for avatar */
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    margin-right: 10px;
}

.username-time {
    font-size: 0.9em;
    color: #b9bbbe;
}

.level {
    font-weight: bold;
    margin-bottom: 5px;
}

.instruction {
    margin-bottom: 10px;
}

.edited {
    font-size: 0.8em;
    color: #7289da;
    margin-left: 5px;
}

.design-1 {
    background-color: #5865f2;
    padding: 10px;
    border-radius: 5px;
    display: flex;
    gap: 10px;
    align-items: center;
}

.design-1-item {
    background-color: white;
    color: black;
    width: 50px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 3px;
}

.design-2 {
    background-color: #5865f2;
    padding: 10px;
    border-radius: 5px;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: flex-start;
}

.design-2-item {
    background-color: white;
    color: black;
    width: 30px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 3px;
    margin-bottom: 10px; /* Add margin for the wrap */
}

.design-2-item.item-9 {
    width: 30px;
    height: 70px;
}
</style>
</head>
<body>

    <div class="container">
        <div class="header">
            <div class="avatar">B</div>
            <div class="username-time">
                <div>საჯარო აზრის ექსპერტი</div>
                <div>3/13/2025 7:04 PM</div>
            </div>
        </div>
        <div class="level">level 55:</div>
        <div class="instruction">
            1) შექმენით მსგავსი დიზაინი <span class="edited">(edited)</span>
        </div>
        <div class="design-1">
            <div class="design-1-item">1</div>
            <div class="design-1-item">2</div>
            <div class="design-1-item">3</div>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <div class="avatar">B</div>
            <div class="username-time">
                <div>საჯარო აზრის ექსპერტი</div>
                <div>3/13/2025 8:47 PM</div>
            </div>
        </div>
        <div class="instruction">
            2)შექმენით მსგავსი დიზაინი
        </div>
        <div class="design-2">
            <div class="design-2-item">1</div>
            <div class="design-2-item">2</div>
            <div class="design-2-item">3</div>
            <div class="design-2-item">4</div>
            <div class="design-2-item">5</div>
            <div class="design-2-item">6</div>
            <div class="design-2-item">7</div>
            <div class="design-2-item">8</div>
            <div class="design-2-item item-9">9</div>
        </div>
    </div>

</body>
</html>