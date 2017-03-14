import sublime
import sublime_plugin

class PicoSetupPathCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def done(path):
			settings = sublime.load_settings("PICO-8.sublime-settings")
			settings.set("pico-8_path", path)
			sublime.save_settings("PICO-8.sublime-settings")
			return

		platform = sublime.platform()
		if platform == "linux":
			self.view.window().show_input_panel("PICO-8 Path", "/path/to/pico8", done, None, None)
		elif platform == "osx":
			self.view.window().show_input_panel("PICO-8 Path", "/path/to/PICO-8.app/Contents/MacOS/pico8", done, None, None)
		elif platform == "windows":
			self.view.window().show_input_panel("PICO-8 Path", "C:\\Program Files (x86)\\PICO-8\\pico8.exe", done, None, None)
		else:
			sublime.error_message("Error: could not resolve platform\n\n[\"linux\", \"osx\", \"windows\"]")
			return
