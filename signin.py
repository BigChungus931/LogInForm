import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector import Error
import bcrypt
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Sign up")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="white")

logo = Image.open("img/Computer-logo.png")
resized_logo = logo.resize((300, 110))
photo = ImageTk.PhotoImage(resized_logo)
y_step = 70

try:
    connection = mysql.connector.connect(
        host = "localhost",
        database = "computer mind",
        user = "root",
        password = "",
        port = 3306
    )

    if connection.is_connected():
        cursor = connection.cursor()
        print("successfully connected to MySQL database")

        frame = tk.Frame(window, bg="white", padx=20, pady=10, width=600, height=900, relief="groove")
        frame.pack(pady=70)
        frame.pack_propagate(False)

        logo_label = tk.Label(frame, image=photo, bd=0, highlightthickness=0, bg="white")
        logo_label.place(x=75, y=0)

        tk.Label(frame, text="Enter email address", bg="white").place(x=170, y=60 + y_step)
        email_entry = tk.Entry(frame, width=50, relief="ridge")
        email_entry.place(x=75, y=90 + y_step)

        tk.Label(frame, text="Enter password", bg="white").place(x=180, y=140 + y_step)
        password_entry = tk.Entry(frame, width=50, show="*", relief="ridge")
        password_entry.place(x=75, y=170 + y_step)


        signin_button = tk.Button(frame, text="Login", bg="#4CAF50", fg="white", width="25", relief="flat", cursor="hand2")
        signin_button.place(y=250 + y_step, x=150)

        exists = tk.Label(frame, text="Don't have an account?", bg="white")
        exists.place(y=450 + y_step, x=190)

        login = tk.Button(frame, text="Signup", fg="#4CAF50", bg="white", relief="flat", cursor="hand2")
        login.place(y=448 + y_step, x=330)

        def on_enter(event):
            login.config(fg="red")
        def on_leave(event):
            login.config(fg="#4CAF50")

        login.bind("<Enter>", on_enter)
        login.bind("<Leave>", on_leave)


except Error as e:
    print(f"Error connecting to database {e}")

window.mainloop()