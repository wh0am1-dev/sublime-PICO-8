import sublime
import sublime_plugin

class PicoToLower(sublime_plugin.TextCommand):
	def run(self, edit):
		upper = self.view.find_all("[A-Z]+")
		for region in upper:
			self.view.replace(edit, region, self.view.substr(region).lower())

class PicoOnSave(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		syntax = view.settings().get("syntax")
		if "PICO-8" in syntax:
			view.run_command("pico_to_lower")
