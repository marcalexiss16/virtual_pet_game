# Add this below the pet label

msg_label = tk.Label(
    root,
    text="",
    bg="#fff0f5",
    font=("Arial", 10)
)

msg_label.pack()

# Update functions

def feed():
    global hunger
    hunger = min(100, hunger + 10)
    hunger_bar["value"] = hunger
    msg_label.config(text="Pet was fed.")

def play():
    global happiness
    happiness = min(100, happiness + 10)
    happiness_bar["value"] = happiness
    msg_label.config(text="Pet played.")

def sleep():
    global energy
    energy = min(100, energy + 10)
    energy_bar["value"] = energy
    msg_label.config(text="Pet is sleeping.")