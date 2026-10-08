from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Window settings
WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150
WINDOW_POSITION = "bottom-right"  # "top-left", "top-right", "bottom-left", "bottom-right", or "x,y"
WINDOW_OFFSET_X = 24
WINDOW_OFFSET_Y = 48
BACKGROUND_COLOR = "magenta"
TOPMOST = True

# Timing (seconds)
MIN_EVENT_INTERVAL = 10
MAX_EVENT_INTERVAL = 30
MIN_BUBBLE_DURATION = 3
MAX_BUBBLE_DURATION = 5

# File paths
MEMORY_FILE = BASE_DIR / "memory.json"
ASSETS_FOLDER = BASE_DIR / "assets"
DEFAULT_SPRITE = "spud.png"

# Fallback rendering
FALLBACK_EMOJI = "🥔"
FALLBACK_EMOJI_SIZE = 72
