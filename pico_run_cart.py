import sublime
import sublime_plugin
import subprocess
import threading

class PicoRunCartCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def target():
			subprocess.Popen(self.cmd, bufsize=-1, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

		pico8 = "\"" + self.view.settings().get("pico-8_path", "undefined") + "\""
		if pico8 == "undefined":
			sublime.error_message("Error: \"pico-8_path\" is not defined !\n\nRun \"PICO-8: Setup Path\" from the Command Palette.")
			return

		cart = "\"" + self.view.file_name() + "\""
		self.cmd = pico8 + " -run " + cart
		threading.Thread(target=target).start()
