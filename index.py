import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Login")
window.geometry("350x350")
window.resizable(False, False)
window.config(bg="white")

frame = tk.Frame(window, bg="white", padx=20, pady=10, relief="flat", borderwidth=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

title_Label = tk.Label(frame, text="Login", font=("Arial", 14, "bold"), bg="white")
title_Label.pack(pady=(0,20))

tk.Label(frame, text="Username", bg="white").pack()
user_entry = tk.Entry(frame, width=30)
user_entry.pack(pady=5)

tk.Label(frame, text="Password", bg="white").pack()
password_entry = tk.Entry(frame, width=30, show="*")
password_entry.pack(pady=5)

def login(event = None):
    username = user_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login success", "Welcome admin")
    else:
        messagebox.showerror("Login failed", "You typed an incorrect username or password, you don't remember it?")

login_button = tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", width="25", command=login, relief="flat")
login_button.pack(pady=15)
window.bind("<Return>", login)

window.mainloop()