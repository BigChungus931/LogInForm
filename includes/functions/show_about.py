import tkinter as tk
from tkinter import ttk
def show_about(self):
    self._current_page = self.show_about
    self._current_page_arg = ()
    colors = self.colors[self.current_theme]
    self.clear_main_content()
    self.create_card(" About",
                     "Here we explore space and its big role in role in the Universe, from our planet Earth to the largest stars, galaxies, and blackholes.",
                     "🌟")
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