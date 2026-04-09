# 🐍 Snake Game

A classic Snake game built with Python's Turtle graphics module.

## Preview

The game features a black screen with a white snake, red food, and a scoreboard that tracks your current score and all-time high score.

## How to Play

- Press **SPACE** to start the game
- Use **W / A / S / D** to move the snake (Up / Left / Down / Right)
- Eat the red food to grow and increase your score
- Avoid hitting the walls or your own tail
- When you die, press **SPACE** to play again

##  Project Structure

```
Snakegame/
├── main.py           # Main game loop, screen setup, start/end menus
├── snake_class.py    # Snake movement, growth, and reset logic
├── food.py           # Food placement and randomization
├── scoreboard.py     # Score display and high score tracking
├── highscore.txt     # Stores the all-time high score (auto-updated)
└── README.md         # This file
```

## Requirements

- Python 3.x
- No extra libraries needed — uses only the built-in `turtle` module

## How to Run

1. Make sure Python 3 is installed on your machine
2. Clone or download this repository
3. Open a terminal in the project folder
4. Run:

```bash
python main.py
```

> On some systems you may need to use `python3` instead of `python`

## High Score

The high score is saved automatically in `highscore.txt`. It persists between sessions. If you want to reset it, open `highscore.txt` and change the number back to `0`.

##  License

This project is open source and free to use.
