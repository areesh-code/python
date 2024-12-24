import tkinter as tk
from tkinter import messagebox


class BattleshipGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        
        
        self.grid_size = 5  
        self.buttons = []
        self.ship_positions = [(1, 1), (3, 2), (4, 4)]  

        self.create_widgets()

    def create_widgets(self):
        
        for row in range(self.grid_size):
            button_row = []
            for col in range(self.grid_size):
                button = tk.Button(
                    self.root,
                    text="~",
                    width=4,
                    height=2,
                    command=lambda r=row, c=col: self.fire(r, c),
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def fire(self, row, col):
        
        if (row, col) in self.ship_positions:
            self.buttons[row][col].config(text="X", bg="red")
            self.ship_positions.remove((row, col))
            if not self.ship_positions:
                messagebox.showinfo("Victory!", "You sank all the ships!")
                self.reset_game()
        else:
            self.buttons[row][col].config(text="O", bg="blue")

    def reset_game(self):
        
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.buttons[row][col].config(text="~", bg="SystemButtonFace")
        
        self.ship_positions = [(1, 1), (3, 2), (4, 4)]


if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipGame(root)
    root.mainloop()
