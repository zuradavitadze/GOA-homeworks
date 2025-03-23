<!DOCTYPE html>
<html>
<head>
<title>Grid Garden Level 57</title>
<style>
  body {
    font-family: sans-serif;
    background-color: #f4f4f4;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .container {
    background-color: #d3eadd;
    border: 1px solid #a8c9a7;
    padding: 20px;
    margin-top: 20px;
    border-radius: 5px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
    color: #333;
  }

  .timestamp {
    font-size: 0.8em;
    color: #777;
  }

  .level {
    font-weight: bold;
    font-size: 1.1em;
    margin-bottom: 5px;
  }

  .instruction {
    margin-bottom: 10px;
  }

  .codepip-bar {
    background-color: #5cb85c;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }

  .codepip-logo {
    font-weight: bold;
    margin-right: 15px;
  }

  .codepip-links a {
    color: white;
    text-decoration: none;
    margin-right: 10px;
  }

  .codepip-links a:hover {
    text-decoration: underline;
  }

  .upgrade-button {
    background-color: #f0ad4e;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 0.9em;
    margin-left: auto;
  }

  .grid-garden-container {
    background-color: #a0d468;
    border: 1px solid #8ac926;
    padding: 10px;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 15px;
  }

  .grid-description {
    color: #333;
    font-size: 0.9em;
    margin-bottom: 10px;
    text-align: center;
  }

  .grid-controls {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .grid-controls label {
    margin-right: 5px;
    font-size: 0.9em;
  }

  .grid-controls select {
    padding: 5px;
    border-radius: 3px;
    border: 1px solid #ccc;
    font-size: 0.9em;
  }

  .grid-area {
    display: grid;
    grid-template-columns: repeat(6, 40px);
    grid-template-rows: repeat(6, 40px);
    gap: 2px;
    background-color: #79a702;
    padding: 5px;
    border-radius: 3px;
  }

  .grid-cell {
    width: 40px;
    height: 40px;
    background-color: #f0f8ea; /* Default cell color */
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8em;
  }

  .carrot {
    background-color: #ffc107;
    border-radius: 5px;
    width: 20px;
    height: 20px;
  }

  .water {
    background-color: #007bff;
    border-radius: 50%;
    width: 20px;
    height: 20px;
  }

  .code-editor {
    background-color: #282c34;
    color: #abb2bf;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 15px;
    font-family: monospace;
    font-size: 0.9em;
    overflow: auto;
    max-height: 300px;
    width: 90%;
  }

  .code-line {
    white-space: pre;
    line-height: 1.2;
  }

  .comment {
    color: #6a9955;
  }

  .property {
    color: #c678dd;
  }

  .value {
    color: #e06c75;
  }

  .selector {
    color: #61aeee;
  }

  .next-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
  }

  .user-message {
    background-color: #e9ecef;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    width: 80%;
    align-self: flex-start;
  }

  .user-info {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
  }

  .avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .username {
    font-weight: bold;
    margin-right: 5px;
  }

  .message-content {
    font-size: 0.95em;
    color: #333;
  }
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div>
        <div class="level">level 57:</div>
        <div class="instruction">1) გავაკეთ მე -3 (edited)</div>
      </div>
      <div class="timestamp">3/20/2025 8:30 PM</div>
    </div>

    <div class="codepip-bar">
      <span class="codepip-logo">codepip</span>
      <div class="codepip-links">
        <a href="#">Games</a>
        <a href="#">Plans</a>
        <a href="#">Blog</a>
      </div>
      <button class="upgrade-button">Upgrade</button>
      <span>grdzulo-</span>
    </div>

    <div class="grid-garden-container">
      <h2>GRID GARDEN</h2>
      <p class="grid-description">Move the water drops to water all your carrots!</p>
      <div class="grid-controls">
        <label for="language">Language:</label>
        <select id="language">
          <option>English</option>
        </select>
        <span>&lt;</span>
        <span>1 of 22</span>
        <span>&gt;</span>
      </div>
      <p style="font-size: 0.8em; color: #333; text-align: left;">When <code style="font-family: monospace;">grid-column-start</code> is used alone, the grid item by default will span exactly one column. However, you can extend the item across multiple columns by adding the <code style="font-family: monospace;">grid-column-end</code> property.</p>
      <p style="font-size: 0.8em; color: #333; text-align: left;">Using <code style="font-family: monospace;">grid-column-end</code>, water all of your carrots while avoiding the dirt. We don't want to waste any water! Note that the carrots start at the 1st vertical grid line and end at the 4th.</p>
      <div class="grid-area">
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"><div class="carrot"></div></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"><div class="water"></div></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"><div class="water"></div></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"><div class="water"></div></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
      </div>

      <div class="code-editor">
        <div class="code-line"><span class="comment">/* Learn CSS Grid the easy way! */</span></div>
        <div class="code-line"><span class="selector">.garden</span> {</div>
        <div class="code-line">  <span class="property">display</span>: <span class="value">grid</span>;</div>
        <div class="code-line">  <span class="property">grid-template-columns</span>: <span class="value">20% 20% 20% 20% 20% 20%</span>;</div>
        <div class="code-line">  <span class="property">grid-template-rows</span>: <span class="value">20% 20% 20% 20% 20% 20%</span>;</div>
        <div class="code-line">}</div>
        <div class="code-line"></div>
        <div class="code-line"><span class="selector">.water</span> {</div>
        <div class="code-line">  <span class="property">grid-column-start</span>: <input type="text" id="grid-column-start" style="width: 30px;">;</div>
        <div class="code-line">}</div>
        <div class="code-line"></div>
      </div>

      <button class="next-button">Next</button>
    </div>
  </div>

  <div class="container">
    <div class="user-message">
      <div class="user-info">
        <img src="https://via.placeholder.com/30" alt="User Avatar" class="avatar">
        <span class="username">ნიკოლოზ დავით ჭურაძული</span>
        <img src="https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.5.0/flags/4x3/ge.svg" alt="Georgian Flag" style="width: 20px; margin-left: 5px;">
      </div>
      <div class="message-content">2) 16 მდე გავაკეთოთ ❤️</div>
      <div class="timestamp">3/20/2025 8:52 PM</div>
    </div>
  </div>

  <script>
    // You can add JavaScript here to make the input field interactive if needed.
    // For example, to update the grid based on the input value.
    const gridColumnStartInput = document.getElementById('grid-column-start');
    const waterElements = document.querySelectorAll('.water');
    const gridArea = document.querySelector('.grid-area');
    const gridCells = document.querySelectorAll('.grid-cell');

    gridColumnStartInput.addEventListener('input', function() {
      const startValue = this.value;
      waterElements.forEach((water, index) => {
        water.style.gridColumnStart = startValue;
        // Basic logic to try and place each water in a different row
        water.style.gridRowStart = index + 4; // Assuming water starts from row 4
        water.style.gridColumnEnd = 'span 3'; // To cover 3 carrot columns as hinted
      });

      // Reset the grid to remove any previous water placements
      gridCells.forEach(cell => {
        if (cell.classList.contains('water')) {
          cell.classList.remove('water');
          cell.innerHTML = '';
        }
      });

      // Re-add the water elements based on the input
      waterElements.forEach((water, index) => {
        const newWaterDiv = document.createElement('div');
        newWaterDiv.classList.add('water');
        const rowStart = parseInt(water.style.gridRowStart) || (index + 4);
        const colStart = parseInt(water.style.gridColumnStart) || 1;
        newWaterDiv.style.gridColumnStart = colStart;
        newWaterDiv.style.gridRowStart = rowStart;
        newWaterDiv.style.gridColumnEnd = 'span 3';

        // Find the correct cell to append to (this is a simplified approach)
        const cellIndex = (rowStart - 1) * 6 + colStart - 1;
        if (cellIndex >= 0 && cellIndex < gridCells.length) {
          gridCells[cellIndex].appendChild(newWaterDiv);
        }
      });
    });
  </script>
</body>
</html>