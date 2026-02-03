"""
Theme configuration - Solarized Dark with Powerline separators
This file is shareable across systems
"""

import os
import subprocess
from libqtile import bar, widget
from libqtile.lazy import lazy

# Get the directory where this config file is located
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))

# Solarized color scheme
colors = {
    "base03": "#002b36",
    "base02": "#073642",
    "base01": "#586e75",
    "base00": "#657b83",
    "base0": "#839496",
    "base1": "#93a1a1",
    "base2": "#eee8d5",
    "base3": "#fdf6e3",
    "yellow": "#b58900",
    "orange": "#cb4b16",
    "red": "#dc322f",
    "magenta": "#d33682",
    "violet": "#6c71c4",
    "blue": "#268bd2",
    "cyan": "#2aa198",
    "green": "#859900",
}

# Widget defaults
widget_defaults = dict(
    font="Cascadia Code NF",
    fontsize=13,
    padding=8,
    background=colors["base03"],
)
extension_defaults = widget_defaults.copy()


def powerline_sep(fg_color, bg_color, direction="left"):
    """Create a powerline separator widget"""
    if direction == "left":
        return widget.TextBox(
            text="\ue0b0",  # Powerline arrow
            fontsize=28,
            foreground=fg_color,
            background=bg_color,
            padding=0,
        )
    else:
        return widget.TextBox(
            text="\ue0b2",  # Powerline arrow (right)
            fontsize=28,
            foreground=fg_color,
            background=bg_color,
            padding=0,
        )


def create_bar():
    """Create the status bar with widgets"""
    return bar.Bar(
        [
            # Left side - Logo and groups
            widget.TextBox(
                text="\uf013",  # Settings/menu icon
                fontsize=14,
                foreground=colors["blue"],
                background=colors["base03"],
                padding=10,
                mouse_callbacks={"Button1": lambda: subprocess.Popen(["bash", f"{CONFIG_DIR}/system_menu.sh"])},
            ),
            widget.GroupBox(
                fontsize=14,
                active=colors["cyan"],
                inactive=colors["base02"],
                highlight_method="block",
                this_current_screen_border=colors["violet"],
                this_screen_border=colors["blue"],
                other_current_screen_border=colors["base01"],
                other_screen_border=colors["base01"],
                urgent_border=colors["red"],
                background=colors["base03"],
                foreground=colors["base0"],
                highlight_color=colors["base02"],
                block_highlight_text_color=colors["base3"],
                rounded=False,
                padding_x=10,
                padding_y=8,
                borderwidth=3,
                disable_drag=True,
                use_mouse_wheel=False,
                markup=True,
            ),
            powerline_sep(colors["base03"], colors["base02"]),
            widget.CurrentLayout(
                foreground=colors["yellow"],
                background=colors["base02"],
                padding=10,
                fmt=" {}",
            ),
            powerline_sep(colors["base02"], colors["base03"]),
            widget.Prompt(
                foreground=colors["green"],
                background=colors["base03"],
                prompt="  ",
            ),
            widget.WindowName(
                foreground=colors["base0"],
                background=colors["base03"],
                max_chars=60,
                padding=10,
            ),
            # Right side - System info
            powerline_sep(colors["base02"], colors["base03"], direction="right"),
            widget.CPU(
                foreground=colors["cyan"],
                background=colors["base02"],
                format="\uf4bc {load_percent}%",
                padding=10,
                update_interval=2,
            ),
            powerline_sep(colors["violet"], colors["base02"], direction="right"),
            widget.Memory(
                foreground=colors["base3"],
                background=colors["violet"],
                format="\uf2db {MemUsed:.0f}{mm}",
                measure_mem="G",
                padding=10,
                update_interval=2,
            ),
            powerline_sep(colors["blue"], colors["violet"], direction="right"),
            widget.Net(
                foreground=colors["base3"],
                background=colors["blue"],
                format="\uf0ab {down:.0f}{down_suffix} \uf0aa {up:.0f}{up_suffix}",
                padding=10,
                update_interval=2,
                use_bits=False,
            ),
            powerline_sep(colors["green"], colors["blue"], direction="right"),
            widget.Volume(
                foreground=colors["base03"],
                background=colors["green"],
                fmt="\uf028 {}",
                padding=10,
            ),
            powerline_sep(colors["yellow"], colors["green"], direction="right"),
            widget.Clock(
                foreground=colors["base03"],
                background=colors["yellow"],
                format="\uf017 %a %b %d  %I:%M %p",
                padding=10,
                mouse_callbacks={
                    "Button1": lambda: subprocess.Popen([
                        "env", "GTK_THEME=Adwaita:dark",
                        "yad", "--calendar", "--undecorated",
                        "--close-on-unfocus", "--no-buttons",
                        "--posx=-10", "--posy=40"
                    ])
                },
            ),
            powerline_sep(colors["orange"], colors["yellow"], direction="right"),
            widget.Systray(
                background=colors["orange"],
                padding=8,
            ),
            widget.QuickExit(
                foreground=colors["base3"],
                background=colors["orange"],
                default_text=" ",
                countdown_format=" [{}]",
                padding=10,
                fontsize=16,
            ),
        ],
        30,
        background=colors["base03"],
        margin=[8, 8, 0, 8],
        opacity=0.95,
    )
