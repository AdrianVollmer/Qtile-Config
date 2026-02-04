"""
User-specific settings
Customize this file for your system
"""

from libqtile.config import Match  # noqa


# Modifier key (mod4 = Super/Windows key, mod1 = Alt)
mod = "mod4"

# Terminal emulator (will auto-detect if not specified)
terminal = None  # Set to "alacritty", "kitty", etc. or None for auto-detect

# Workspace mode: "awesomewm" or "standard"
# - awesomewm: Workspaces span all screens (switching workspace changes all monitors)
# - standard: Workspaces float between screens (qtile default)
workspace_mode = "awesomewm"

# Autostart programs - add your startup applications here
autostart_programs = [
    "autorandr --change",
    "flameshot",
    "picom",  # Compositor for effects/transparency
    "nm-applet",  # Network manager applet
    "zoom",
    "firefox",
    "gnome-terminal -- tmux a",
    "virt-manager --show-systray",
    # "nitrogen --restore",  # Wallpaper
]

# Additional floating window rules
# Use xprop to find wm_class and wm_name of windows
user_float_rules = [
    # Match(wm_class="myapp"),
    # Match(title="My Floating Window"),
    Match(title="Zoom Workplace"),  # All zoom windows except the main ("Zoom Workplace - Licensed account")
    Match(wm_class="zoom_linux_float_video_window"),  # Floating video
]


# Custom keybindings
# Format: (modifiers, key, command, description)
# Modifiers use the 'mod' variable defined above
custom_keys = [
    ([mod], "z", "xscreensaver-command -lock", "Lock screen"),
    ([mod], "u", "passmenu.sh", "Pass Menu"),
    # Example: Launch rofi app launcher
    # ([mod], "p", "rofi -show drun", "Launch app launcher"),
    # Example: Take screenshot
    # ([mod, "shift"], "s", "flameshot gui", "Take screenshot"),
    # Example: Launch browser
    # ([mod], "b", "firefox", "Launch browser"),
]
