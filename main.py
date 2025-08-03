from machine import Pin, I2C
import time
import ssd1306

# === Display Setup ===
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  # Adjust pins if needed
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# === Button Setup ===
feed_btn = Pin(2, Pin.IN, Pin.PULL_UP)
play_btn = Pin(3, Pin.IN, Pin.PULL_UP)

# === Pet State ===
pet = {
    "hunger": 5,     # 0 = full, 10 = starving
    "happiness": 5,  # 0 = sad, 10 = thrilled
    "awake": True
}

# === OLED Face Display ===
def show_pet():
    oled.fill(0)
    if not pet["awake"]:
        oled.text("Zzz...", 0, 8)
    else:
        face = ":)" if pet["happiness"] > 5 else ":("
        oled.text(f"Hunger: {pet['hunger']}", 0, 0)
        oled.text(f"Mood: {face}", 0, 16)
    oled.show()

# === Button Actions ===
def feed(p):
    pet["hunger"] = max(0, pet["hunger"] - 1)
    show_pet()

def play(p):
    pet["happiness"] = min(10, pet["happiness"] + 1)
    show_pet()

feed_btn.irq(trigger=Pin.IRQ_FALLING, handler=feed)
play_btn.irq(trigger=Pin.IRQ_FALLING, handler=play)

# === Main Loop ===
while True:
    # Pet gets hungrier/sadder over time
    time.sleep(10)
    if pet["awake"]:
        pet["hunger"] = min(10, pet["hunger"] + 1)
        pet["happiness"] = max(0, pet["happiness"] - 1)
        show_pet()
