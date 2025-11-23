from tkinter import ttk
from PIL import Image, ImageTk
from gallery import *
from history import *
from probes_quiz import *
from stars_quiz import *
from space_images_quiz import *
class AstronomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Astronomy Hub")
        self.geometry("1400x800")
        self.configure(bg="white")
        self.current_theme="light"
        self.resizable(False, False)
        self.current_canvas_frame = None

        #Castom Styling
        self.style=ttk.Style(self)
        self.style.theme_use("clam")

        #Images
        self.img1 = None
        self.img2 = None
        self.img3 = None
        self.img4 = None
        self.img5 = None
        self.img6 = None
        self.img7 = None
        self.img8 = None
        self.img9 = None
        self.img10 = None
        self.img11 = None
        self.img12 = None
        self.img13 = None
        self.img14 = None
        self.img15 = None
        self.img16 = None
        self.img17 = None
        self.img18 = None

        self.tk_img1 = None
        self.tk_img2 = None
        self.tk_img3 = None
        self.tk_img4 = None
        self.tk_img5 = None
        self.tk_img6 = None
        self.tk_img7 = None
        self.tk_img8 = None
        self.tk_img9 = None
        self.tk_img10 = None
        self.tk_img11 = None
        self.tk_img12 = None
        self.tk_img13 = None
        self.tk_img14 = None
        self.tk_img15 = None
        self.tk_img16 = None
        self.tk_img17 = None
        self.tk_img18 = None

        #Color Schemes
        self.colors = {
            "light":{
                "top_nav":"black",
                "side_nav":"black",
                "bg":"#EBEFFB",
                "card":"#5855F5",
                "text":"black",
                "nav_text":"white",
                "score":"#D7DC03"
            },
            "dark":{
                "top_nav":"#161616",
                "side_nav":"#161616",
                "bg":"#252525",
                "card":"#5855F5",
                "text":"white",
                "nav_text":"white",
                "score": "yellow"
            }
        }

        #Configure_style
        self.configure_styles()

        #Create main layout
        self.top_nav = ttk.Frame(self, style="TopNav.TFrame", height=100)
        self.side_nav = ttk.Frame(self, style="SideNav.TFrame", width=400)
        self.side_nav.grid(row=1, column=0, sticky="nsew")
        self.side_nav.grid_propagate(False)
        self.main_content = ttk.Frame(self, style="main.TFrame")

        #Grid layout
        self.top_nav.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.main_content.grid(row=1, column=1, sticky="nsew")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1, minsize=90)

        #Build component
        self.create_top_nav()
        self.create_side_nav()
        self.show_home()

    def configure_styles(self):
        colors = self.colors[self.current_theme]
        self.style.configure("TopNav.TFrame", background=colors["top_nav"])
        self.style.configure("SideNav.TFrame", background=colors["side_nav"], width=220)
        self.style.configure("Nav.TButton", foreground="white", background=colors["side_nav"], padding=12, font=("Helvetica", 11, "bold"))
        self.style.map("Nav.TButton",
                       background=[("active", "white")],
                       foreground=[("active", "black")])
        self.style.configure("main.TFrame", background=colors["bg"])
        self.style.configure("Card.TFrame", background=colors["bg"], relief="flat")
        self.style.configure("Title.TLabel", font=("Helvetica", 20, "bold"), foreground=colors["text"])
        self.style.configure("Subtitle.TLabel", font=("Helvetica", 20), foreground=colors["text"], background=colors["bg"])
        self.style.configure("Text.TLabel", font=("Helvetica", 15), foreground=colors["text"], background=colors["bg"])
        self.style.configure("Textx.TLabel", font=("Bahnschrift", 20), foreground=colors["text"], background=colors["bg"])
        self.style.configure("Theme.TButton", font=("Helvetica", 12, "bold"), padding=10, background=colors["bg"], foreground=colors["text"])
        self.style.map("Theme.TButton",
                       background=[("active", "white")],
                       foreground=[("active", "black")])

    def create_top_nav(self):
        colors = self.colors[self.current_theme]
        top_left_frame = ttk.Frame(self.top_nav)
        top_left_frame.pack(side="left", padx=20, pady=25)

        title = ttk.Label(top_left_frame, text="Astronomy", style="Title.TLabel", foreground=colors["nav_text"], background=colors["top_nav"])
        title.pack(side="left")

        top_right_frame = ttk.Frame(self.top_nav, style="TopNav.TFrame")
        top_right_frame.pack(side="right", padx=20)
        theme_btn = ttk.Button(top_right_frame, text="Change Theme", style="Theme.TButton")
        theme_btn.pack(side="right", padx=10)
    def create_side_nav(self):
        nav_buttons = [
            ("Home", self.show_home),
            ("About", self.show_about),
            ("History", self.show_history),
            ("Quiz", self.show_quiz),
            ("Gallery", self.show_gallery),
            ("Terms of use", self.show_tou),
            ("Contact", self.show_contact)
        ]
        for text, command in nav_buttons:
            btn = ttk.Button(self.side_nav, text=text, style="Nav.TButton", command=command)
            btn.pack(fill="x", ipady=12, pady=15, ipadx=50, padx=50)
    def clear_main_content(self):
        try:
            self.unbind_all("<Mousewheel>")
        except:
            pass
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def create_card(self, title, content, emoji = None):
        card = ttk.Frame(self.main_content, style="Card.TFrame")
        card.pack(fill="x", padx=20, pady=10, ipady=10)
        if emoji:
            title_text = f"{emoji}{title}"

        else:
            title_text = title

        ttk.Label(card, text=title_text, style="Subtitle.TLabel").pack(anchor="w", padx=20, pady=5)
        ttk.Label(card, text=content, style="Text.TLabel", wraplength=1000).pack(anchor="w", padx=20, pady=5)

    def create_card2(self, title, content, emoji = None):
        card = ttk.Frame(self.main_content, style="Card.TFrame")
        card.pack(fill="x", padx=20, pady=10, ipady=10)
        if emoji:
            title_text = f"{emoji}{title}"

        else:
            title_text = title

        ttk.Label(card, text=title_text, style="Subtitle.TLabel").pack(anchor="w", padx=20, pady=5)
        ttk.Label(card, text=content, style="Textx.TLabel", wraplength=1000).pack(anchor="w", padx=20, pady=5)

