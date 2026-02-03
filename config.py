"""
Main Qtile configuration file
This imports and combines all modular config files
"""

import subprocess

from libqtile import hook
from libqtile.config import Click, Drag, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Import modular configuration
from settings import mod, terminal, autostart_programs
from theme import create_bar, widget_defaults, extension_defaults  # noqa
from layouts import layouts, floating_layout  # noqa
from keys import keys, groups  # noqa

# Terminal setup
if terminal is None:
    terminal = guess_terminal()

# Add terminal launch keybinding
keys.insert(0, Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"))

# Add key bindings to switch VTs in Wayland
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: __import__('libqtile').qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# Screen configuration
screens = [Screen(top=create_bar())]

# Mouse bindings
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# General settings
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True
auto_minimize = True

# Wayland settings
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

# Java app compatibility
wmname = "LG3D"


# Autostart hook
@hook.subscribe.startup_once
def autostart():
    """Run autostart programs once on qtile startup"""
    for program in autostart_programs:
        subprocess.Popen(program.split())
