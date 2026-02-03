"""
User-specific settings
Customize this file for your system
"""

from libqtile.config import Match

# Modifier key (mod4 = Super/Windows key, mod1 = Alt)
mod = "mod4"

# Terminal emulator (will auto-detect if not specified)
terminal = None  # Set to "alacritty", "kitty", etc. or None for auto-detect

# Autostart programs - add your startup applications here
autostart_programs = [
    "flameshot",
    "picom",  # Compositor for effects/transparency
    "nm-applet",  # Network manager applet
    # "nitrogen --restore",  # Wallpaper
]

# Additional floating window rules
# Use xprop to find wm_class and wm_name of windows
user_float_rules = [
    # Match(wm_class="myapp"),
    # Match(title="My Floating Window"),
]
