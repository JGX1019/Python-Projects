import tkinter as tk
import pycountry 
import random

class HangmanGame:

    def __init__(self, root):
        self.root = root

        self.countries = [country.name.upper() for country in pycountry.countries if len(country.name) < 10 and " " not in country.name]
        self.target_word = random.choice(self.countries)

        self.guessed_word = "_" * len(self.target_word)
        self.max_chances = 6
        self.attempts = 0
        self.updated_guessed_word = list(self.guessed_word)
        self.permanent_letters = ["_"] * len(self.target_word)

        print(self.target_word)

        self.root.geometry("1280x720") 

        self.root.configure(background='light blue')

        self.root.title("Country Hangman Game")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg = "lightgreen")
        self.canvas.pack(pady=20)

        self.guess_label = tk.Label(self.root, text=" ".join(self.updated_guessed_word),font=("Helvetica", 40, "bold"), bg="light blue")
        self.guess_label.pack(pady=10)

        self.clear_button = tk.Button(self.root, text="Restart", font=("Helvetica", 16), command=self.restart, bg="lightgreen")
        self.clear_button.pack(pady=10, side=tk.BOTTOM, padx=10)

        self.message_box = tk.Text(self.root, height=1, width=50, font=("Helvetica", 24), bd=0, highlightthickness=0, wrap="word", bg = "lightblue")
        self.message_box.tag_configure("center", justify="center")
        self.message_box.pack(pady=20)

        self.root.bind("<Return>", self.submit_input)
        self.root.bind("<KeyPress>", self.update_display)
        self.root.bind("<BackSpace>", self.clear_input)

    def update_display(self, event):
        if event.char.isalpha():
            for i in range(len(self.updated_guessed_word)):
                if self.updated_guessed_word[i] == "_":
                    self.updated_guessed_word[i] = event.char.upper()
                    break 
            self.guess_label.config(text=" ".join(self.updated_guessed_word))

    def submit_input(self, event):
        self.message_box.config(state="normal")  
        self.message_box.delete("1.0", tk.END)  
        self.message_box.config(state="disabled")

        self.underscored_guess = "".join(self.updated_guessed_word)
        self.guess = self.underscored_guess.replace("_", "").strip()
        self.list_guess = list(self.guess)

        if len(self.guess) != len(self.target_word):
            self.update_message_box = ("Please enter the appropriate no. of words")
            self.message_box.config(state="normal")  
            self.message_box.insert(tk.END, self.update_message_box + "\n")  
            self.message_box.config(state="disabled")
        elif self.guess not in self.countries:
            self.update_message_box = ("Not a valid country")
            self.message_box.config(state="normal")  
            self.message_box.insert(tk.END, self.update_message_box + "\n") 
            self.message_box.config(state="disabled")
        else:
            for i in range(len(self.target_word)):
                if self.updated_guessed_word[i] == self.target_word[i]:
                    self.permanent_letters[i] = self.target_word[i]

            if "".join(self.permanent_letters) == self.target_word:
                self.update_message_box = ("Congratulations! You guessed the word!")
                self.message_box.config(state="normal")  
                self.message_box.insert(tk.END, self.update_message_box + "\n")  
                self.message_box.config(state="disabled")
            else:
                self.attempts += 1
                self.hangman_drawing()
                if self.attempts >= self.max_chances:
                    self.update_message_box = ("You lost! The word was: " + self.target_word)
                    self.message_box.config(state="normal")  
                    self.message_box.insert(tk.END, self.update_message_box + "\n")  
                    self.message_box.config(state="disabled")
                    
            self.updated_guessed_word = self.permanent_letters[:]
            self.guess_label.config(text=" ".join(self.updated_guessed_word))

    def clear_input(self, event):
        for i in range(len(self.target_word)):
            if self.updated_guessed_word[i] == self.permanent_letters[i]:
                pass
            else:
                self.updated_guessed_word = ["_"] * len(self.target_word)
        self.guess_label.config(text=" ".join(self.updated_guessed_word))

    def hangman_drawing(self):
            if self.attempts == 1:
                self.canvas.create_oval(160, 40, 260, 130, width=4)
            elif self.attempts == 2:
                self.canvas.create_line(210, 130, 210, 250, width=4)
            elif self.attempts == 3:
                self.canvas.create_line(210, 130, 275, 180, width=4)
            elif self.attempts == 4:
                self.canvas.create_line(210, 130, 150, 180, width=4)
            elif self.attempts == 5:
                self.canvas.create_line(210, 250, 275, 320, width=4)
            elif self.attempts == 6:
                self.canvas.create_line(210, 250, 150, 320, width=4)

    def restart(self):
        self.root.destroy()
        root = tk.Tk()
        game = HangmanGame(root)
        root.mainloop()
        

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()