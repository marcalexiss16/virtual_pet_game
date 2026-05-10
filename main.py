import tkinter as tk
from tkinter import ttk

# --- VARIABLES ---
hunger = 100
happiness = 100
energy = 100
age = 0
alive = True

faces = {
    "happy":   "(^‿^)",
    "neutral": "(-.-)",
    "hungry":  "(>_<)",
    "sleepy":  "(-_-)zzz",
    "dead":    "(x_x)"
}

# --- FUNCTIONS ---
def get_mood():
    if not alive:
        return "dead"
    if hunger < 30:
        return "hungry"
    if energy < 30:
        return "sleepy"
    if hunger > 60 and happiness > 60 and energy > 60:
        return "happy"
    return "neutral"

def update_display():
    pet_label.config(text=faces[get_mood()])
    hunger_bar["value"] = hunger
    happiness_bar["value"] = happiness
    energy_bar["value"] = energy
    age_label.config(text=f"Age: {age}")

def feed():
    global hunger
    if not alive: return
    hunger = min(100, hunger + 20)
    msg_label.config(text="Pet was fed.")
    update_display()

def play():
    global happiness, energy
    if not alive: return
    happiness = min(100, happiness + 20)
    energy = max(0, energy - 10)
    msg_label.config(text="Pet played.")
    update_display()

def sleep():
    global energy
    if not alive: return
    energy = min(100, energy + 30)
    msg_label.config(text="Pet is sleeping.")
    update_display()

def time_passing():
    global hunger, happiness, energy, age, alive
    if alive:
        hunger    = max(0, hunger - 2)
        happiness = max(0, happiness - 1)
        energy    = max(0, energy - 1)
        age += 1
        if hunger == 0 or energy == 0:
            alive = False
            msg_label.config(text="Your pet has died.")
        update_display()
    root.after(3000, time_passing)

# --- WINDOW ---
root = tk.Tk()
root.title("Virtual Pet")
root.geometry("340x460")

tk.Label(root, text="Virtual Pet Game", font=("Arial", 16, "bold")).pack(pady=8)

tk.Label(root, text="Difficulty: Normal", font=("Arial", 10)).pack()

age_label = tk.Label(root, text="Age: 0")
age_label.pack()

pet_label = tk.Label(root, text="(^‿^)", font=("Courier", 40))
pet_label.pack(pady=10)

msg_label = tk.Label(root, text="")
msg_label.pack()

# Bars
bar_frame = tk.Frame(root)
bar_frame.pack(pady=6)

tk.Label(bar_frame, text="Hunger   ").grid(row=0, column=0, sticky="w")
hunger_bar = ttk.Progressbar(bar_frame, length=200, maximum=100)
hunger_bar.grid(row=0, column=1, pady=3)

tk.Label(bar_frame, text="Happiness").grid(row=1, column=0, sticky="w")
happiness_bar = ttk.Progressbar(bar_frame, length=200, maximum=100)
happiness_bar.grid(row=1, column=1, pady=3)

tk.Label(bar_frame, text="Energy   ").grid(row=2, column=0, sticky="w")
energy_bar = ttk.Progressbar(bar_frame, length=200, maximum=100)
energy_bar.grid(row=2, column=1, pady=3)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=16)

tk.Button(btn_frame, text="Feed",  width=8, command=feed).grid(row=0, column=0, padx=6)
tk.Button(btn_frame, text="Play",  width=8, command=play).grid(row=0, column=1, padx=6)
tk.Button(btn_frame, text="Sleep", width=8, command=sleep).grid(row=0, column=2, padx=6)

# --- START ---
update_display()
time_passing()
root.mainloop()