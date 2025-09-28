import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import bcrypt
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Sign up")
window.geometry("700x700")
window.resizable(False, False)
window.config(bg="white")

logo = Image.open("img/Computer-logo.png")
resized_logo = logo.resize((300, 90))
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


        frame = tk.Frame(window, bg="white", padx=20, pady=10, width=600, height=900, relief="groove")
        frame.pack(pady=70)
        frame.pack_propagate(False)

        logo_label = tk.Label(frame, image=photo, bd=0, highlightthickness=0)
        logo_label.pack(pady=0)

        # title_Label = tk.Label(frame, text="Sign up", font=("Arial", 14, "bold"), bg="white")
        # title_Label.pack(pady=(0,20))

        tk.Label(frame, text="Display first name", bg="white").place(x=0, y=70 + y_step)
        firstname_entry = tk.Entry(frame, width=45, relief="ridge")
        firstname_entry.place(x=0, y=100 + y_step)

        tk.Label(frame, text="Display last name", bg="white").place(x=300, y=70 + y_step)
        lastname_entry = tk.Entry(frame, width=45, relief="ridge")
        lastname_entry.place(x=300, y=100 + y_step)

        tk.Label(frame, text="Enter email address", bg="white").place(x=0, y=150 + y_step)
        email_entry = tk.Entry(frame, width=45, relief="ridge")
        email_entry.place(x=0, y=180 + y_step)

        tk.Label(frame, text="Add your age", bg="white").place(x=300, y=150 + y_step)
        age_entry = tk.Entry(frame, width=45, relief="ridge")
        age_entry.place(x=300, y=180 + y_step)

        tk.Label(frame, text="Create password", bg="white").place(x=0, y=230 + y_step)
        password_entry = tk.Entry(frame, width=45, show="*", relief="ridge")
        password_entry.place(x=0, y=260 + y_step)

        tk.Label(frame, text="Confirm password", bg="white").place(x=300, y=230 + y_step)
        password_verify_entry = tk.Entry(frame, width=45, show="*", relief="ridge")
        password_verify_entry.place(x=300, y=260 + y_step)

        tk.Label(frame, text="Enter your country", bg="white").place(x=225, y=310 + y_step)
        country_entry = tk.Entry(frame, width=95, relief="ridge")
        country_entry.place(x=0, y=340 + y_step)


        signin_button = tk.Button(frame, text="Signup", bg="#4CAF50", fg="white", width="25", command=add_user, relief="flat", cursor="hand2")
        signin_button.place(y=395 + y_step, x=190)

        exists = tk.Label(frame, text="Already have an account?", bg="white")
        exists.place(y=450 + y_step, x=190)

        login = tk.Button(frame, text="Login", fg="#4CAF50", bg="white", relief="flat", cursor="hand2")
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