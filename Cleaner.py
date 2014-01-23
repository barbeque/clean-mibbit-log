import sublime, sublime_plugin, re

# Designed to clean up mibbit logs to look more normal
class CleanMibbitLogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# grab everything from the current buffer...
		reg = sublime.Region(0, self.view.size())
		# split it up by lines... but i'm not really sure if it actually does this
		lines = self.view.split_by_newlines(reg)
		for lineRegion in lines:
			# why do i have to do this twice?
			# maybe because the buffer changed since the last time i called this region...
			# ... so the absolute character position is wrong again.
			# this SHOULD work properly by getting the line that contains the region.
			realLineRegion = self.view.line(lineRegion)
			text = self.view.substr(realLineRegion)
			timestampsStripped = self.removeTimestamps(text)
			usernamesReformatted = self.formatUsernames(timestampsStripped)
			# replace the buffer with the results.
			self.view.replace(edit, realLineRegion, usernamesReformatted)
	def removeTimestamps(self, logText):
		# replace [0-9]+:[0-9]+\t with nothing
		return re.sub('^[0-9]+:[0-9]+\t', '', logText)
	def formatUsernames(self, logText):
		# replace [A-z]+\t, putting brackets about.
		# raw strings (the r'') are very important here.
		return re.sub('([A-z]+)\t', r'<\1> ', logText)

