import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_instruction = tk.Label(self.master, text="Guess the number between 1 and 100:")
        self.label_instruction.pack(pady=10)

        self.entry_guess = tk.Entry(self.master, width=20)
        self.entry_guess.pack(pady=5)

        self.button_guess = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.button_guess.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry_guess.get())
            self.attempts += 1

            if user_guess < 1 or user_guess > 100:
                messagebox.showwarning("Invalid Guess", "Please enter a number between 1 and 100.")
            else:
                if user_guess == self.secret_number:
                    self.game_over(True)
                elif user_guess < self.secret_number:
                    messagebox.showinfo("Too Low", "Try guessing a higher number.")
                else:
                    messagebox.showinfo("Too High", "Try guessing a lower number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def game_over(self, success):
        if success:
            messagebox.showinfo("Congratulations!", f"You guessed the correct number in {self.attempts} attempts!")
        else:
            messagebox.showinfo("Game Over", f"The number was {self.secret_number}. Better luck next time!")
        self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
