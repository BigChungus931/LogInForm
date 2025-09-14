import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import bcrypt

window = tk.Tk()
window.title("Sign up")
window.geometry("700x600")
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

            error_found = False

            cursor.execute("SELECT COUNT(*) FROM users WHERE Firstname=%s", (fname,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Firstname exists", "Firstname taken")
                error_found = True

            cursor.execute("SELECT COUNT(*) FROM users WHERE Lastname=%s", (lname,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Lastname exists", "lastname taken")
                error_found = True

            cursor.execute("SELECT COUNT(*) FROM users WHERE Email=%s", (email,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Email exists", "Email taken")
                error_found = True

            cursor.execute("SELECT COUNT(*) FROM users WHERE Password=%s", (pwd,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Password exists", "Password taken")
                error_found = True

            cursor.execute("SELECT COUNT(*) FROM users WHERE Country=%s", (country,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Country exists", "Country taken")
                error_found = True

            cursor.execute("SELECT COUNT(*) FROM users WHERE Age=%s", (age,))
            user_count = cursor.fetchone()[0]
            if user_count > 0:
                messagebox.showerror("Age exists", "Age taken")
                error_found = True

            if int(age) < 12:
                messagebox.showerror("You're too young", "Wait until you're 13 years old")
                error_found = True

            if int(age) > 150:
                messagebox.showerror("Too old", "Are you a mummy?")
                error_found = True

            if pwd != cpwd:
                messagebox.showerror("Failed", "Passwords do not match")
                error_found = True

            if not error_found:
                cursor.execute("INSERT INTO `users`( `Firstname`, `Lastname`, `Email`, `Password`, `Country`, `Age`, `Joined`) VALUES ( %s, %s, %s, %s, %s, %s, %s )", (fname, lname, email, hashed_pwd, country, age, joined))
                connection.commit()
                messagebox.showinfo("Success", "User registered successfully")


        frame = tk.Frame(window, bg="white", padx=20, pady=10, width=600, height=700, relief="groove")
        frame.pack(pady=100)
        frame.pack_propagate(False)

        title_Label = tk.Label(frame, text="Sign up", font=("Arial", 14, "bold"), bg="white")
        title_Label.pack(pady=(0,20))

        tk.Label(frame, text="Display first name", bg="white").place(x=0, y=70)
        firstname_entry = tk.Entry(frame, width=45, relief="ridge")
        firstname_entry.place(x=0, y=100)

        tk.Label(frame, text="Display last name", bg="white").place(x=300, y=70)
        lastname_entry = tk.Entry(frame, width=45, relief="ridge")
        lastname_entry.place(x=300, y=100)

        tk.Label(frame, text="Enter email address", bg="white").place(x=0, y=150)
        email_entry = tk.Entry(frame, width=45, relief="ridge")
        email_entry.place(x=0, y=180)

        tk.Label(frame, text="Add your age", bg="white").place(x=300, y=150)
        age_entry = tk.Entry(frame, width=45, relief="ridge")
        age_entry.place(x=300, y=180)

        tk.Label(frame, text="Create password", bg="white").place(x=0, y=230)
        password_entry = tk.Entry(frame, width=45, show="*", relief="ridge")
        password_entry.place(x=0, y=260)

        tk.Label(frame, text="Confirm password", bg="white").place(x=300, y=230)
        password_verify_entry = tk.Entry(frame, width=45, show="*", relief="ridge")
        password_verify_entry.place(x=300, y=260)

        tk.Label(frame, text="Enter your country", bg="white").place(x=225, y=310)
        country_entry = tk.Entry(frame, width=95, relief="ridge")
        country_entry.place(x=0, y=340)


        signin_button = tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", width="25", command=add_user, relief="flat")
        signin_button.place(y=370, x=190)

except Error as e:
    print(f"Error connecting to database {e}")

window.mainloop()