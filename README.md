# Sublime PICO-8

PICO-8 plugin for the [Sublime Text 3](https://www.sublimetext.com/) editor.

![sublime-PICO-8](https://raw.githubusercontent.com/Neko250/sublime-PICO-8/master/img/screenshot.png)

This package includes:

- `.p8` language definition (by [Overkill](http://www.lexaloffle.com/bbs/?uid=11331)).
- Syntax highlighting (by [Overkill](http://www.lexaloffle.com/bbs/?uid=11331)).
- PICO-8 `.ttf` font (by [RhythmLynx](http://www.lexaloffle.com/bbs/?uid=11704)).
- Build system to run the cartridges from Sublime Text.

To-Do:

- Snippet integration based on the official PICO-8 API.

## Installation

### Using [Package Control](https://packagecontrol.io/)

1. Open the command palette with `ctrl+shift+p` (`cmd+shift+p` in OSX).
1. Run `Package Control: Install Package` command.
1. Search for `PICO-8` and install it.
1. Restart Sublime Text (if required).

### Using Git

#### Linux

```bash
cd ~/.config/sublime-text-3/Packages
rm -rf PICO-8
git clone https://github.com/Neko250/sublime-PICO-8 PICO-8
```

#### OSX

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
rm -rf PICO-8
git clone https://github.com/Neko250/sublime-PICO-8 PICO-8
```

#### Windows

```bash
cd "%APPDATA%\Sublime Text 3\Packages"
rd /s /q PICO-8
git clone https://github.com/Neko250/sublime-PICO-8 PICO-8
```

### Manual Installation

1. Download the files using the GitHub `.zip` download option.
1. Unzip the files and rename the folder to `PICO-8`.
1. Find your `Packages` directory:
	- Linux: `~/.config/sublime-text-3/Packages`
	- Mac OS: `~/Library/Application Support/Sublime Text 3/Packages`
	- Windows: `%APPDATA%\Sublime Text 3\Packages`
1. Copy the folder into your Sublime Text `Packages` directory.

## Font

Independently of the installation method you chose, after installing you'll need to install the PICO-8 font. You can download the font from this link: [PICO-8.ttf](https://raw.githubusercontent.com/Neko250/sublime-PICO-8/master/font/PICO-8.ttf).

## Build System

To use the build system included with the package follow this instructions:

### Linux

Execute this command in the terminal:

```bash
sudo ln -s /path/to/your/pico8 /usr/local/bin
```

### OSX

Execute this command in Terminal.app:

```bash
sudo ln -s /path/to/your/PICO-8.app/Contents/MacOS/pico8 /usr/local/bin
```

### Windows

1. Navigate to: `Control Panel > System > Advanced System Settings > Environment Variables`.
1. Edit the `Path` variable under `User variables`.
1. Add your PICO-8 installation path (default: `C:\Program Files (x86)\PICO-8`).

## Version History

- __v1.2.1__:
	- `removed`: `.no-sublime-package`.

- __v1.2.0__:
	- `added`: build system.
	- `changed`: installation message.
	- `changed`: font size no longer predefined.
	- `changed`: caret width no longer predefined.

- __v1.1.0__:
	- `added`: installation message.

- __v1.0.0__:
	- `added`: `.p8` language definition.
	- `added`: syntax highlighting.
	- `added`: PICO-8 TrueType font.
