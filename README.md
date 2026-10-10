# 🏃 Run or Walk 🌧️

This project explores a simple question:

> When it's raining, is it better to run or walk to get less wet? 🌧️

Run or Walk is a small 2D game built with Python and Pygame. The player can choose between walking and running while trying to avoid raindrops.

The goal is to experiment with both movement speeds and observe how many raindrops hit the player.


## 🛠️ Technologies

🐍 Python

🎮 Pygame

🎲 Random


## ✨ Features

* 🌧️ Randomly generated rain

* 🚶 Walking mode

* 🏃 Running mode

* 💧 Raindrop collision detection

* 📊 Drop counter

* 🔄 Game reset functionality

* 🎮 Simple keyboard controls

* 🖥️ Lightweight 2D gameplay

* 🏃 Character animation while running


## 🎮 Game Controls

| Key | Action |
| :--- | :--- |
| 1 | 🚶 Walk |
| 2 | 🏃 Run |
| SPACE | 🔄 Reset |
| Close Window | ❌ Quit the game |


## 🏃 Movement Speeds

* 🚶 Walk: 3 px/frame

* 🏃 Run: 6 px/frame

When running, the character also leans forward slightly to visually represent the increased speed.


## 🌧️ How It Works

The game continuously generates rows of raindrops across the screen.

Each row receives a random horizontal offset, creating variations in the rain pattern.

The player moves horizontally while the raindrops fall from the top of the screen.

Whenever a raindrop collides with the player, the Drops counter increases.

```
if drop.get_rect().colliderect(person.get_rect()):
    drop_count += 1
```

The game therefore allows you to compare the two movement strategies and see how many drops hit the player.


## 🕹️ Gameplay

The player starts at the bottom-left of the screen.

Your objective is to move through the rain while getting hit by as few drops as possible.

Try both options:
```
🚶 Walk  →  3 px/frame
🏃 Run   →  6 px/frame
```

Then reset the game with **SPACE** and compare the results.


## 🧩 Collision Detection

Both the player and the raindrops use rectangular hitboxes.

The game uses Pygame's colliderect() method to detect when a raindrop touches the player:

```
drop.get_rect().colliderect(person.get_rect())
```

Every collision increases the number displayed on the screen:

```
Drops: 12
```


## ⚙️ Requirements

Before running the game, make sure you have:

* 🐍 Python 3

* 🎮 Pygame


## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Leandrado/RunOrWalk
cd RunOrWalk
```

Install Pygame:

```bash
py -m pip install pygame
```


## ▶️ Running the Game

Run the main Python file:

```
python main.py
```

The game will open in a 600 × 300 window.


## 🎯 Project Goal

This project was created as a simple experiment based on the classic "run or walk in the rain" problem.

Besides being a small game, it demonstrates some basic concepts of game development with Pygame:

* 🎮 Game loops

* ⌨️ Keyboard input

* 🏃 Character movement

* 🌧️ Object generation

* 💥 Collision detection

* 🎨 2D rendering

* 🔄 Game state resetting

* 🎲 Randomized behavior


## 📄 License

This project is available for educational and personal use.