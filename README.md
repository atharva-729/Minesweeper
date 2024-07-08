## Minesweeper
This project implements the classic Minesweeper game using Python's Tkinter library and Object-Oriented Programming (OOP) principles. The game offers three difficulty levels:

- **Not So Easy:** A good starting point for beginners.
- **Kinda Hard:** Provides a more challenging experience.
- **DO NOT PRESS:** Named such beacuse a single cell click took 4-5 seconds to update (on my machine), you'll be genuinely frustrated playing in this mode.

****PLEASE NOTE: AT PRESENT, THIS GAME ONLY RUNS AS INTENDED ON WINDOWS AND LINUX (I have no idea about Mac)****

**How to Play:**

1. Run the `main.py` file to launch the game.
2. Select your desired difficulty level from the available options.
3. Click on individual cells to reveal them. Left-click to uncover a cell, and right-click to mark a suspected mine.
4. The objective is to flag all mines while uncovering all safe spaces without detonating a mine. 

### Project Structure:

- `main.py`: Handles game initialization, difficulty selection, and window management. It interacts with `cell.py` for core game logic.
- `cell.py`: Contains algorithms for game functionality, including cell population, updates based on clicks, and game flow management.
- `settings.py`: Stores essential game configuration variables like grid size and mine count.
- `utils.py`: Provides utility functions used by both `main.py` and `cell.py`.
- `screenshot`: An image showcasing the game's earlier stage of development.

#### Credits/Inspiration
This project was built upon the foundations provided by JimShapedCoding's excellent Minesweeper tutorial:  [Python Game Development Project Using OOP – Minesweeper Tutorial (w/ Tkinter)-freeCodeCamp.org](https://youtu.be/OqbGRZx4xUc?si=kzhJqKQUe0t9G29V). Thanks for the clear and concise explanation!<br>
Gemini helped a lot too. Thanks AI!
