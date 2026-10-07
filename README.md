# mip

A small Tkinter playground with:
- a **frameless demo window** (`frameless_window.py`)
- the **Spud desktop buddy** app (`spud/main.py`)

## Beginner-friendly quick start

### 1) Prerequisites
- Python **3.10+**
- Tkinter available in your Python install

### 2) Clone and open the project
```bash
git clone https://github.com/GertvdLee/mip.git
cd mip
```

### 3) Run the simple frameless demo
```bash
python frameless_window.py
```
What you should see:
- a frameless, always-on-top window
- positioned near the bottom-right of your screen
- `Esc` closes the window

### 4) Run the Spud app
```bash
python spud/main.py
```
What you should see:
- a frameless, always-on-top potato companion
- random bubbles/animations every few seconds
- memory tracking saved in `spud/memory.json`

## Requirement status check

Based on the current code in this repository, these requirements are implemented:

- [x] Frameless window behavior (`overrideredirect(True)`)
- [x] Always-on-top window behavior (`-topmost`)
- [x] Bottom-right placement support
- [x] Transparent background support with fallback behavior
- [x] Keyboard close shortcut (`Esc`)
- [x] Random events (text bubbles + animations) in Spud
- [x] Basic persistent memory tracking (`spud/memory.json`)
