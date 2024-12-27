import tkinter as tk
from tkinter import messagebox
import random


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You Win!"
    else:
        return "Computer Wins!"

def player_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)


    player_choice_label.config(text=f"Player: {choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)


def reset_game():
    player_choice_label.config(text="Player: None")
    computer_choice_label.config(text="Computer: None")
    result_label.config(text="Result: None")


window = tk.Tk()
window.title("Rock Paper Scissors Game")


player_choice_label = tk.Label(window, text="Player: None", font=("Arial", 14))
player_choice_label.pack()

computer_choice_label = tk.Label(window, text="Computer: None", font=("Arial", 14))
computer_choice_label.pack()

result_label = tk.Label(window, text="Result: None", font=("Arial", 14, "bold"))
result_label.pack()


rock_button = tk.Button(window, text="Rock", font=("Arial", 12), command=lambda: player_choice("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", font=("Arial", 12), command=lambda: player_choice("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", font=("Arial", 12), command=lambda: player_choice("Scissors"))
scissors_button.pack(pady=5)


reset_button = tk.Button(window, text="Reset", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

window.mainloop()
