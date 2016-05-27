# What is this?
LuaExtended is a syntax definition and snippet package for Sublime Text 3 (it should theoretically work with ST2 as well, but I didn't test it).

# Features
As of right now, LuaExtended contains the following improvements over the default Lua package:

* Indentation of `repeat until` loops fixed
* Indentation of table definitions fixed
* Improved syntax definition structure for easier future work on more fixes
* `error` calls have red-highlighted strings
* Completions include the full standard library, including parameter names with tab stops
* Completions also include Lua keywords 
* New snippets:
	* New loop snippets (`while` and `repeat`)
	* Improved indentation of `for` snippets
	* `++` (expands the current line into the form of `line = line + 1`, ignoring inline comments and whitespace)
	* `+=` and `-=` 
	* `dfun`, an LDoc-style documented function snippet
	* `if`, `elseif` and `else`
	* `if~`, `if=`, and their `elseif` counterparts, expanding to `if x ~= y then ...` and similar
	* Most snippets also handle selection, meaning you can e.g. apply `while` on a block of code which will then become the body of the `while` loop
* Function calls (including object method invocations `foo:bar()`) are highlighted properly
* Restructured indent settings
	* `do end` blocks are indented properly
* All features are grouped under the `source.luae` scope, so that they don't interfere with the default Lua package

# Installation
Simply clone this repository into your `Data/User` folder (either in the install directory, in `%appdata%/Sublime Text 3` on Windoze, or wherever else other environments put it).

# LuaExtended and Linters
If you are using a SublimeLinter3-based linter such as [SublimeLinter-lua](https://github.com/SublimeLinter/SublimeLinter-lua), you will need to edit it manually to get LuaExtended linting work.

Start with locating the linter's package file in `C:\Users\<username>\AppData\Roaming\Sublime Text 3\Installed Packages`, and opening it with an archive manager such as 7Zip (`sublime-package` files are in fact Zip archives).

![](https://i.imgur.com/a3YrGjo.png)

If you haven't already, set the View/Edit functions of 7Zip to use your favourite editor. Go to Tools/Options, click on the Editor tab and browse for your editor's executable. Then accept the changes with OK.

![](https://i.imgur.com/FPbi066.png) 

Finally right-click the linter.py file in the archive's root and select "Edit".

![](https://i.imgur.com/iCU6p7C.png)

Once in Sublime Text, locate the line that says `syntax = 'lua'`, and change it to `syntax = ('lua', 'luaextended')`. This will ensure the Lua syntax is still linted, and LuaExtended as well.  

![](https://i.imgur.com/W2ldXl2.png)

Save the changes. 7Zip will ask you whether to apply the changes to the archive, select "Yes".

And there you go! Try opening a `*.luae`, `*.ext.lua` or `*.extended.lua` file and see whether linting works. If it for some reason doesn't work, read the tutorial again and check that you've followed it to the point. Sometimes, 7Zip will fail to notice the file has changed after saving it in the editor, but you can always extract the whole archive, edit it and then pack it as a Zip again.
