"""Compatibility wrapper for the original frameless demo.

This is kept as a historical example. The product app is the `spud` package.
"""

from examples.frameless_window_demo import create_window


if __name__ == "__main__":
    create_window().mainloop()
