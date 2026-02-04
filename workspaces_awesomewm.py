"""
AwesomeWM-style workspace configuration
Workspace sticks to screen, similar to AwesomeWM tags
"""

from libqtile.config import Group, Key
from libqtile.lazy import lazy


def create_groups(num_screens=None):
    """
    Create N×9 groups for AwesomeWM-style workspaces

    Args:
        num_screens: Number of monitors (None = auto-detect or use max of 6)

    Returns:
        List of Group objects
    """
    # Create groups for maximum screens (will only use what's needed)
    max_screens = num_screens if num_screens is not None else 6
    groups = []
    for screen in range(max_screens):
        for workspace in range(1, 10):
            groups.append(
                Group(
                    name=f"screen{screen}_{workspace}",  # Internal name
                    label=str(workspace),  # Display label (1-9)
                )
            )
    return groups


def switch_current_screen_to_workspace(qtile, workspace_num):
    """Switch current screen to workspace N (AwesomeWM style)"""
    screen_idx = qtile.current_screen.index
    screen = qtile.screens[screen_idx]
    group_name = f"screen{screen_idx}_{workspace_num}"
    if group_name in qtile.groups_map:
        group = qtile.groups_map[group_name]
        screen.set_group(group)


def move_window_to_workspace(qtile, workspace_num):
    """Move window to workspace N on current screen"""
    screen_idx = qtile.current_screen.index
    group_name = f"screen{screen_idx}_{workspace_num}"
    qtile.current_window.togroup(group_name)


def create_workspace_keys(mod):
    """
    Create keybindings for AwesomeWM-style workspaces

    Args:
        mod: Modifier key (e.g., "mod4")

    Returns:
        List of Key objects
    """
    keys = []
    for i in range(1, 10):
        keys.extend(
            [
                # mod + number = switch current screen to workspace N
                Key(
                    [mod],
                    str(i),
                    lazy.function(switch_current_screen_to_workspace, i),
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
    return keys


def init_workspaces_hook():
    """
    Hook to initialize each screen to workspace 1 on startup
    Returns a function to be used with @hook.subscribe.startup
    """

    def init():
        qtile_obj = __import__("libqtile").qtile
        for screen_idx, screen in enumerate(qtile_obj.screens):
            group_name = f"screen{screen_idx}_1"
            if group_name in qtile_obj.groups_map:
                qtile_obj.groups_map[group_name].toscreen(screen)

    return init


def screen_change_hook():
    """
    Hook to handle screen changes (monitors added/removed)
    Returns a function to be used with @hook.subscribe.screen_change
    """

    def on_screen_change(event):
        qtile_obj = __import__("libqtile").qtile
        # Re-initialize workspaces for all current screens
        for screen_idx, screen in enumerate(qtile_obj.screens):
            # Get the current group for this screen, or default to workspace 1
            current_group = screen.group
            if current_group and current_group.name.startswith(f"screen{screen_idx}_"):
                # Screen already has a valid group
                continue
            else:
                # Initialize to workspace 1
                group_name = f"screen{screen_idx}_1"
                if group_name in qtile_obj.groups_map:
                    qtile_obj.groups_map[group_name].toscreen(screen)

    return on_screen_change
