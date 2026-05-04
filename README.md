# 🎯 Hangman Game (Python CLI)

## 📌 Overview
This is a command-line implementation of the classic **Hangman game** built using Python.

The player must guess letters to uncover a hidden word before running out of lives.

---

## ✨ Features
- ✅ Random word selection
- ✅ Letter-by-letter guessing
- ✅ Tracks guessed letters
- ✅ Limited lives system
- ✅ Win/Lose conditions

---

## 🛠️ Tech Stack
- Python
- Built-in `random` module

---

## ⚙️ How It Works
- A random word is selected from a predefined list
- The word is displayed as underscores (`_ _ _`)
- The player guesses one letter at a time
- Correct guesses reveal letters
- Wrong guesses reduce lives
- Game ends when:
  - Player guesses the word ✅
  - Lives reach zero ❌

---

## ▶️ Usage

1. Run the program:
```bash
python your_file_name.py
