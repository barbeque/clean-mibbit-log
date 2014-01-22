import sublime, sublime_plugin, re

# Designed to clean up mibbit logs to look more normal
class CleanMibbitLogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# grab everything from the current buffer...
		reg = sublime.Region(0, self.view.size())
		text = self.view.substr(reg)
		# do our work to it
		timestampsStripped = self.removeTimestamps(text)
		usernamesReformatted = self.formatUsernames(timestampsStripped)
		# replace the buffer with the results.
		self.view.replace(edit, reg, usernamesReformatted)
	def removeTimestamps(self, logText):
		# replace [0-9]+:[0-9]+\t with nothing
		return re.sub('[0-9]+:[0-9]+\t', '', logText)
	def formatUsernames(self, logText):
		# replace [A-z]+\t, putting brackets about.
		# raw strings (the r'') are very important here.
		return re.sub('([A-z]+)\t', r'<\1> ', logText)

