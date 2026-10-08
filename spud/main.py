import ctypes
import tkinter as tk

from config import (
    BACKGROUND_COLOR,
    TOPMOST,
    WINDOW_HEIGHT,
    WINDOW_OFFSET_X,
    WINDOW_OFFSET_Y,
    WINDOW_POSITION,
    WINDOW_WIDTH,
)
from spud_logic import SpudLogic
from spud_memory import load_memory, save_memory, update_daily_tracking
from spud_visuals import SpudVisuals


def _position_geometry(root: tk.Tk) -> str:
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    if "," in WINDOW_POSITION:
        x_str, y_str = WINDOW_POSITION.split(",", maxsplit=1)
        return f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{int(x_str)}+{int(y_str)}"

    match WINDOW_POSITION:
        case "top-left":
            x, y = WINDOW_OFFSET_X, WINDOW_OFFSET_Y
        case "top-right":
            x, y = screen_w - WINDOW_WIDTH - WINDOW_OFFSET_X, WINDOW_OFFSET_Y
        case "bottom-left":
            x, y = WINDOW_OFFSET_X, screen_h - WINDOW_HEIGHT - WINDOW_OFFSET_Y
        case _:
            x, y = (
                screen_w - WINDOW_WIDTH - WINDOW_OFFSET_X,
                screen_h - WINDOW_HEIGHT - WINDOW_OFFSET_Y,
            )

    return f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"


def _best_effort_clickthrough(root: tk.Tk) -> None:
    if root.tk.call("tk", "windowingsystem") != "win32":
        return

    try:
        hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
        exstyle = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, exstyle | 0x20 | 0x80000)
    except Exception:
        # Click-through is best effort only.
        return


def main() -> None:
    memory_data = update_daily_tracking(load_memory())

    root = tk.Tk()
    root.title("Spud")
    root.overrideredirect(True)
    root.attributes("-topmost", TOPMOST)
    root.configure(bg=BACKGROUND_COLOR)
    root.geometry(_position_geometry(root))

    # Transparent color key is best on Windows; alpha fallback for others.
    try:
        root.wm_attributes("-transparentcolor", BACKGROUND_COLOR)
    except tk.TclError:
        root.attributes("-alpha", 0.92)

    _best_effort_clickthrough(root)

    canvas = tk.Canvas(
        root,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        bg=BACKGROUND_COLOR,
        highlightthickness=0,
        bd=0,
    )
    canvas.pack(fill="both", expand=True)

    visuals = SpudVisuals(canvas)
    visuals.render_spud("idle")

    logic = SpudLogic(root, memory_data, visuals)

    def shutdown(*_args) -> None:
        save_memory(memory_data)
        root.destroy()

    root.bind("<Escape>", shutdown)
    root.protocol("WM_DELETE_WINDOW", shutdown)

    initial_delay_ms = 1500
    root.after(initial_delay_ms, logic.random_event_loop)
    root.mainloop()


if __name__ == "__main__":
    main()
