"""
Theme configuration - Solarized Dark with Powerline separators
This file is shareable across systems
"""

import os
import subprocess
from libqtile import bar, widget
from libqtile.lazy import lazy  # noqa

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


def create_bar(include_systray=True, screen_index=0):
    """Create the status bar with widgets"""
    widgets = [
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
            # Text colors - clear visual hierarchy
            active=colors["yellow"],          # Groups with windows (not current) = YELLOW
            inactive=colors["base01"],        # Empty groups = dark gray
            # Highlight method
            highlight_method="block",
            # Border colors - THIS SCREEN
            this_current_screen_border=colors["cyan"],     # ← YOUR ACTIVE GROUP (cyan border!)
            this_screen_border=colors["base02"],           # Other groups on this screen
            # Border colors - OTHER SCREENS
            other_current_screen_border=colors["blue"],    # Active on other screen (blue)
            other_screen_border=colors["base02"],          # Other groups on other screens
            # Special states
            urgent_border=colors["red"],
            # Background colors
            background=colors["base03"],
            highlight_color=colors["base02"],
            block_highlight_text_color=colors["base3"],    # Current group = BRIGHT WHITE
            # Filter to show only this screen's groups (1-9 for this screen)
            visible_groups=[f"screen{screen_index}_{i}" for i in range(1, 10)],
            # Style
            rounded=False,
            padding_x=10,
            padding_y=8,
            borderwidth=3,
            disable_drag=True,
            use_mouse_wheel=False,
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
        powerline_sep(colors["magenta"], colors["green"], direction="right"),
        widget.Battery(
            foreground=colors["base03"],
            background=colors["magenta"],
            format="{char} {percent:2.0%}",
            charge_char="",
            discharge_char="\uf240",
            full_char="",
            empty_char="\uf244",
            not_charging_char="",
            show_short_text=False,
            low_foreground=colors["red"],
            low_percentage=0.2,
            notify_below=15,
            hide_threshold=0.98,
            update_interval=30,
            padding=10,
        ),
        powerline_sep(colors["yellow"], colors["magenta"], direction="right"),
        widget.Clock(
            foreground=colors["base03"],
            background=colors["yellow"],
            format="\uf017 %a %b %d  %I:%M %p",
            padding=10,
            update_interval=1.0,
            mouse_callbacks={
                "Button1": lambda: subprocess.Popen(
                    [
                        "env",
                        "GTK_THEME=Adwaita:dark",
                        "yad",
                        "--calendar",
                        "--undecorated",
                        "--close-on-unfocus",
                        "--no-buttons",
                        "--posx=-10",
                        "--posy=40",
                    ]
                )
            },
        ),
        powerline_sep(colors["orange"], colors["yellow"], direction="right"),
    ]

    # Add systray only to primary screen
    if include_systray:
        widgets.append(
            widget.Systray(
                background=colors["orange"],
                padding=8,
            )
        )

    # QuickExit on all screens
    widgets.append(
        widget.QuickExit(
            foreground=colors["base3"],
            background=colors["orange"],
            default_text=" ",
            countdown_format=" [{}]",
            padding=10,
            fontsize=16,
        )
    )

    return bar.Bar(
        widgets,
        30,
        background=colors["base03"],
        margin=[8, 8, 0, 8],
        opacity=0.95,
    )
