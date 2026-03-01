import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from Pages.history import *

def show_history(self):
    self._current_page = self.show_history
    self._current_page_arg = ()
    colors = self.colors[self.current_theme]
    self.clear_main_content()
    self.create_card(" History",
                     "Here we explore space probes and space telescopes.",
                     "🚀")
    # Canvas with scroll bar
    canvas_frame = ttk.Frame(self.main_content)
    canvas_frame.pack(fill="both", expand=True, padx=20, pady=10)

    canvas = tk.Canvas(canvas_frame, background=colors["bg"], highlightbackground=colors["bg"],
                       highlightcolor=colors["bg"], highlightthickness=1)

    canvas.pack(side="left", fill="both", expand=True)

    self.img1 = Image.open("Space images/probes/Venera16.PNG").resize((280, 240))
    self.img2 = Image.open("Space images/probes/Venera4.PNG").resize((280, 240))
    self.img3 = Image.open("Space images/probes/Voyager1.PNG").resize((280, 240))
    self.img4 = Image.open("Space images/probes/Viking1.PNG").resize((280, 240))
    self.img5 = Image.open("Space images/probes/Juno.PNG").resize((280, 240))
    self.img6 = Image.open("Space images/probes/Rosetta.PNG").resize((280, 240))
    self.img7 = Image.open("Space images/probes/Parker.PNG").resize((280, 240))
    self.img8 = Image.open("Space images/probes/Pioneer5.PNG").resize((280, 240))
    self.img9 = Image.open("Space images/probes/hubble.PNG").resize((280, 240))
    self.img10 = Image.open("Space images/probes/JWST.PNG").resize((280, 240))
    self.img11 = Image.open("Space images/probes/Fermi.PNG").resize((280, 240))
    self.img12 = Image.open("Space images/probes/Chandra.PNG").resize((280, 240))

    self.tk_img1 = ImageTk.PhotoImage(self.img1)
    self.tk_img2 = ImageTk.PhotoImage(self.img2)
    self.tk_img3 = ImageTk.PhotoImage(self.img3)
    self.tk_img4 = ImageTk.PhotoImage(self.img4)
    self.tk_img5 = ImageTk.PhotoImage(self.img5)
    self.tk_img6 = ImageTk.PhotoImage(self.img6)
    self.tk_img7 = ImageTk.PhotoImage(self.img7)
    self.tk_img8 = ImageTk.PhotoImage(self.img8)
    self.tk_img9 = ImageTk.PhotoImage(self.img9)
    self.tk_img10 = ImageTk.PhotoImage(self.img10)
    self.tk_img11 = ImageTk.PhotoImage(self.img11)
    self.tk_img12 = ImageTk.PhotoImage(self.img12)

    image_list = [self.tk_img1, self.tk_img2, self.tk_img3, self.tk_img4, self.tk_img5, self.tk_img6, self.tk_img7,
                  self.tk_img8, self.tk_img9, self.tk_img10, self.tk_img11, self.tk_img12]

    row_height = 280
    col_width = 340
    padding = 30
    cols = 3
    for index, img in enumerate(image_list):
        row = index // cols
        col = index % cols
        x = col * col_width + padding
        y = row * row_height + padding

        border_thickness = 2
        canvas.create_rectangle(
            x - border_thickness,
            y - border_thickness,
            x + img.width() + border_thickness,
            y + img.height() + border_thickness,
            fill="white",
            outline="white"
        )

        image_id = canvas.create_image(x, y, image=img, anchor="nw")

        def on_image_click(event, idx=index):
            self.unbind_all("<MouseWheel>")
            self.history(idx)

        canvas.tag_bind(image_id, "<Button-1>", on_image_click)

    total_rows = (len(image_list) + cols - 1) // cols
    canvas.configure(scrollregion=(0, 0, cols * col_width, total_rows * row_height))

    def on_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    self.current_canvas_frame = canvas_frame
    canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel))
    canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))

def history(self, i):
        self._current_page = self.history
        self._current_page_arg = (i,)
        if i == 0:
            Venera16(self.clear_main_content, self.create_card)

        elif i == 1:
            Venera4(self.clear_main_content, self.create_card)

        elif i == 2:
            Voyager1(self.clear_main_content, self.create_card)

        elif i == 3:
            Viking1(self.clear_main_content, self.create_card)

        elif i == 4:
            Juno(self.clear_main_content, self.create_card)

        elif i == 5:
            Rosetta(self.clear_main_content, self.create_card)

        elif i == 6:
            Parker(self.clear_main_content, self.create_card)

        elif i == 7:
            Pioneer5(self.clear_main_content, self.create_card)

        elif i == 8:
            Hubble(self.clear_main_content, self.create_card)

        elif i == 9:
            jwst(self.clear_main_content, self.create_card)

        elif i == 10:
            Fermi(self.clear_main_content, self.create_card)

        elif i == 11:
            Chandra(self.clear_main_content, self.create_card)