# Qtile Configuration Structure

This qtile configuration is modularized for easy maintenance and sharing.

Needs qtile-extras.

![screenshot](/screenshot.png)

## Installation

Since we need qtile-extras, let's install the python dependencies in its own
venv:

```
$ pwd
/opt/qtile
$ cat requirements.txt
qtile[widgets]
psutils
qtile-extras
$ uv venv && uv pip install -r requirements
$ cat /usr/share/xsessions/qtile.desktop
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
#  Exec=/usr/bin/qtile-start
# Use our qtile installation:
Exec=/opt/qtile/.venv/bin/qtile start
Type=Application
Keywords=wm;tiling
```

Then link the config:

```
ln -s /path/to/this/repo ~/.config/qtile
```

## File Structure

### User-Specific Files (customize these)
- **settings.py** - Your personal settings
  - Modifier key (Super/Alt)
  - Terminal preference
  - Autostart programs

### Shareable Files (can be shared/versioned)
- **theme.py** - Visual configuration
  - Solarized color scheme
  - Status bar layout
  - Powerline separators
  - Widget styling

- **layouts.py** - Window management
  - Window layouts (Columns, MonadTall, BSP, Max)
  - Floating window rules
  - Border styles and margins

- **keys.py** - Keyboard shortcuts
  - Window navigation (hjkl)
  - Window movement
  - Layout switching
  - Workspace groups (imports from workspaces module)

- **workspaces_awesomewm.py** - AwesomeWM-style workspace behavior
  - Workspaces that span all screens
  - Switching workspaces changes all monitors simultaneously
  - Moving windows between screens preserves workspace
  - Auto-detects number of monitors (supports up to 6)
  - Handles hot-plugging monitors (dock/undock laptop)

- **workspaces_standard.py** - Standard qtile workspace behavior
  - Workspaces float between screens
  - Traditional qtile workspace model

- **config.py** - Main configuration
  - Imports all modules
  - Combines everything
  - Hooks and startup

## Customization

### To switch workspace modes:

Edit `settings.py` and change one line:

```python
# Choose your workspace behavior:
workspace_mode = "awesomewm"  # Each workspace lives on its screen so we have 3*N workspaces
# OR
workspace_mode = "standard"   # Workspaces float between screens (qtile default)
```

**AwesomeWM mode:**
- Pressing `Mod+2` switches to workspace 2 of the focused screen
- Each monitor has its own set of workspaces

**Standard mode:**
- Pressing `Mod+2` switches to workspace 2 (may change screens)
- Each screen independently shows one workspace
- Workspaces "float" to whichever screen is viewing them

### To change autostart programs:
Edit `settings.py` and modify the `autostart_programs` list.

### To add custom floating window rules:
Edit `settings.py` and add Match rules to the `user_float_rules` list. Use `xprop` to find window class names.

### To customize the system menu:
Edit `system_menu.sh` to add/remove menu options or change commands. The menu appears when clicking the settings icon (⚙) in the bar.

### To add custom keybindings:
Edit `settings.py` and add entries to the `custom_keys` list:
```python
custom_keys = [
    ([mod], "p", "rofi -show drun", "Launch app launcher"),
    ([mod, "shift"], "s", "flameshot gui", "Take screenshot"),
]
```

### To change colors or bar appearance:
Edit `theme.py` - you can change the color scheme or modify the bar layout.

### To add/modify layouts:
Edit `layouts.py` to add new layouts or modify existing ones.

### To customize keybindings:
Edit `keys.py` to change keyboard shortcuts.

## Features

- **Solarized Dark** color scheme
- **Powerline-style** triangle separators
- **Nerd Font icons** for system info
- **System menu dropdown** - Settings icon with Logout/Restart/Shutdown/Lock options
- **Calendar popup** on clock click (requires yad)
- **Visual workspace indicators** (cyan = occupied, dim = empty)
- **Glowing window borders** (4px cyan borders)
- **System monitoring** (CPU, Memory, Network, Volume)
- **Autostart support** for your favorite programs

## Requirements

- Cascadia Code NF (or another Nerd Font)
- yad (for calendar popup)
- rofi (for system menu dropdown)
- i3lock/xscreensaver-command (optional, for screen locking)
- picom (optional, for effects)
- flameshot (optional, for screenshots)
