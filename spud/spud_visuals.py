import tkinter as tk
from pathlib import Path

from config import ASSETS_FOLDER, DEFAULT_SPRITE, FALLBACK_EMOJI, FALLBACK_EMOJI_SIZE


class SpudVisuals:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self._sprite: tk.PhotoImage | None = None
        self.sprite_item: int | None = None
        self.text_item: int | None = None

    def render_spud(self, state: str = "idle") -> None:
        image_path = _image_for_state(state)
        self.canvas.delete("spud")

        if image_path:
            self._sprite = tk.PhotoImage(file=str(image_path))
            self.sprite_item = self.canvas.create_image(
                75,
                75,
                image=self._sprite,
                tags=("spud", "spud_sprite"),
            )
            self.text_item = None
            return

        self.text_item = self.canvas.create_text(
            75,
            75,
            text=FALLBACK_EMOJI,
            font=("Segoe UI Emoji", FALLBACK_EMOJI_SIZE),
            tags=("spud", "spud_sprite"),
        )
        self.sprite_item = None

    def animate(self, animation_type: str) -> None:
        if animation_type == "wiggle":
            self._animate_wiggle()
        elif animation_type == "grow_shrink":
            self._animate_grow_shrink()
        elif animation_type == "flash":
            self._animate_flash()

    def _animate_wiggle(self) -> None:
        target = self.sprite_item or self.text_item
        if not target:
            return

        sequence = [(-4, 0), (8, 0), (-8, 0), (8, 0), (-4, 0)]

        def step(i: int) -> None:
            if i >= len(sequence):
                return
            dx, dy = sequence[i]
            self.canvas.move(target, dx, dy)
            self.canvas.after(40, lambda: step(i + 1))

        step(0)

    def _animate_grow_shrink(self) -> None:
        target = self.sprite_item or self.text_item
        if not target:
            return

        scales = [1.08, 1.08, 0.92, 0.92, 1.0]

        def step(i: int) -> None:
            if i >= len(scales):
                return
            scale = scales[i]
            self.canvas.scale(target, 75, 75, scale, scale)
            self.canvas.after(55, lambda: step(i + 1))

        step(0)

    def _animate_flash(self) -> None:
        target = self.text_item
        if not target:
            # Flash the background ring around image fallback case.
            ring = self.canvas.create_oval(15, 15, 135, 135, outline="#ffd54f", width=4, tags=("spud",))
            self.canvas.after(240, lambda: self.canvas.delete(ring))
            return

        original = self.canvas.itemcget(target, "fill")

        def set_color(color: str) -> None:
            self.canvas.itemconfigure(target, fill=color)

        set_color("#ffd54f")
        self.canvas.after(120, lambda: set_color(original if original else "black"))


def _image_for_state(state: str) -> Path | None:
    candidates = [
        ASSETS_FOLDER / f"{state}.png",
        ASSETS_FOLDER / DEFAULT_SPRITE,
    ]

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    return None
