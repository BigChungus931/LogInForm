import tkinter as tk
from tkinter import messagebox, PhotoImage
from tkinter import Menu
import webbrowser

screen = tk.Tk()
#screen.configure(bg="grey")
screen.title("Sign In")
screen.geometry("500x500")
screen.resizable(False,False)
def spwd():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_pwd.config(image=sizedIcon)
    else:
        password_entry.config(show="*")
        show_pwd.config(image=sizedHide)
def create_menu(screen):
    menu_bar = Menu(screen)
    file_menu = Menu(menu_bar, tearoff = 0)
    file_menu.add_command(label="new", command=lambda : messagebox.showinfo("new", "New file created"))
    file_menu.add_separator()
    file_menu.add_command(label="open", command=lambda: messagebox.showinfo("open", "opened file"))
    file_menu.add_separator()
    file_menu.add_command(label="exit", command=screen.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    about_menu = Menu(menu_bar, tearoff = 0)
    about_menu.add_command(label="about", command=lambda : messagebox.showinfo("about", "This app was developed by Daniel"))
    about_menu.add_separator()
    about_menu.add_command(label="github", command=lambda: webbrowser.open("https://github.com/BigChungus931"))
    menu_bar.add_cascade(label="About", menu=about_menu)
    screen.config(menu = menu_bar)
def login():
    username = name_entry.get()
    pwd = password_entry.get()
    if not username:
        messagebox.showwarning("Input Error", "Username cannot be empty")
    if not pwd:
        messagebox.showwarning("Input Error", "Password cannot be empty")
    if username == "Daniel" and pwd == "1234":
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid username")
create_menu(screen)
logo = PhotoImage(file="user.png")
sizedlogo = logo.subsample(5,5)

icon = PhotoImage(file="eye.png")
sizedIcon = icon.subsample(10,10)

hide = PhotoImage(file="hide.png")
sizedHide = hide.subsample(10,10)
ystep = 100
image = tk.Label(screen, image=sizedlogo).place(x=200, y=30)
header = tk.Label(screen, text="Sign In", font=("Franklin Gothic Medium", 25)).place(x=200, y=50 + ystep)

name_text = tk.Label(screen, text="Name:", font=("Franklin Gothic Medium", 15)).place(x=50, y=110 + ystep)
name_entry = tk.Entry(screen, width=33, fg="black", font=("Franklin Gothic Medium", 15))
name_entry.place(x=50, y=140 + ystep)

password_text = tk.Label(screen, text="Password:", font=("Franklin Gothic Medium", 15)).place(x=50, y=190 + ystep)
password_entry = tk.Entry(screen, width=29, fg="black", font=("Franklin Gothic Medium", 15), show="*")
password_entry.place(x=50, y=220 + ystep)

show_pwd = tk.Button(screen, image=sizedIcon, font=("Franklin Gothic Medium", 12), width=30, height=30, relief="raised", command=spwd)
show_pwd.place(x=405, y=215 + ystep)

btn = tk.Button(screen, text="Enter", font=("Franklin Gothic Medium", 15), width=20, relief="ridge", activebackground="white", activeforeground="grey", justify="left", borderwidth=7, command=login).place(x=140, y=280 + ystep)
screen.mainloop()