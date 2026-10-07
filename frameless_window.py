import tkinter as tk


WIDTH = 320
HEIGHT = 120
MARGIN_X = 20
MARGIN_Y = 40
TRANSPARENT_KEY = "#ff00ff"


def create_window() -> tk.Tk:
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    root.configure(bg=TRANSPARENT_KEY)
    try:
        root.attributes("-transparentcolor", TRANSPARENT_KEY)
    except tk.TclError:
        # Some platforms don't support transparentcolor.
        pass

    root.update_idletasks()
    x = root.winfo_screenwidth() - WIDTH - MARGIN_X
    y = root.winfo_screenheight() - HEIGHT - MARGIN_Y
    root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

    content = tk.Frame(root, bg="#1e1e1e", padx=16, pady=12)
    content.pack(expand=True, fill="both", padx=12, pady=12)

    tk.Label(
        content,
        text="Frameless always-on-top window",
        bg="#1e1e1e",
        fg="white",
        font=("Segoe UI", 11),
    ).pack(expand=True)

    root.bind("<Escape>", lambda _event: root.destroy())
    return root


if __name__ == "__main__":
    create_window().mainloop()
