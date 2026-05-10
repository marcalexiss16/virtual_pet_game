import tkinter as tk
from tkinter import ttk
import random

# ----------------
# VARIABLES
# ----------------
hunger = 100
happiness = 100
energy = 100
age = 0
alive = True

# Difficulty
difficulty = "Normal"

settings = {
    "Easy": 1,
    "Normal": 2,
    "Hard": 4
}

# Challenge
challenge_active = False

challenges = [
    {"msg": "Press FEED!", "action": "feed"},
    {"msg": "Press PLAY!", "action": "play"},
    {"msg": "Press SLEEP!", "action": "sleep"}
]

# ----------------
# FUNCTIONS
# ----------------
def update_display():
    hunger_bar["value"] = hunger
    happiness_bar["value"] = happiness
    energy_bar["value"] = energy

    age_label.config(text=f"Age: {age}")

def feed():
    global hunger
    if not alive:
        return

    hunger = min(100, hunger + 20)

    check_challenge("feed")

    msg_label.config(text="Pet was fed.")
    update_display()

def play():
    global happiness, energy
    if not alive:
        return

    happiness = min(100, happiness + 20)
    energy = max(0, energy - 10)

    check_challenge("play")

    msg_label.config(text="Pet played.")
    update_display()

def sleep():
    global energy
    if not alive:
        return

    energy = min(100, energy + 30)

    check_challenge("sleep")

    msg_label.config(text="Pet is sleeping.")
    update_display()

# ----------------
# TIME SYSTEM
# ----------------
def time_passing():
    global hunger, happiness, energy, age, alive

    if alive:
        decay = settings[difficulty]

        hunger = max(0, hunger - decay)
        happiness = max(0, happiness - 1)
        energy = max(0, energy - 1)

        age += 1

        if hunger == 0 or energy == 0:
            alive = False
            msg_label.config(text="Your pet has died.")

        update_display()

    root.after(3000, time_passing)

# ----------------
# DIFFICULTY
# ----------------
def change_difficulty(choice):
    global difficulty
    difficulty = choice

    msg_label.config(text=f"{choice} mode selected.")

# ----------------
# CHALLENGE SYSTEM
# ----------------
def start_challenge():
    global challenge_active
    global current_challenge

    if alive and not challenge_active:
        challenge_active = True

        current_challenge = random.choice(challenges)

        challenge_label.config(
            text=current_challenge["msg"],
            fg="red"
        )

        root.after(5000, fail_challenge)

def check_challenge(action):
    global challenge_active

    if challenge_active:
        if current_challenge["action"] == action:

            challenge_active = False

            challenge_label.config(
                text="Challenge Complete!",
                fg="green"
            )

def fail_challenge():
    global challenge_active
    global hunger, happiness, energy

    if challenge_active:

        challenge_active = False

        hunger = max(0, hunger - 10)
        happiness = max(0, happiness - 10)
        energy = max(0, energy - 10)

        challenge_label.config(
            text="Challenge Failed!",
            fg="orange"
        )

        update_display()

def challenge_loop():
    if alive:
        start_challenge()

    root.after(15000, challenge_loop)

# ----------------
# WINDOW
# ----------------
root = tk.Tk()

root.title("Virtual Pet")
root.geometry("360x560")
root.config(bg="#fff0f5")

# ----------------
# TITLE
# ----------------
title_label = tk.Label(
    root,
    text="My Virtual Pet",
    font=("Arial", 16, "bold"),
    bg="#fff0f5",
    fg="#ff69b4"
)

title_label.pack(pady=10)

# Difficulty Menu
difficulty_var = tk.StringVar(value="Normal")

difficulty_menu = tk.OptionMenu(
    root,
    difficulty_var,
    "Easy",
    "Normal",
    "Hard",
    command=change_difficulty
)

difficulty_menu.pack()

# Age
age_label = tk.Label(
    root,
    text="Age: 0",
    bg="#fff0f5"
)

age_label.pack()

# Pet Face
pet_label = tk.Label(
    root,
    text="(^_^)",
    font=("Courier", 40),
    bg="#fff0f5",
    fg="#ff69b4"
)

pet_label.pack(pady=10)

# Message
msg_label = tk.Label(
    root,
    text="",
    bg="#fff0f5"
)

msg_label.pack()

# Challenge
challenge_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold"),
    bg="#fff0f5"
)

challenge_label.pack(pady=5)

# ----------------
# BARS
# ----------------
tk.Label(root, text="Hunger", bg="#fff0f5").pack()

hunger_bar = ttk.Progressbar(
    root,
    length=220,
    maximum=100
)

hunger_bar.pack(pady=5)

tk.Label(root, text="Happiness", bg="#fff0f5").pack()

happiness_bar = ttk.Progressbar(
    root,
    length=220,
    maximum=100
)

happiness_bar.pack(pady=5)

tk.Label(root, text="Energy", bg="#fff0f5").pack()

energy_bar = ttk.Progressbar(
    root,
    length=220,
    maximum=100
)

energy_bar.pack(pady=5)

# ----------------
# BUTTONS
# ----------------
button_frame = tk.Frame(
    root,
    bg="#fff0f5"
)

button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Feed",
    width=10,
    bg="#ff9999",
    fg="white",
    command=feed
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Play",
    width=10,
    bg="#99ccff",
    fg="white",
    command=play
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Sleep",
    width=10,
    bg="#cc99ff",
    fg="white",
    command=sleep
).grid(row=0, column=2, padx=5)

# ----------------
# START
# ----------------
update_display()
time_passing()
challenge_loop()

root.mainloop()