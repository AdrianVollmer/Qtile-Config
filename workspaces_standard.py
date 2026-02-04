"""
Standard qtile workspace configuration
Workspaces "float" between screens - each screen shows one workspace at a time
"""

from libqtile.config import Group, Key
from libqtile.lazy import lazy


def create_groups():
    """
    Create 9 standard qtile groups (workspaces)

    Returns:
        List of Group objects
    """
    return [Group(name=str(i), label=str(i)) for i in range(1, 10)]


def create_workspace_keys(mod):
    """
    Create keybindings for standard qtile workspaces

    Args:
        mod: Modifier key (e.g., "mod4")

    Returns:
        List of Key objects
    """
    keys = []
    for i in range(1, 10):
        keys.extend(
            [
                # mod + number = switch to workspace (may switch screens)
                Key(
                    [mod],
                    str(i),
                    lazy.group[str(i)].toscreen(),
                    desc=f"Switch to workspace {i}",
                ),
                # mod + shift + number = move window to workspace and follow
                Key(
                    [mod, "shift"],
                    str(i),
                    lazy.window.togroup(str(i), switch_group=True),
                    desc=f"Move window to workspace {i} and switch",
                ),
            ]
        )
    return keys


def init_workspaces_hook():
    """
    No special initialization needed for standard workspaces
    Returns a no-op function
    """
    def init():
        pass
    return init


def screen_change_hook():
    """
    No special handling needed for standard workspaces
    Returns a no-op function
    """
    def on_screen_change(event):
        pass
    return on_screen_change
