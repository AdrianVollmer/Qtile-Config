"""
Window layouts and floating rules
This file is shareable across systems
"""

from libqtile import layout
from libqtile.config import Match
from theme import colors
from settings import user_float_rules

# Window layouts
layouts = [
    layout.Columns(
        border_focus=colors["cyan"],
        border_normal=colors["base02"],
        border_focus_stack=colors["violet"],
        border_normal_stack=colors["base02"],
        border_width=4,
        margin=10,
    ),
    layout.MonadTall(
        border_focus=colors["cyan"],
        border_normal=colors["base02"],
        border_width=4,
        margin=10,
    ),
    layout.Max(),
    layout.Bsp(
        border_focus=colors["cyan"],
        border_normal=colors["base02"],
        border_width=4,
        margin=10,
    ),
]

# Floating layout configuration
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Default floating rules
        *layout.Floating.default_float_rules,
        # Common application rules
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="yad"),  # yad calendar and dialogs
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # User-defined rules from settings.py
        *user_float_rules,
    ],
)
