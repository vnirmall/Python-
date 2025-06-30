import tkinter as tk
import random

# Global score variables
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    options = ['Rock', 'Paper', 'Scissors']
    emojis = {'Rock': '✊', 'Paper': '🖐', 'Scissors': '✌'}
    computer_choice = random.choice(options)

    result_text = f"You chose {emojis[user_choice]} {user_choice}\nComputer chose {emojis[computer_choice]} {computer_choice}\n"

    if user_choice == computer_choice:
        result = "It's a tie!"
        result_color = "#f06292"  # light pink
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "🎉 You win!"
        result_color = "#ba68c8"  # light purple
        user_score += 1
    else:
        result = "💻 Computer wins!"
        result_color = "#e91e63"  # vibrant pink
        computer_score += 1

    # Update result display
    result_label.config(text=result_text + result, fg=result_color)
    score_label.config(text=f"🏆 Score - You: {user_score} | Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors ✊🖐✌")
root.geometry("420x430")
root.config(bg="black")

# Heading
tk.Label(
    root, text="Rock ✊ Paper 🖐 Scissors ✌", font=("Comic Sans MS", 18, "bold"),
    bg="black", fg="#e1bee7"  # soft lavender
).pack(pady=15)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="white", justify="center")
result_label.pack(pady=15)

# Score display
score_label = tk.Label(
    root, text="🏆 Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"),
    bg="black", fg="#f8bbd0"  # pale pink
)
score_label.pack(pady=5)

# Buttons for user choices
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

tk.Button(
    button_frame, text="✊ Rock", width=12, font=("Arial", 12, "bold"),
    bg="#9575cd", fg="white", activebackground="#7e57c2",
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame, text="🖐 Paper", width=12, font=("Arial", 12, "bold"),
    bg="#f06292", fg="white", activebackground="#ec407a",
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame, text="✌ Scissors", width=12, font=("Arial", 12, "bold"),
    bg="#ce93d8", fg="black", activebackground="#ba68c8",
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=10)

# Exit button
tk.Button(
    root, text="🚪 Exit Game", font=("Arial", 11, "bold"),
    bg="#e91e63", fg="white", activebackground="#c2185b", width=15,
    command=root.quit
).pack(pady=15)

# Start GUI loop
root.mainloop()