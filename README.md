# 🐾 Pico Pet

**Your own pixelated companion on a Raspberry Pi Pico!**  
Powered by MicroPython, this mini OLED pet responds to your button presses, shows moods, gets hungry over time, and gives you a reason to smile while coding.

Made with curiosity, creativity, and a sprinkle of artificial personality 🍭

---

## 📦 Features

- OLED display updates live pet status: Hunger & Mood
- Two-button interaction: Feed & Play
- Dynamic mood changes based on hunger/happiness
- Auto-updating display loop every 10 seconds
- Cute starter expressions with room to expand!

---

## 🛠 Hardware Setup

### Raspberry Pi Pico Connections

| Component      | Pico Pin | Notes              |
|----------------|----------|--------------------|
| OLED VCC       | 3.3V     | Power              |
| OLED GND       | GND      | Ground             |
| OLED SCL       | GP17     | I2C Clock          |
| OLED SDA       | GP16     | I2C Data           |
| Feed Button    | GP2      | `PULL_UP` enabled  |
| Play Button    | GP3      | `PULL_UP` enabled  |

---

## ⚙️ Files

- `main.py` — your pet's brain 🧠
- `ssd1306.py` — OLED display driver
- `/docs` — wiring diagram & notes
- `/assets` — pixel sprites (coming soon!)

---

## 📂 Installation Instructions

1. Flash MicroPython to your Raspberry Pi Pico (use [Thonny](https://thonny.org) or similar)
2. Upload `main.py` and `ssd1306.py` to your Pico
3. Wire up the OLED and buttons (see schematic in `/docs`)
4. Reset your Pico and meet your new pet!

---

## 🌱 Future Additions

- Pixel art face using `framebuf`
- Sleep mode with inactivity timer
- Save/load pet state with EEPROM
- Buzzer for mood sounds
- Naming screen on boot

---

## 💡 Credits

- Project by **Willem** (@willer481) — 13 years old and coding like a champ in Python & MicroPython from the UK 🇬🇧  
- Assistant support by **Microsoft Copilot** — your nerdy AI buddy with too much personality and a love for pixel pets 👾

---

## 📜 License

Open-source, remix-friendly.  
License: MIT or feel free to choose your own adventure here!

---

## 🎉 Final Notes

This project is all about learning, tinkering, and having fun. Feel free to fork, modify, or build your own creature zoo.  
If your pet starts talking to you, that’s either a bug… or magic.

