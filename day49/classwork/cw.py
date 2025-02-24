<!DOCTYPE html>
<html>
<head>
<title>Orange Square</title>
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  background-color: #f0f0f0; /* Light grey background */
}

.container {
  width: 300px;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #e0e0e0; /* Slightly darker grey container */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2); /* Soft shadow */
}

.orange-square {
  width: 200px;
  height: 200px;
  background-color: #dd6b4d; /* Original orange color */
  border-radius: 5px; /* Slightly rounded corners for the square */
  animation: pulse 2s infinite ease-in-out; /* Add a subtle pulse animation */
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
</style>
</head>
<body>
<div class="container">
  <div class="orange-square"></div>
</div>
</body>
</html>