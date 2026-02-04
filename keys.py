"""
Keybindings and workspace groups
This file is mostly shareable - mod key is imported from settings
"""

from libqtile.config import Key, Group
from libqtile.lazy import lazy
from settings import mod, custom_keys  # noqa


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    """Move window to previous screen, keeping it in the same workspace"""
    current_screen = qtile.current_screen.index
    new_screen = (current_screen + 1) % len(qtile.screens)
    # Extract workspace number from current group name (e.g., "screen0_3" -> 3)
    current_group = qtile.current_group.name
    workspace_num = current_group.split("_")[1] if "_" in current_group else "1"
    # Move to same workspace on new screen
    target_group = f"screen{new_screen}_{workspace_num}"
    qtile.current_window.togroup(target_group, switch_group=switch_group)
    if switch_screen:
        qtile.cmd_to_screen(new_screen)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    """Move window to next screen, keeping it in the same workspace"""
    current_screen = qtile.current_screen.index
    new_screen = (current_screen - 1) % len(qtile.screens)
    # Extract workspace number from current group name
    current_group = qtile.current_group.name
    workspace_num = current_group.split("_")[1] if "_" in current_group else "1"
    # Move to same workspace on new screen
    target_group = f"screen{new_screen}_{workspace_num}"
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

# AwesomeWM-style workspaces: N screens × 9 workspaces
NUM_SCREENS = 3  # Adjust to your monitor count

# Create N×9 groups internally, labeled 1-9 for display
groups = []
for screen in range(NUM_SCREENS):
    for workspace in range(1, 10):
        groups.append(
            Group(
                name=f"screen{screen}_{workspace}",  # Internal name
                label=str(workspace),  # Display label
            )
        )


def switch_all_screens_to_workspace(qtile, workspace_num):
    """Switch all screens to workspace N (AwesomeWM style)"""
    for screen_idx, screen in enumerate(qtile.screens):
        group_name = f"screen{screen_idx}_{workspace_num}"
        if group_name in qtile.groups_map:
            group = qtile.groups_map[group_name]
            screen.set_group(group)


def move_window_to_workspace(qtile, workspace_num):
    """Move window to workspace N on current screen"""
    screen_idx = qtile.current_screen.index
    group_name = f"screen{screen_idx}_{workspace_num}"
    qtile.current_window.togroup(group_name)


# Add group keybindings - AwesomeWM style
for i in range(1, 10):
    keys.extend(
        [
            # mod + number = switch ALL screens to workspace N
            Key(
                [mod],
                str(i),
                lazy.function(switch_all_screens_to_workspace, i),
                desc=f"Switch all screens to workspace {i}",
            ),
            # mod + shift + number = move window to workspace N on current screen
            Key(
                [mod, "shift"],
                str(i),
                lazy.function(move_window_to_workspace, i),
                desc=f"Move window to workspace {i}",
            ),
        ]
    )

# Add custom user keybindings from settings
for modifiers, key, command, desc in custom_keys:
    keys.append(Key(modifiers, key, lazy.spawn(command), desc=desc))
