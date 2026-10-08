import random
import tkinter as tk

from config import (
    MAX_BUBBLE_DURATION,
    MAX_EVENT_INTERVAL,
    MIN_BUBBLE_DURATION,
    MIN_EVENT_INTERVAL,
)

PUNS_AND_COMMENTS = [
    "I'm just here for moral starch.",
    "Tubers gonna tube.",
    "Don't mind me, I'm in spectator mode.",
    "I saw that typo. We both did.",
    "Chaos level: gently simmering.",
    "Plot twist: you're the side character.",
    "Productivity detected. Suspicious.",
]


class SpudLogic:
    def __init__(self, root: tk.Tk, memory_data: dict, visuals):
        self.root = root
        self.memory_data = memory_data
        self.visuals = visuals
        self._bubble: tk.Toplevel | None = None

    def random_event_loop(self) -> None:
        self._run_random_event()
        delay_ms = random.randint(MIN_EVENT_INTERVAL, MAX_EVENT_INTERVAL) * 1000
        self.root.after(delay_ms, self.random_event_loop)

    def _run_random_event(self) -> None:
        event = random.choice(["bubble", "animation", "memory_reference"])

        if event == "bubble":
            self.show_text_bubble(random.choice(PUNS_AND_COMMENTS))
            return

        if event == "animation":
            self.visuals.animate(random.choice(["wiggle", "grow_shrink", "flash"]))
            return

        self.show_text_bubble(self.trigger_memory_comment())

    def show_text_bubble(self, text: str) -> None:
        if self._bubble and self._bubble.winfo_exists():
            self._bubble.destroy()

        bubble = tk.Toplevel(self.root)
        bubble.overrideredirect(True)
        bubble.attributes("-topmost", True)
        bubble.configure(bg="#fffde7")

        label = tk.Label(
            bubble,
            text=text,
            bg="#fffde7",
            fg="#3e2723",
            padx=10,
            pady=6,
            wraplength=220,
            justify="left",
            font=("Segoe UI", 10),
        )
        label.pack()

        x = self.root.winfo_x() - 40
        y = self.root.winfo_y() - 80
        bubble.geometry(f"+{max(0, x)}+{max(0, y)}")

        self._bubble = bubble
        ttl = random.randint(MIN_BUBBLE_DURATION, MAX_BUBBLE_DURATION) * 1000
        bubble.after(ttl, bubble.destroy)

    def trigger_memory_comment(self) -> str:
        days = int(self.memory_data.get("days_active", 1) or 1)
        interactions = int(self.memory_data.get("total_interactions", 0) or 0)

        options = [
            f"Day {days} and we're still doing this. Respect.",
            f"We've logged {days} day(s) together. That's commitment.",
            f"Total interactions: {interactions}. I'm definitely keeping score.",
        ]
        return random.choice(options)
