import sublime
import sublime_plugin

class PicoToLower(sublime_plugin.TextCommand):
	def run(self, edit):
		upper = self.view.find_all("(_ENV)|([A-Z]+)")
		for region in upper:
			s = self.view.substr(region)
			if s == "_ENV" or self.view.score_selector(region.a, "string") > 0:
				continue
			self.view.replace(edit, region, s.lower())

class PicoOnSave(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		syntax = view.settings().get("syntax")
		if "PICO-8" in syntax:
			if view.settings().get("pico-8_auto_lowercase", True):
				view.run_command("pico_to_lower")
