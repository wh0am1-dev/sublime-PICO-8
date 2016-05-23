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
