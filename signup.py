import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Sign up")
window.geometry("350x350")
window.resizable(False, False)
window.config(bg="white")

frame = tk.Frame(window, bg="white", padx=20, pady=10, relief="flat", borderwidth=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

title_Label = tk.Label(frame, text="Sign up", font=("Arial", 14, "bold"), bg="white")
title_Label.pack(pady=(0,20))

tk.Label(frame, text="Create username", bg="white").pack()
name_entry = tk.Entry(frame, width=30)
name_entry.pack(pady=5)

tk.Label(frame, text="Create Password", bg="white").pack()
password_entry = tk.Entry(frame, width=30, show="*")
password_entry.pack(pady=5)

window.mainloop()