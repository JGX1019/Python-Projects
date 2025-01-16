import tkinter as tk
from tkinter import Canvas, ttk, messagebox
import pygame
import time

class DigitalClockApp:
    def __init__(self, root):
        self.root = root
        pygame.mixer.init()
        self.setup_window()
        self.create_notebook()
        self.create_clock_canvas()
        self.create_alarm_ui()
        self.update_clock()

    def setup_window(self):
        
        self.root.title("Digital Clock")
        self.root.geometry("360x360")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        style = ttk.Style(self.root)
        style.theme_use("default")
        style.configure("TNotebook", background="black", borderwidth=0)
        style.configure("TNotebook.Tab", background="black", foreground="white")
        style.map("TNotebook.Tab", background=[("selected", "grey")])

    def create_notebook(self):

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.frame1 = tk.Frame(self.notebook, bg="black")
        self.frame2 = tk.Frame(self.notebook, bg="black")

        self.notebook.add(self.frame1, text="Clock")
        self.notebook.add(self.frame2, text="Alarm")

    def create_clock_canvas(self):
        self.canvas = Canvas(self.frame1, width=300, height=300, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.circle = self.canvas.create_oval(50, 50, 250, 250, fill="grey", outline="grey")
        self.time_text = self.canvas.create_text(150, 150, text="", fill="white", font=("Arial", 30, "bold"))

    def update_clock(self):
        self.current_time = time.strftime("%H:%M:%S")
        self.canvas.itemconfig(self.time_text, text=self.current_time)
        self.root.after(1000, self.update_clock)
    
    def create_alarm_ui(self):
        tk.Label(self.frame2, text="Set Alarm (HH:MM:SS)", font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=10)

        self.hour_entry = tk.Entry(self.frame2, width=2, font=("Arial", 14))
        self.hour_entry.pack(side="left", padx=5)
        tk.Label(self.frame2, text=":", font=("Arial", 14), bg="black", fg="white").pack(side="left")

        self.minute_entry = tk.Entry(self.frame2, width=2, font=("Arial", 14))
        self.minute_entry.pack(side="left", padx=5)
        tk.Label(self.frame2, text=":", font=("Arial", 14), bg="black", fg="white").pack(side="left")

        self.second_entry = tk.Entry(self.frame2, width=2, font=("Arial", 14))
        self.second_entry.pack(side="left", padx=5)

        tk.Button(self.frame2, text="Set Alarm", command=self.set_alarm, font=("Arial", 12), bg="grey", fg="black").pack(pady=10)

    def set_alarm(self):
        hour = self.hour_entry.get().zfill(2)  
        minute = self.minute_entry.get().zfill(2)
        second = self.second_entry.get().zfill(2)

        try:
            time.strptime(f"{hour}:{minute}:{second}", "%H:%M:%S")  
            self.alarm_time = f"{hour}:{minute}:{second}"
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time}")
            self.alarm_clock()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM:SS format.")

    def play_alarm_sound(self):
        pygame.mixer.music.load("alarm.mp3")  
        pygame.mixer.music.play(loops=0)   
        pygame.time.Clock().tick(10)  

    def alarm_clock(self):
        current_time = time.strftime("%H:%M:%S")
        if self.alarm_time and current_time == self.alarm_time:
            self.play_alarm_sound()
        else:
            self.root.after(1000, self.alarm_clock)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClockApp(root)
    root.mainloop()