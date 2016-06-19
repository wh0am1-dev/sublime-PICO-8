# What is this?
LuaExtended is a syntax definition and snippet package for Sublime Text 3.

[![Package Control](https://img.shields.io/packagecontrol/dt/LuaExtended.svg?maxAge=2592000)](https://packagecontrol.io/packages/LuaExtended)
[![license](https://img.shields.io/github/license/viluon/LuaExtended.svg?maxAge=2592000)](https://github.com/viluon/LuaExtended/blob/master/LICENSE.md)
[![GitHub release](https://img.shields.io/github/release/viluon/LuaExtended.svg?maxAge=2592000)](https://github.com/viluon/LuaExtended/releases)
[![GitHub stars](https://img.shields.io/github/stars/viluon/LuaExtended.svg?style=social&label=Star&maxAge=2592000)](https://github.com/viluon/LuaExtended/stargazers)

# Features
As of right now, LuaExtended contains the following improvements over the default Lua package:

* Indentation of `repeat until` loops fixed

	![](https://i.imgur.com/mhi7Ok2.gif)
* Indentation of table definitions fixed

	![](https://i.imgur.com/4H0GnEA.gif)
* Improved syntax definition structure for easier future work on more fixes
* `error` calls have red-highlighted strings

	![](https://i.imgur.com/irGZUPb.png)
* Completions include the full standard library, including parameter names with tab stops

	![](https://i.imgur.com/QnIQyNG.gif)
* Completions also include Lua keywords 
* New snippets:
	* New loop snippets (`while` and `repeat`)

		![](https://i.imgur.com/ThhEdZX.gif)
	* Improved indentation of `for` snippets, synced variable name tab stops

		![](https://i.imgur.com/cKSW2ny.gif)
	* `++` (expands the current line into the form of `line = line + 1`, ignoring inline comments and whitespace)

		![](https://i.imgur.com/gbJ3969.gif)
	* `+=` and `-=`

		![](https://i.imgur.com/7gATWIz.gif)
	* `dfun`, an LDoc-style documented function snippet

		![](https://i.imgur.com/FVXVTb6.gif)
	* `if`, `elseif` and `else`

		![](https://i.imgur.com/xVoBQIQ.gif)
	* `if~`, `if=`, and their `elseif` counterparts, expanding to `if x ~= y then ...` and similar

		![](https://i.imgur.com/Yac7RFk.gif)
	* Most snippets also handle selection, meaning you can e.g. apply `while` on a block of code which will then become the body of the `while` loop
* Function calls (including object method invocations `foo:bar()` and syntactic sugar like `foo { bar }`) are highlighted properly

	![](https://i.imgur.com/kCJvy4j.png)
* Anonymous function definitions are highlighted properly (arguments are formatted)

	![](https://i.imgur.com/aOQZYE2.png)
* Restructured indent settings
	* `do end` blocks are indented properly

		![](https://i.imgur.com/0DG2QRe.gif)
* All features are grouped under the `source.luae` scope, so that they don't interfere with the default Lua package

# Installation
You can now use [Package Control](https://packagecontrol.io/) to install [LuaExtended](https://packagecontrol.io/packages/LuaExtended). Simply type "install" in the Command Palette (<kbd>Ctrl + Shift + P</kbd>) to [find](https://i.imgur.com/XnYlj0y.gif) the [`Package Control: Install Package`](https://packagecontrol.io/docs/usage) command. Wait for the repository lists to load

![](https://i.imgur.com/tyDRMgP.png)

and search for 'LuaExtended'. Alternatively, you can clone this repository into your `Data/User` folder (either in the install directory, in `%appdata%/Sublime Text 3` on Windoze, or wherever else other environments put it).

# LuaExtended and Linters
If you are using a SublimeLinter3-based linter such as [SublimeLinter-lua](https://github.com/SublimeLinter/SublimeLinter-lua), you will need to modify your settings to get LuaExtended linting to work.

Navigate to Preferences > Package Settings

![](https://i.imgur.com/CIiMwB6.png)

Find SublimeLinter in the list and open its "Settings - User"

![](https://i.imgur.com/8oWbfOI.png)

The settings file is of the JSON format, so look for the line that says `"syntax_map": {`

![](https://i.imgur.com/BYM6QYB.png)

You will need to add a binding that tells SublimeLinter to lint LuaExtended just like Lua. This is done by adding a line that says `"luaextended": "lua",`. Don't worry about the alphabetical order of the entries, SublimeLinter will sort them on next reload.

![](https://i.imgur.com/7LOKYXF.png)

And there you go! Try opening a `*.luae`, `*.ext.lua` or `*.extended.lua` file and see whether linting works. If it for some reason doesn't work, read the tutorial again and check that you've followed it to the point. Try restarting Sublime before opening an issue!
