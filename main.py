# Difficulty
difficulty = "Normal"

settings = {
    "Easy": 1,
    "Normal": 2,
    "Hard": 4
}

# Difficulty menu
difficulty_var = tk.StringVar(value="Normal")

def change_difficulty(choice):
    global difficulty

    difficulty = choice

    msg_label.config(
        text=f"{choice} mode selected."
    )

difficulty_menu = tk.OptionMenu(
    root,
    difficulty_var,
    "Easy",
    "Normal",
    "Hard",
    command=change_difficulty
)

difficulty_menu.pack()

# Time system
def time_passing():
    global hunger, happiness, energy

    decay = settings[difficulty]

    hunger = max(0, hunger - decay)
    happiness = max(0, happiness - 1)
    energy = max(0, energy - 1)

    hunger_bar["value"] = hunger
    happiness_bar["value"] = happiness
    energy_bar["value"] = energy

    root.after(3000, time_passing)

time_passing()


faces = {
    "happy": "(^‿^)",
    "neutral": "(-.-)",
    "hungry": "(>_<)",
    "sleepy": "(-_-)zzz"
}

def get_mood():
    if hunger < 20:
        return "hungry"

    if energy < 20:
        return "sleepy"

    if hunger > 60 and happiness > 60:
        return "happy"

    return "neutral"

talk_label = tk.Label(
    root,
    text="",
    bg="#fff0f5",
    font=("Arial", 10, "bold")
)

talk_label.pack()