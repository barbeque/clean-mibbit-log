import sublime, sublime_plugin, re

# Designed to clean up mibbit logs to look more normal
class CleanMibbitLogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# grab everything from the current buffer...
		reg = sublime.Region(0, self.view.size())
		# split it up by lines... but i'm not really sure if it actually does this
		lineRegions = self.view.split_by_newlines(reg)
		# copy into a buffer of strings
		lines = map(lambda r: self.view.substr(r), lineRegions)
		editedLines = []
		for text in lines:
			timestampsStripped = self.removeTimestamps(text)
			usernamesReformatted = self.formatUsernames(timestampsStripped)
			editedLines.append(usernamesReformatted)
		# now write it back in
		finishedBuffer = '\n'.join(editedLines)
		self.view.replace(edit, reg, finishedBuffer)
	def removeTimestamps(self, logText):
		# replace [0-9]+:[0-9]+\t with nothing
		return re.sub('^[0-9]+:[0-9]+\t', '', logText)
	def formatUsernames(self, logText):
		# replace [A-z\S]+\t, putting brackets about.
		# raw strings (the r'') are very important here.
		return re.sub('([A-z\S]+)\t', r'<\1> ', logText)

