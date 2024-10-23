import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play(choice):
    global user_score, computer_score

    if user_score < 3 and computer_score < 3:
        computer_choice = get_computer_choice()
        result = determine_winner(choice, computer_choice)

        result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
        score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

        if user_score == 3:
            result_label.config(text="🎉 You are the champion! 🎉")
            disable_buttons()
        elif computer_score == 3:
            result_label.config(text="😢 Computer is the champion! 😢")
            disable_buttons()
    else:
        reset_game()

def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    result_label.config(text="Choose Rock, Paper, or Scissors!")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Score label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=('Helvetica', 14))
score_label.pack(pady=10)

# Create buttons for user choices
rock_button = tk.Button(root, text="🪨 Rock", command=lambda: play('rock'), width=15)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="📄 Paper", command=lambda: play('paper'), width=15)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="✂️ Scissors", command=lambda: play('scissors'), width=15)
scissors_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors!", font=('Helvetica', 14))
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()
