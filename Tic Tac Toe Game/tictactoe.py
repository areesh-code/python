import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#333")

        self.current_player = "X"
        self.board = [""] * 9

        # Title Label
        self.title_label = tk.Label(
            self.root,
            text="Tic-Tac-Toe",
            font=("Arial", 24, "bold"),
            bg="#333",
            fg="#FFD700"
        )
        self.title_label.pack(pady=10)

        # Create game board frame
        self.board_frame = tk.Frame(self.root, bg="#333")
        self.board_frame.pack()

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.board_frame,
                text="",
                font=("Arial", 20, "bold"),
                bg="#444",
                fg="#FFF",
                width=5,
                height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Arial", 14),
            bg="#333",
            fg="#FFF"
        )
        self.status_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 12, "bold"),
            bg="#FFD700",
            fg="#000",
            command=self.reset_game
        )
        self.reset_button.pack(pady=10)

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.status_label.config(
                    text=f"Player {self.current_player} Wins!"
                )
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
            elif "" not in self.board:
                self.status_label.config(text="It's a Draw!")
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(
                    text=f"Player {self.current_player}'s Turn"
                )

    def check_winner(self):
        # Winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for combo in winning_combinations:
            if (
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                and self.board[combo[0]] != ""
            ):
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")
        self.status_label.config(text="Player X's Turn")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()