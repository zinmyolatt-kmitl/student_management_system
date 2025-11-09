from tkinter import ttk

PRIMARY_BG = "#ffffff"
CARD_BG = "#FFFFFF"
TEXT_COLOR = "#003366"
ACCENT_COLOR = "#000000"
BUTTON_HOVER = "#0057D9"

def setup_style(root):
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("TFrame", background=PRIMARY_BG)
    style.configure("Title.TLabel", background=PRIMARY_BG, foreground=TEXT_COLOR,
                    font=("Helvetica", 18, "bold"))
    style.configure("TLabel", background=PRIMARY_BG, foreground=TEXT_COLOR,
                    font=("Helvetica", 11))
    style.configure("TEntry", font=("Helvetica", 11), padding=6, relief="flat")

    style.configure("TButton",
                    background=CARD_BG, font=("Helvetica", 11, "bold"),
                    padding=(10, 6), relief="flat", borderwidth=0)
    style.map("TButton",
              background=[("active", ACCENT_COLOR)],
              foreground=[("active", "white")])

    style.configure("Vertical.TScrollbar", background=PRIMARY_BG,
                    troughcolor=CARD_BG, bordercolor=PRIMARY_BG)
