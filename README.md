# 🧩 Sliding Image Puzzle Game (3×3)

This is a personal Python project that implements a **3×3 sliding image puzzle game** using **Tkinter**.  
The game challenges players to rearrange image tiles into the correct order by sliding them into an empty space.

The project was created to improve my **Python programming skills**, **GUI development**, and **game logic implementation**.

---

## 🎮 Game Features
- 3×3 sliding image puzzle
- Randomized but solvable puzzle generation
- Move validation (only adjacent tiles can move)
- Timer to track completion time
- Sound effects for tile movement and winning
- Win detection with visual feedback
- Restart (“Again”) button

---

## 🛠️ Technologies Used
- **Python**
- **Tkinter** (GUI)
- **playsound** (sound effects)
- **OpenCV not required** (pure Tkinter implementation)

---

## 📁 Project Structure

├── main.py

├── SlidePuzzlePic/

│ └── Lulu/

│ ├── row-1-column-1.png

│ ├── row-1-column-2.png

│ ├── row-1-column-3.png

│ ├── row-2-column-1.png

│ ├── row-2-column-2.png

│ ├── row-2-column-3.png

│ ├── row-3-column-1.png

│ └── row-3-column-2.png

├── SlidePuzzleSoundEffect/

│ ├── click_sound_2.wav

│ └── win_sound_2.wav

---

## ▶️ How to Run
1. Make sure **Python 3** is installed
2. Install the required library:
   ```bash
   pip install playsound
Ensure image and sound folders are placed correctly:

- SlidePuzzlePic/Lulu

- SlidePuzzleSoundEffect

Run the game:

    python main.py

---

## ⚙️ How the Game Works

The puzzle consists of 8 image tiles and 1 empty space

Tiles can only move if they are adjacent to the empty space

The board is randomized at the start while ensuring it remains solvable

A timer starts automatically when the game begins

When all tiles are placed in the correct order, a win message and sound effect are triggered

---

## 🧠 Learning Outcomes

Through this project, I practiced:

- Object-oriented programming in Python

- Tkinter GUI layout using grid

- Game state management

- Randomized puzzle logic

- Event handling and timing with after()

- File handling for images and sound effects

---

## 📌 Future Improvements

- Add difficulty levels (4×4, 5×5)

- Add move counter

- Improve UI layout and animations

- Add image selection feature

---
