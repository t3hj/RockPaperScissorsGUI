import tkinter as tk
import random
import json

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.user_score = 0
        self.computer_score = 0
        self.user_name = "You"
        self.user_wins = 0
        self.load_scores()
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("300x500")  # Adjusted size for name entry and save button
        self.center_window()

        self.create_widgets()
        self.create_buttons()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Enter your name:", font=('Helvetica', 12))
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.name_entry.pack(pady=5)

        self.name_button = tk.Button(self.root, text="Set Name", command=self.set_name, width=15, bg="lightgray")
        self.name_button.pack(pady=5)

        self.score_label = tk.Label(self.root, text=f"Score - {self.user_name}: {self.user_score} | Computer: {self.computer_score}", font=('Helvetica', 14))
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors!", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

    def create_buttons(self):
        self.rock_button = tk.Button(self.root, text="🪨 Rock", command=lambda: self.play('rock'), width=15, bg="lightblue")
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(self.root, text="📄 Paper", command=lambda: self.play('paper'), width=15, bg="lightgreen")
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(self.root, text="✂️ Scissors", command=lambda: self.play('scissors'), width=15, bg="lightcoral")
        self.scissors_button.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.save_button = tk.Button(button_frame, text="💾 Save", command=self.save_scores, width=15, bg="lightgray")
        self.save_button.grid(row=0, column=0, padx=5)

        self.restart_button = tk.Button(button_frame, text="🔄 Restart", command=self.restart_game, width=15, bg="lightyellow")
        self.restart_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(self.root, text="🔄 Reset", command=self.reset_game, width=15, bg="lightyellow")
        self.reset_button.pack(pady=10)

    def set_name(self):
        self.user_name = self.name_entry.get() or "You"
        self.update_score_label()

    def update_score_label(self):
        self.score_label.config(text=f"Score - {self.user_name}: {self.user_score} | Computer: {self.computer_score}")

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def load_scores(self):
        try:
            with open("scores.json", "r") as file:
                data = json.load(file)
                self.user_name = data.get("user_name", "You")
                self.user_score = data.get("user_score", 0)
                self.computer_score = data.get("computer_score", 0)
                self.user_wins = data.get("user_wins", 0)
        except FileNotFoundError:
            self.user_score = 0
            self.computer_score = 0
            self.user_wins = 0

    def save_scores(self):
        data = {
            "user_name": self.user_name,
            "user_score": self.user_score,
            "computer_score": self.computer_score,
            "user_wins": self.user_wins
        }
        with open("scores.json", "w") as file:
            json.dump(data, file)

    def get_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            result = "You win!"
        else:
            self.computer_score += 1
            result = "Computer wins!"
        self.save_scores()
        return result

    def play(self, choice):
        if self.user_score < 3 and self.computer_score < 3:
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(choice, computer_choice)

            self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
            self.update_score_label()

            if self.user_score == 3:
                self.user_wins += 1
                self.result_label.config(text=f"🎉 {self.user_name} are the champion! 🎉")
                self.disable_buttons()
            elif self.computer_score == 3:
                self.result_label.config(text="😢 Computer is the champion! 😢")
                self.disable_buttons()
        else:
            self.restart_game()

    def disable_buttons(self):
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.save_scores()
        self.update_score_label()
        self.result_label.config(text="Choose Rock, Paper, or Scissors!")
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.restart_game()
        self.name_entry.delete(0, tk.END)
        self.user_name = "You"
        self.update_score_label()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
