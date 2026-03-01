import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from Pages.gallery import *

def show_gallery(self):
    self._current_page = self.show_gallery
    self._current_page_arg = ()
    colors = self.colors[self.current_theme]
    self.clear_main_content()
    self.create_card(" Space Images", "", "🌌")

    # Canvas with scroll bar
    canvas_frame = ttk.Frame(self.main_content)
    canvas_frame.pack(fill="both", expand=True, padx=20, pady=10)

    canvas = tk.Canvas(canvas_frame, background=colors["bg"], highlightbackground=colors["bg"],
                       highlightcolor=colors["bg"], highlightthickness=1)

    canvas.pack(side="left", fill="both", expand=True)

    self.img1 = Image.open("Space images/Hoag.PNG").resize((280, 240))
    self.img2 = Image.open("Space images/Ic1101.PNG").resize((280, 240))
    self.img3 = Image.open("Space images/Vela_pulsar.PNG").resize((280, 240))
    self.img4 = Image.open("Space images/Needle.PNG").resize((280, 240))
    self.img5 = Image.open("Space images/Ton618Newer.PNG").resize((280, 240))
    self.img6 = Image.open("Space images/Laniakea.PNG").resize((280, 240))
    self.img7 = Image.open("Space images/Wasp7b.PNG").resize((280, 240))
    self.img8 = Image.open("Space images/SolarSystem.PNG").resize((280, 240))
    self.img9 = Image.open("Space images/Sirius_A&B.PNG").resize((280, 240))
    self.img10 = Image.open("Space images/Alcyoneus2.PNG").resize((280, 240))
    self.img11 = Image.open("Space images/PhoenixCluster.PNG").resize((280, 240))
    self.img12 = Image.open("Space images/Stephenson.PNG").resize((280, 240))
    self.img13 = Image.open("Space images/Sombrero2.PNG").resize((280, 240))
    self.img14 = Image.open("Space images/Orion.PNG").resize((280, 240))
    self.img15 = Image.open("Space images/horse.PNG").resize((280, 240))
    self.img16 = Image.open("Space images/Helix.PNG").resize((280, 240))
    self.img17 = Image.open("Space images/AlphaCentauri.PNG").resize((280, 240))
    self.img18 = Image.open("Space images/Kepler-425b.PNG").resize((280, 240))

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
    self.tk_img13 = ImageTk.PhotoImage(self.img13)
    self.tk_img14 = ImageTk.PhotoImage(self.img14)
    self.tk_img15 = ImageTk.PhotoImage(self.img15)
    self.tk_img16 = ImageTk.PhotoImage(self.img16)
    self.tk_img17 = ImageTk.PhotoImage(self.img17)
    self.tk_img18 = ImageTk.PhotoImage(self.img18)

    image_list = [self.tk_img1, self.tk_img2, self.tk_img3, self.tk_img4, self.tk_img5, self.tk_img6, self.tk_img7,
                  self.tk_img8, self.tk_img9, self.tk_img10, self.tk_img11, self.tk_img12, self.tk_img13, self.tk_img14,
                  self.tk_img15, self.tk_img16, self.tk_img17, self.tk_img18]

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
            self.gallery(idx)

        canvas.tag_bind(image_id, "<Button-1>", on_image_click)

    total_rows = (len(image_list) + cols - 1) // cols
    canvas.configure(scrollregion=(0, 0, cols * col_width, total_rows * row_height))

    def on_wheel2(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    self.current_canvas_frame = canvas_frame
    canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel2))
    canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))

def gallery(self, i):
        self._current_page = self.gallery
        self._current_page_arg = (i, )
        if i == 0:
            Hoag(self.clear_main_content, self.create_card)

        elif i == 1:
            Ic1101(self.clear_main_content, self.create_card)

        elif i == 2:
            Vela(self.clear_main_content, self.create_card)

        elif i == 3:
            Needle(self.clear_main_content, self.create_card)

        elif i == 4:
            Ton618(self.clear_main_content, self.create_card)

        elif i == 5:
            Laniakea(self.clear_main_content, self.create_card)

        elif i == 6:
            Wasp7b(self.clear_main_content, self.create_card)

        elif i == 7:
            SolarSystem(self.clear_main_content, self.create_card)

        elif i == 8:
            SiriusAB(self.clear_main_content, self.create_card)

        elif i == 9:
            Alcyoneus(self.clear_main_content, self.create_card)

        elif i == 10:
            PhoenixCluster(self.clear_main_content, self.create_card)

        elif i == 11:
            Stephenson(self.clear_main_content, self.create_card)

        elif i == 12:
            Sombrero(self.clear_main_content, self.create_card)

        elif i == 13:
            Orion(self.clear_main_content, self.create_card)

        elif i == 14:
            Horsehead(self.clear_main_content, self.create_card)

        elif i == 15:
            Helix(self.clear_main_content, self.create_card)

        elif i == 16:
            AlphaCentauri(self.clear_main_content, self.create_card)

        elif i == 17:
            Kepler452b(self.clear_main_content, self.create_card)