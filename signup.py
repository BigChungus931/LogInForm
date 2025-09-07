import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import bcrypt

window = tk.Tk()
window.title("Sign up")
window.geometry("350x600")
window.resizable(False, False)
window.config(bg="white")

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

        def add_user():
            fname = firstname_entry.get()
            lname = lastname_entry.get()
            email = email_entry.get()
            pwd = password_entry.get()
            cpwd = password_verify_entry.get()
            country = country_entry.get()
            joined = 1
            age = age_entry.get()
            salt = bcrypt.gensalt()
            hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)

            cursor.execute("SELECT COUNT(*) FROM users WHERE Firstname=%s", (fname,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Firstname exists", "Firstname taken")

            cursor.execute("SELECT COUNT(*) FROM users WHERE Lastname=%s", (lname,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Lastname exists", "lastname taken")

            cursor.execute("SELECT COUNT(*) FROM users WHERE Email=%s", (email,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Email exists", "Email taken")

            cursor.execute("SELECT COUNT(*) FROM users WHERE Password=%s", (pwd,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Password exists", "Password taken")

            cursor.execute("SELECT COUNT(*) FROM users WHERE Country=%s", (country,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Country exists", "Country taken")

            cursor.execute("SELECT COUNT(*) FROM users WHERE Age=%s", (age,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Age exists", "Age taken")


            if pwd == cpwd:
                cursor.execute("INSERT INTO `users`( `Firstname`, `Lastname`, `Email`, `Password`, `Country`, `Age`, `Joined`) VALUES ( %s, %s, %s, %s, %s, %s, %s )", (fname, lname, email, hashed_pwd, country, age, joined))
                connection.commit()

            else:
                messagebox.showerror("Failed", "Passwords do not match")

        frame = tk.Frame(window, bg="white", padx=20, pady=10, relief="groove", borderwidth=2)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title_Label = tk.Label(frame, text="Sign up", font=("Arial", 14, "bold"), bg="white")
        title_Label.pack(pady=(0,20))

        tk.Label(frame, text="Display first name", bg="white").pack()
        firstname_entry = tk.Entry(frame, width=30, relief="ridge")
        firstname_entry.pack(pady=5)

        tk.Label(frame, text="Display last name", bg="white").pack()
        lastname_entry = tk.Entry(frame, width=30, relief="ridge")
        lastname_entry.pack(pady=5)

        tk.Label(frame, text="Enter email address", bg="white").pack()
        email_entry = tk.Entry(frame, width=30, relief="ridge")
        email_entry.pack(pady=5)

        tk.Label(frame, text="Create password", bg="white").pack()
        password_entry = tk.Entry(frame, width=30, show="*", relief="ridge")
        password_entry.pack(pady=5)

        tk.Label(frame, text="Confirm password", bg="white").pack()
        password_verify_entry = tk.Entry(frame, width=30, show="*", relief="ridge")
        password_verify_entry.pack(pady=5)

        tk.Label(frame, text="Enter your country of residence", bg="white").pack()
        country_entry = tk.Entry(frame, width=30, relief="ridge")
        country_entry.pack(pady=5)

        tk.Label(frame, text="Add your age", bg="white").pack()
        age_entry = tk.Entry(frame, width=30, relief="ridge")
        age_entry.pack(pady=5)

        signin_button = tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", width="25", command=add_user, relief="flat")
        signin_button.pack(pady=15)

except Error as e:
    print(f"Error connecting to database {e}")

window.mainloop()