# Qtile Configuration Structure

This qtile configuration is modularized for easy maintenance and sharing.

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
  - Workspace groups

- **config.py** - Main configuration
  - Imports all modules
  - Combines everything
  - Hooks and startup

## Customization

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
