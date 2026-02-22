from tkinter import ttk
from Pages.gallery import *
from Pages.history import *
from Quizzes.probes_quiz import *
from Quizzes.stars_quiz import *
from Quizzes.space_images_quiz import *
from includes.functions import *
class AstronomyApp(tk.Tk):
    show_home = show_home
    show_tou = show_tou
    show_about = show_about
    show_gallery = show_gallery
    show_history = show_history
    show_quiz = show_quiz
    show_contact = show_contact
    def __init__(self):
        super().__init__()
        self.title("Astronomy Hub")
        self.geometry("1400x800")
        self.configure(bg="white")
        self.current_theme="dark"
        self.resizable(False, False)
        self.current_canvas_frame = None
        self._current_page = None
        self._current_page_arg = ()

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
                "top_nav":"#BCCEDE",
                "side_nav":"#BCCEDE",
                "bg":"#EBEFFB",
                "card":"#5855F5",
                "text":"black",
                "nav_text":"black",
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

    def change_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.configure_styles()
        colors = self.colors[self.current_theme]
        self.configure(bg=colors["top_nav"])

        for widget in self.top_nav.winfo_children():
            widget.destroy()

        self.create_top_nav()

        for widget in self.side_nav.winfo_children():
            widget.destroy()

        self.create_side_nav()

        if self._current_page is not None:
            self._current_page(* self._current_page_arg)

    def configure_styles(self):
        colors = self.colors[self.current_theme]
        self.style.configure("TopNav.TFrame", background=colors["top_nav"])
        self.style.configure("SideNav.TFrame", background=colors["side_nav"], width=220)
        self.style.configure("Nav.TButton", foreground=colors["nav_text"], background=colors["side_nav"], padding=12, font=("Helvetica", 11, "bold"))
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
        theme_btn = ttk.Button(top_right_frame, text="Change Theme", style="Theme.TButton", command=self.change_theme)
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

    def quiz(self, i):
        self._current_page = self.quiz
        self._current_page_arg = (i,)
        colors = self.colors[self.current_theme]
        if i == 0:
            probes_quiz(self.clear_main_content, self.create_card2, self, colors)

        elif i == 1:
            stars_quiz(self.clear_main_content, self.create_card2, self, colors)

        elif i == 2:
            space_images_quiz(self.clear_main_content, self.create_card2, self, colors)

if __name__ == "__main__":
    app = AstronomyApp()
    app.mainloop()
