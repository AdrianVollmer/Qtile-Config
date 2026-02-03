#!/bin/bash
# System menu for qtile bar

# Main menu
choice=$(echo -e "Power\nReload Config" |
	rofi -dmenu -i -p "System: " \
		-location 1 \
		-xoffset 10 \
		-yoffset 40 \
		-theme-str 'window {width: 200px;}' \
		-theme-str 'listview {lines: 2;}' \
		-theme-str '* {
        background-color: #002b36;
        foreground-color: #839496;
        border-color: #2aa198;
    }' \
		-theme-str 'element {
        padding: 8px;
        border-radius: 0px;
        background-color: #002b36;
        text-color: #839496;
    }' \
		-theme-str 'element selected {
        background-color: #2aa198;
        text-color: #002b36;
    }' \
		-theme-str 'inputbar {padding: 8px; background-color: #073642; children: [prompt, entry];}' \
		-theme-str 'prompt {text-color: #2aa198; background-color: #073642;}' \
		-theme-str 'entry {text-color: #839496; background-color: #073642;}' \
		-theme-str 'window {border: 2px; border-color: #2aa198; padding: 0px;}')

case "$choice" in
"Power")
	# Nested power menu
	power_choice=$(echo -e "← Back\nLogout\nRestart\nShutdown\nLock" |
		rofi -dmenu -i -p "Power: " \
			-location 1 \
			-xoffset 10 \
			-yoffset 40 \
			-theme-str 'window {width: 200px;}' \
			-theme-str 'listview {lines: 5;}' \
			-theme-str '* {background-color: #002b36; foreground-color: #839496; border-color: #2aa198;}' \
			-theme-str 'element {padding: 8px; border-radius: 0px; background-color: #002b36; text-color: #839496;}' \
			-theme-str 'element selected {background-color: #2aa198; text-color: #002b36;}' \
			-theme-str 'inputbar {padding: 8px; background-color: #073642; children: [prompt, entry];}' \
			-theme-str 'prompt {text-color: #2aa198; background-color: #073642;}' \
			-theme-str 'entry {text-color: #839496; background-color: #073642;}' \
			-theme-str 'window {border: 2px; border-color: #2aa198; padding: 0px;}')

	case "$power_choice" in
	"Logout")
		qtile cmd-obj -o cmd -f shutdown
		;;
	"Restart")
		systemctl reboot
		;;
	"Shutdown")
		systemctl poweroff
		;;
	"Lock")
		i3lock -c 002b36 || xscreensaver-command -lock
		;;
	"← Back")
		exec "$0"  # Re-run the script to show main menu
		;;
	esac
	;;
"Reload Config")
	qtile cmd-obj -o cmd -f reload_config
	;;
esac
