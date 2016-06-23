# Sublime PICO-8

PICO-8 plugin for the [Sublime Text 3](https://www.sublimetext.com/) editor.

![screenshot](https://raw.githubusercontent.com/Neko250/sublime-PICO-8/master/img/screenshot.png)

This package includes:

- `.p8` language definition (by [Overkill](http://www.lexaloffle.com/bbs/?uid=11331)).
- Syntax highlighting (by [Overkill](http://www.lexaloffle.com/bbs/?uid=11331)).
- PICO-8 `.ttf` font (by [RhythmLynx](http://www.lexaloffle.com/bbs/?uid=11704)).

To-Do:

- Snippet integration based on the official PICO-8 API.
- Add a build system to run the cartridges from Sublime Text.

## Installation

Independently of the installation method you chose, after installing, navigate to the package folder and manually install `PICO-8.ttf` to your system fonts.

Alternatively, you can also download the font from this link: [PICO-8 TrueType font](https://raw.githubusercontent.com/Neko250/sublime-PICO-8/master/font/PICO-8.ttf).

### Using [Package Control](https://packagecontrol.io/)

1. Open the command palette:
	- Linux: `ctrl+shift+p`
	- Mac OS: `cmd+shift+p`
	- Windows: `ctrl+shift+p`
1. Run `Package Control: Install Package` command.
1. Search for `PICO-8` and install it.
1. Restart Sublime Text (if required).

### Using Git

Linux users:

```bash
cd ~/.config/sublime-text-3/Packages
rm -rf PICO-8
git clone https://github.com/Neko250/sublime-PICO-8 PICO-8
```

Mac OS users:

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
rm -rf PICO-8
git clone https://github.com/Neko250/sublime-PICO-8 PICO-8
```

Windows users:

```cmd
cd "%APPDATA%\Sublime Text 3\Packages"
rd /s /q PICO-8
git clone https://github.com/Neko250/sublime-PICO-8 PICO-8
```

### Manual installation

1. Download the files using the GitHub `.zip` download option.
1. Unzip the files and rename the folder to `PICO-8`.
1. Find your `Packages` directory:
	- Linux: `~/.config/sublime-text-3/Packages`
	- Mac OS: `~/Library/Application Support/Sublime Text 3/Packages`
	- Windows: `%APPDATA%\Sublime Text 3\Packages`
1. Copy the folder into your Sublime Text `Packages` directory.

## Version history

- __v1.1.0__:
	- `added`: installation message

- __v1.0.0__:
	- `added`: `.p8` language definition.
	- `added`: syntax highlighting.
	- `added`: PICO-8 TrueType font.
