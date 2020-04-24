import logging
import shutil

from SLControl import SLControl


class SLFiler:

	def __init__(self):
		self.backups = SLControl.my_lists_backups
		self.comma_substitution_char = SLControl.comma_substitution_char.replace(",", ";")

#unused
	def print_words(self, filename):
		with open(filename, SLControl.read_from_file) as f:
			for line in f:
				words = line.split(SLControl.comma)
				for w in words:
					print(w)
				print()

	def get_last_line(self, filename):
		last_line = ""
		with open(filename, SLControl.read_from_file) as f:
			for line in f:
				last_line = line
		return last_line

	def get_my_lists(self, filename, validation_string):
		my_lists = []
		i = 0
		with open(filename, SLControl.read_from_file) as f:
			for line in f:
				if line.startswith("#"): # is a comment
					continue
				if i == 0:
					if line.strip() == validation_string:
						i = i + 1
						continue
					print("Not a valid my lists file, expected v0.0")
					break
				else:
					new_list = []
					words = line.split(SLControl.comma)
					for w in words:
						#hydrate the substitute char back to a comma
						w = w.replace(self.comma_substitution_char, SLControl.comma)
						#remove whitespace
						x = w.strip()
						#don't append blanks
						if x != "":
							new_list.append(x)
						i = i + 1
					my_lists.append(new_list)
		return my_lists


#unused
	@staticmethod
	def print_lists(my_lists):
		for next_list in my_lists:
			for word in next_list:
				print(word)
			print()

	def save_values(self, ll, filename, file_version):
		file_names = []
		if __debug__:
			logging.info("creating backups")
		file_names.insert(0, filename)
		for file_name in self.backups:
			file_names.insert(0, file_name)
		file1 = ""
		file2 = ""
		for file_name in file_names:
			file2 = file1
			file1 = file_name
			if file2 != "":
				shutil.copyfile(file1, file2)

		if __debug__:
			logging.info("creating new my_list " + filename)

		with open(filename, SLControl.write_to_file) as f:
			f.write(file_version + SLControl.file_newline)
			for lw in ll:
				c = len(lw)
				c = c - 1
				for ww in lw:
					#substitute for commas
					f.write(ww.replace(SLControl.comma, self.comma_substitution_char))
					if c > 0:  # if not the last word, put a comma
						f.write(SLControl.comma)
						c = c - 1
				f.write(SLControl.file_newline)
		return 0

	def append_values_to_file(self, l, filename, mode = SLControl.append_mode):
		if __debug__:
			logging.info("saving backups")

		if __debug__:
			logging.info("creating new file " + filename)

		with open(filename, mode) as f:
			next_comma = ","
			for word in l:
				if word == "\n":
					f.write(SLControl.file_newline)
					next_comma = ""
				else:
					if next_comma != "":
						f.write(SLControl.comma)
					f.write(word.replace(SLControl.comma, self.comma_substitution_char))
					next_comma = ","
		return 0

