# mip

`mip` is now organized around a single app: the Spud desktop companion.

Project layout:
- `spud/` — the actual desktop companion app
- `examples/` — demo scripts and experiments, including the old frameless sample
- `README.md` — product guidance for the app

## Quick start

### 1) Prerequisites
- Python **3.10+**
- Tkinter available in your Python install

### 2) Run the Spud app
From the repository root, open a terminal and run:

```bash
python -m spud
```

This starts the desktop companion in its own frameless window, keeps it above other apps, and begins its random bubble/animation loop immediately. On first launch it creates `spud/memory.json` and from then on it persists a lightweight memory log while the app stays running in the background. If you want to keep the original demo window for reference, you can still run `python frameless_window.py` separately.

What you should see:
- a frameless, always-on-top potato companion
- random bubbles/animations every few seconds
- persistent memory saved in `spud/memory.json`
- a simple visual fallback if no sprite asset is available yet

### 3) Run the legacy demo (example only)
```bash
python frameless_window.py
```

This demo is retained as an example and not the product app itself.

## Current implementation status

The repo is now aligned around a single product app in `spud/`.

Implemented:
- [x] Frameless, always-on-top companion window
- [x] Transparent background with fallback behavior
- [x] Corner placement support
- [x] Random text bubbles and animation events
- [x] Persistent memory in `spud/memory.json`
- [x] Package entry point via `python -m spud`
- [x] Demo code isolated under `examples/`

Planned follow-up items:
- [ ] Add real sprite assets in `spud/assets/`
- [ ] Add keyboard activity support (phase 2)
- [ ] Add stronger memory interaction tracking for daily usage
- [ ] Improve Windows click-through reliability