#Gallery.py content
    def gallery(self, i):
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

    def history(self, i):
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

    def quiz(self, i):
        colors = self.colors[self.current_theme]
        if i == 0:
            probes_quiz(self.clear_main_content, self.create_card2, self, colors)

        elif i == 1:
            stars_quiz(self.clear_main_content, self.create_card2, self, colors)

        elif i == 2:
            space_images_quiz(self.clear_main_content, self.create_card2, self, colors)

    def show_home(self):
        self.clear_main_content()
        self.create_card(" Welcome to Astronomy Hub", "Explore various mystery objects from space that we discovered.", "🔍")

    def show_about(self):
        colors = self.colors[self.current_theme]
        self.clear_main_content()
        self.create_card(" About","Here we explore space and its big role in role in the Universe, from our planet Earth to the largest stars, galaxies, and blackholes.", "🌟")
        canvas_frame = ttk.Frame(self.main_content)
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=10)

        canvas = tk.Canvas(canvas_frame, background=colors["bg"], highlightbackground=colors["bg"],
                           highlightcolor=colors["bg"], highlightthickness=1)

        canvas.pack(side="left", fill="both", expand=True)

        canvas.configure(scrollregion=(0, 0, 500, 500))

        def on_wheel4(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.current_canvas_frame = canvas_frame
        canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel4))
        canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))

    def show_history(self):
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

        image_list = [self.tk_img1, self.tk_img2, self.tk_img3, self.tk_img4, self.tk_img5, self.tk_img6, self.tk_img7, self.tk_img8, self.tk_img9, self.tk_img10, self.tk_img11, self.tk_img12]

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
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.current_canvas_frame = canvas_frame
        canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel))
        canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))

    def show_quiz(self):
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
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.current_canvas_frame = canvas_frame
        canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel3))
        canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))

    def show_gallery(self):
        colors = self.colors[self.current_theme]
        self.clear_main_content()
        self.create_card(" Space Images", "", "🌌")

        #Canvas with scroll bar
        canvas_frame = ttk.Frame(self.main_content)
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=10)

        canvas = tk.Canvas(canvas_frame, background=colors["bg"], highlightbackground=colors["bg"], highlightcolor=colors["bg"], highlightthickness=1)

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

        image_list = [self.tk_img1, self.tk_img2, self.tk_img3, self.tk_img4, self.tk_img5, self.tk_img6, self.tk_img7, self.tk_img8, self.tk_img9, self.tk_img10, self.tk_img11, self.tk_img12, self.tk_img13, self.tk_img14, self.tk_img15, self.tk_img16, self.tk_img17, self.tk_img18]


        row_height = 280
        col_width = 340
        padding = 30
        cols = 3
        for index, img in enumerate(image_list):
            row = index//cols
            col = index%cols
            x = col * col_width + padding
            y = row * row_height + padding

            border_thickness = 2
            canvas.create_rectangle(
                x-border_thickness,
                y-border_thickness,
                x+img.width()+border_thickness,
                y+img.height()+border_thickness,
                fill = "white",
                outline = "white"
            )

            image_id = canvas.create_image(x, y, image = img, anchor="nw")
            def on_image_click(event, idx=index):
                self.unbind_all("<MouseWheel>")
                self.gallery(idx)
            canvas.tag_bind(image_id, "<Button-1>", on_image_click)

        total_rows = (len(image_list) + cols - 1)//cols
        canvas.configure(scrollregion=(0, 0, cols * col_width, total_rows * row_height))

        def on_wheel2(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.current_canvas_frame = canvas_frame
        canvas_frame.bind("<Enter>", lambda e: canvas_frame.bind_all("<MouseWheel>", on_wheel2))
        canvas_frame.bind("<Leave>", lambda e: canvas_frame.unbind_all("<MouseWheel>"))

    def show_tou(self):
        self.clear_main_content()

    def show_contact(self):
        self.clear_main_content()

if __name__ == "__main__":
    app = AstronomyApp()
    app.mainloop()
