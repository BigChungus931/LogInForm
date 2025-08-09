import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

window = tk.Tk()
window.title("Sign up")
window.geometry("350x600")
window.resizable(False, False)
window.config(bg="white")

try:
    connection = mysql.connector.connect(
        host = "localhost",
        database = "chatdb",
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
            uname = username_entry.get()
            pwd = password_entry.get()
            cpwd = password_verify_entry.get()
            addr = address_entry.get()
            city = city_entry.get()
            age = age_entry.get()

            if pwd == cpwd:
                cursor.execute("INSERT INTO `users`( `FirstName`, `LastName`, `Username`, `Password`, `Address`, `City`, `Age`) VALUES ( %s, %s, %s, %s, %s, %s, %s )", (fname, lname, uname, pwd, addr, city, age))
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

        tk.Label(frame, text="Create username", bg="white").pack()
        username_entry = tk.Entry(frame, width=30, relief="ridge")
        username_entry.pack(pady=5)

        tk.Label(frame, text="Create password", bg="white").pack()
        password_entry = tk.Entry(frame, width=30, show="*", relief="ridge")
        password_entry.pack(pady=5)

        tk.Label(frame, text="Confirm password", bg="white").pack()
        password_verify_entry = tk.Entry(frame, width=30, show="*", relief="ridge")
        password_verify_entry.pack(pady=5)

        tk.Label(frame, text="Add your address", bg="white").pack()
        address_entry = tk.Entry(frame, width=30, relief="ridge")
        address_entry.pack(pady=5)

        tk.Label(frame, text="Add your city", bg="white").pack()
        city_entry = tk.Entry(frame, width=30, relief="ridge")
        city_entry.pack(pady=5)

        tk.Label(frame, text="Add your age", bg="white").pack()
        age_entry = tk.Entry(frame, width=30, relief="ridge")
        age_entry.pack(pady=5)

        signin_button = tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", width="25", command=add_user, relief="flat")
        signin_button.pack(pady=15)

except Error as e:
    print(f"Error connecting to database {e}")

window.mainloop()