import tkinter as tk
from tkinter import messagebox

def open_mail():
    label.config(text="CONGRATULATIONS MADAME PRESIDENT!")
    open_button.config(state=tk.DISABLED)
    throw_away_button.config(state=tk.DISABLED)

def throw_away():
    label.config(text="Sure?")
    open_button.config(state=tk.NORMAL)
    throw_away_button.config(state=tk.NORMAL)

def create_mail_window():
    window = tk.Tk()
    window.title("You've Got Mail!")
    window.geometry("300x150")

    global label  # Define label as a global variable
    label = tk.Label(window, text="You've got mail!")
    label.pack(pady=10)

    open_button = tk.Button(window, text="Open", command=open_mail)
    open_button.pack()

    throw_away_button = tk.Button(window, text="Throw Away", command=throw_away)
    throw_away_button.pack()

    window.mainloop()

if __name__ == "__main__":
    create_mail_window()