import random

# Challenge variables
challenge_active = False

challenges = [
    {"msg": "Press FEED!", "action": "feed"},
    {"msg": "Press PLAY!", "action": "play"},
    {"msg": "Press SLEEP!", "action": "sleep"}
]

# Challenge label
challenge_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold"),
    bg="#fff0f5"
)

challenge_label.pack(pady=5)

# Functions
def start_challenge():
    global challenge_active
    global current_challenge

    challenge_active = True

    current_challenge = random.choice(challenges)

    challenge_label.config(
        text=current_challenge["msg"],
        fg="red"
    )

def check_challenge(action):
    global challenge_active

    if challenge_active:
        if current_challenge["action"] == action:

            challenge_active = False

            challenge_label.config(
                text="Challenge Complete!",
                fg="green"
            )

# Add inside functions
# feed()
check_challenge("feed")

# play()
check_challenge("play")

# sleep()
check_challenge("sleep")

# Start challenge
root.after(5000, start_challenge)