# 🎲 Pig Dice Game (Scuffed Edition)

A simple Pig Dice Game built with **Python** and **CustomTkinter**, featuring a playable AI opponent, animated dice rolls, and customizable win conditions.

---

## 📌 Features

* 🎮 Player vs Computer gameplay
* 🎲 Animated dice rolling
* 🧠 Simple AI logic (risk-based decisions)
* 🏆 Customizable win score
* 🌙 Dark mode UI using CustomTkinter
* 🔄 Reset / New Game button

---

## 🕹️ How to Play

1. On your turn, click **Roll Dice**
2. Rolling **2–6** adds to your turn score
3. Rolling a **1** ends your turn and resets your turn score
4. Click **Hold** to bank your turn score
5. First player to reach the **Win Score** wins

If **Play vs Computer** is enabled, the AI will automatically take its turn.

---

## ⚙️ Requirements

* Python **3.9+**
* `customtkinter`

Install dependencies:

```bash
pip install customtkinter
```

---

## ▶️ Running the Game

```bash
python pig_dice_game.py
```

Replace `pig_dice_game.py` with your actual file name.

---

## 🧠 AI Behavior

The computer player:

* Continues rolling until it reaches roughly **15 turn points**
* Stops early if it is close to winning
* Automatically ends its turn when rolling a **1**

This keeps gameplay fast and slightly unpredictable.

---

## 🛠️ Customization

* Change the default win score using the input field
* Toggle AI opponent on or off
* Modify AI behavior in the `ai_turn()` function
* Adjust dice animation speed using `app.after()`

---

## 🧪 Known Limitations

* Single human player only
* No sound effects
* Basic AI (intentionally “scuffed”)

---

## 🚀 Possible Future Improvements

* 🎨 Dice images instead of emojis
* 🔊 Sound effects
* 👥 Two-player local mode
* 🧠 Multiple AI difficulty levels
* 📜 Turn history or game log

---

## 📜 License

This project is open-source and free to use for learning, modification, and experimentation.

---

Have fun rolling! 🎲(okay i'll stop talking)
