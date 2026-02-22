import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

def show_quiz(self):
    self._current_page = self.show_quiz
    self._current_page_arg = ()
    self.clear_main_content()
    colors = self.colors[self.current_theme]
    self.clear_main_content()
    self.create_card(" Quiz",
                     "This is the quiz section where you can test your knowledge",
                     "💡")
    # Canvas with scroll bar
    canvas_frame = ttk.Frame(self.main_content)
    canvas_frame.pack(fill="both", expand=True, padx=20, pady=10)

    canvas = tk.Canvas(canvas_frame, background=colors["bg"], highlightbackground=colors["bg"],
                       highlightcolor=colors["bg"], highlightthickness=1)

    canvas.pack(side="left", fill="both", expand=True)

    self.img1 = Image.open("Space images/wasp7b.PNG").resize((280, 240))
    self.img2 = Image.open("Space images/probes/Stars.PNG").resize((280, 240))
    self.img3 = Image.open("Space images/wizard.PNG").resize((280, 240))

    self.tk_img1 = ImageTk.PhotoImage(self.img1)
    self.tk_img2 = ImageTk.PhotoImage(self.img2)
    self.tk_img3 = ImageTk.PhotoImage(self.img3)

    image_list = [self.tk_img1, self.tk_img2, self.tk_img3]

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
            self.quiz(idx)

        canvas.tag_bind(image_id, "<Button-1>", on_image_click)

    total_rows = (len(image_list) + cols - 1) // cols
    canvas.configure(scrollregion=(0, 0, cols * col_width, total_rows * row_height))

    def on_wheel3(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    self.current_canvas_frame = canvas_frame
    canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel3))
    canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))