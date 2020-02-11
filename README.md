# Sublime PICO-8

PICO-8 plugin for the [Sublime Text 3](https://www.sublimetext.com/) editor.

![sublime-PICO-8](https://raw.githubusercontent.com/sparr/sublime-PICO-8/master/img/screenshot.png)

This package includes:

- `.p8` language definition (originally by [Overkill](http://www.lexaloffle.com/bbs/?uid=11331)).
- Syntax highlighting (originally by [Overkill](http://www.lexaloffle.com/bbs/?uid=11331)).
- PICO-8 `.ttf` font (by [RhythmLynx](http://www.lexaloffle.com/bbs/?uid=11704)).
- Cartridge runner to launch your cart right from Sublime Text.
- Code completion based on the official [PICO-8 API](http://pico-8.github.io/pico8-api/).
- Code snippets.

----

## Installation

### Using [Package Control](https://packagecontrol.io/)

1. Open the command palette with `ctrl+shift+p` (`cmd+shift+p` in OSX).
1. Run `Package Control: Install Package` command.
1. Search for `PICO-8` and install it.
1. Restart Sublime Text.

### Using Git

#### Linux

```bash
cd ~/.config/sublime-text-3/Packages
rm -rf PICO-8
git clone https://github.com/sparr/sublime-PICO-8 PICO-8
```

#### OSX

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
rm -rf PICO-8
git clone https://github.com/sparr/sublime-PICO-8 PICO-8
```

#### Windows

```bash
cd "%APPDATA%\Sublime Text 3\Packages"
rd /s /q PICO-8
git clone https://github.com/sparr/sublime-PICO-8 PICO-8
```

### Manual Installation

1. Download the files using the GitHub `.zip` download option.
1. Unzip the files and rename the folder to `PICO-8`.
1. Find your `Packages` directory:
	- Linux: `~/.config/sublime-text-3/Packages`
	- Mac OS: `~/Library/Application Support/Sublime Text 3/Packages`
	- Windows: `%APPDATA%\Sublime Text 3\Packages`
1. Copy the folder into your Sublime Text `Packages` directory.

----

## Post Installation

### Font Setup

Independently of the installation method you chose, after installing you'll need to setup the PICO-8 font.

1. Open the command palette with `ctrl+shift+p` (`cmd+shift+p` in OSX).
1. Run `PICO-8: Download Font` command.
1. Find `PICO-8.ttf` in your downloads folder and install it.
1. Restart Sublime Text.

Test different font sizes until you find one that goes well with your screen resolution !

### Cartridge Runner Setup

To setup the Cartridge Runner, open the Command Palette in Sublime Text (ctrl+shift+p / cmd+shift+p) and run "PICO-8: Setup PICO-8 Path".
Then enter the path to PICO-8 in the prompt input.

1. Open the command palette with `ctrl+shift+p` (`cmd+shift+p` in OSX).
1. Run `PICO-8: Setup PICO-8 Path` command.
1. Type the path to your PICO-8 executable. Defaults to:
	- Linux: `/there/is/no/default/in/linux/shrug/pico8`
	- OSX: `/Applications/PICO-8.app/Contents/MacOS/pico8`
	- Windows: `C:\\Program Files (x86)\\PICO-8\\pico8.exe`

__IMPORTANT__: Remember using the escape character for the backslash (`\\`) instead of a single one (`\`) in Windows !!!

----


## Version History

- __v2020.02.10__:
	- Initial fork and merge of Sublime PICO-8 and LuaExtended
	- Remove inapplicable LuaExtended parts
	- `added`: Add `goto` to list of completion keywords
	- `added`: Add support for block comments
	- `added`: Additional completion cancel triggers
	- `changed`: Rearrange files from both sources
	- `changed`: Reformat CDATA in snippets
	- `fixed`: Restrict snippet/completion/etc scopes, exclude strings, comments, non-lua sections
	- `removed`: Disable completion of `count()` and mapdraw`()`, both deprecated

- __v2017.3.14__:
	- `added`: automatically lowercase the file upon saving.
	- `added`: `extcmd` function (syntax and autocomplete).
	- `added`: raspberry pi / pocketchip gpio snippet.
	- `added`: `forpairs` block snippet.
	- `added`: `repeat-until` block snippet.
	- `added`: `goto` block snippet.
	- `added`: semantic comments inside block snippets.
	- `changed`: updated api autocompletions to match PICO-8 0.1.10.
	- `changed`: `forin` block snippet renamed to `forall`.
	- `fixed`: hex number highlighting when not preceded by space.
	- `fixed`: comment start definition (`Toggle Comment` from the Command Palette).

- __v2016.7.1__:
	- `added`: `.no-sublime-package`.
	- `changed`: package is no longer compressed.
	- `fixed`: cartridge runner is now visible to sublime.

- __v2016.6.30__:
	- `added`: command palette download font shortcut: `PICO-8: Download Font`.
	- `added`: command palette preferences: `Preferences: PICO-8 - Default` & `Preferences: PICO-8 - User`.
	- `added`: command palette bbs shortcut: `PICO-8: Browse BBS`.
	- `added`: command palette API reference shortcut: `PICO-8: Browse API Reference`.
	- `added`: `highlight_line` setting defaults to `true`.
	- `added`: menu items to open preferences files: `Preferences > Package Settings > PICO-8`.
	- `changed`: version system changed to tagging date.
	- `changed`: theme's line highlight is now a bit brighter than the background.
	- `fixed`: setup cartridge runner from the command palette: `PICO-8: Setup PICO-8 Path`.
	- `fixed`: run cartridges from the command palette: `PICO-8: Run Cartridge`.
	- `removed`: old build system: `PICO-8.sublime-build`.

- __v0.1.8__:
	- `added`: snippet library.
	- `added`: code completion.
	- `changed`: changed version to match PICO-8.
	- `fixed`: completed `.tmLanguage` functions.

- __v0.0.3__:
	- `removed`: `.no-sublime-package`.

- __v0.0.2__:
	- `added`: build system.
	- `changed`: installation message.
	- `changed`: font size no longer predefined.
	- `changed`: caret width no longer predefined.

- __v0.0.1__:
	- `added`: installation message.

- __v0.0.0__:
	- `added`: `.p8` language definition.
	- `added`: syntax highlighting.
	- `added`: PICO-8 TrueType font.
