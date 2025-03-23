<!DOCTYPE html>
<html>
<head>
<title>Frontend Mentor | Article Preview Component</title>
<style>
  body {
    font-family: sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
  }

  .container {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    max-width: 800px;
    display: flex;
    flex-direction: row;
    margin: 20px;
  }

  .image-container {
    flex: 1;
  }

  .image-container img {
    display: block;
    width: 100%;
    height: auto;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
  }

  .content-container {
    flex: 1;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .article-info {
    margin-bottom: 20px;
  }

  .article-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
    line-height: 1.2;
  }

  .article-summary {
    color: #777;
    line-height: 1.6;
  }

  .share-info {
    display: flex;
    align-items: center;
  }

  .author-info {
    display: flex;
    align-items: center;
    margin-right: auto;
  }

  .author-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .author-name {
    font-size: 0.9rem;
    font-weight: bold;
    color: #333;
    margin-bottom: 3px;
  }

  .publish-date {
    font-size: 0.8rem;
    color: #777;
  }

  .share-button {
    background-color: #e6e6e6;
    color: #999;
    border: none;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    font-size: 1rem;
  }

  .share-button:hover {
    background-color: #d3d3d3;
  }

  /* You would add more styling for the share icons and the active share state here */

  /* Responsive Design */
  @media (max-width: 768px) {
    .container {
      flex-direction: column;
      margin: 15px;
    }

    .image-container img {
      border-top-left-radius: 10px;
      border-top-right-radius: 10px;
      border-bottom-left-radius: 0;
    }
  }
</style>
</head>
<body>
  <div class="container">
    <div class="image-container">
      <img src="https://via.placeholder.com/400x300/abcdef/ffffff?Text=Article%20Image" alt="Article Preview">
    </div>
    <div class="content-container">
      <div class="article-info">
        <h2 class="article-title">Shift the overall look and feel by adding these wonderful touches to furniture in your home</h2>
        <p class="article-summary">Ever been in a room and felt like something was missing? Perhaps it felt slightly bare and uninviting. I’ve got some simple tips to help you make any room feel complete.</p>
      </div>
      <div class="share-info">
        <div class="author-info">
          <img src="https://via.placeholder.com/40x40/999999/ffffff?Text=Avatar" alt="Author Avatar" class="author-avatar">
          <div>
            <div class="author-name">Michelle Appleton</div>
            <div class="publish-date">28 Jun 2020</div>
          </div>
        </div>
        <button class="share-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13"><path fill="#6E8098" d="M15 6.495L8.753.007 0 7.393l6.247 5.607 8.753-6.502z"/></svg>
        </button>
        </div>
    </div>
  </div>
</body>
</html>