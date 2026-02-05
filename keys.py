"""
Keybindings and workspace groups
This file is mostly shareable - mod key is imported from settings
"""

from libqtile.config import Key, Group
from libqtile.lazy import lazy
from settings import mod, custom_keys, workspace_mode  # noqa

# Import workspace module based on mode
if workspace_mode == "awesomewm":
    from workspaces_awesomewm import create_groups, create_workspace_keys
else:
    from workspaces_standard import create_groups, create_workspace_keys


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    """Move window to previous screen to its currently active group"""
    current_screen = qtile.current_screen.index
    new_screen = (current_screen + 1) % len(qtile.screens)
    # Get the currently active group on the target screen
    target_group = qtile.screens[new_screen].group.name
    qtile.current_window.togroup(target_group, switch_group=switch_group)
    if switch_screen:
        qtile.cmd_to_screen(new_screen)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    """Move window to next screen to its currently active group"""
    current_screen = qtile.current_screen.index
    new_screen = (current_screen - 1) % len(qtile.screens)
    # Get the currently active group on the target screen
    target_group = qtile.screens[new_screen].group.name
    qtile.current_window.togroup(target_group, switch_group=switch_group)
    if switch_screen:
        qtile.cmd_to_screen(new_screen)


# Keybindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Window management
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    # Layout management
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Qtile management
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Screen management
    Key([mod], "comma", lazy.next_screen(), desc="Focus next screen"),
    Key([mod], "period", lazy.prev_screen(), desc="Focus previous screen"),
    Key([mod], "p", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod], "o", lazy.function(window_to_previous_screen, switch_screen=True)),
]

# AwesomeWM-style workspaces (auto-detects screens, max 6)
groups = create_groups()

# Add workspace keybindings
keys.extend(create_workspace_keys(mod))

# Add custom user keybindings from settings
for modifiers, key, command, desc in custom_keys:
    keys.append(Key(modifiers, key, lazy.spawn(command), desc=desc))
