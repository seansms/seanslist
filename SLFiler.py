import logging
import shutil

from SLControl import SLControl


class SLFiler:

	def __init__(self):
		self.filename = SLControl.my_lists_filename
		self.backups = SLControl.my_lists_backups
		self.comma_substitution_char = SLControl.comma_substitution_char.replace(",", ";")

#unused
	def print_words(self):
		with open(self.filename, SLControl.read_from_file) as f:
			for line in f:
				words = line.split(SLControl.comma)
				for w in words:
					print(w)
				print()

	def get_my_lists(self):
		my_lists = []
		with open(self.filename, SLControl.read_from_file) as f:
			for line in f:
				new_list = []
				words = line.split(SLControl.comma)
				for w in words:
					w = w.replace(self.comma_substitution_char, SLControl.comma)
					x = w.strip()
					if x != "":
						new_list.append(x)
				my_lists.append(new_list)
		return my_lists

#unused
	@staticmethod
	def print_lists(my_lists):
		for next_list in my_lists:
			for word in next_list:
				print(word)
			print()

	def save_values(self, ll):
		file_names = []
		file_names.insert(0, self.filename)
		for file_name in self.backups:
			file_names.insert(0, file_name)

		if __debug__:
			logging.info("creating backups")

		file1 = ""
		file2 = ""
		for file_name in file_names:
			file2 = file1
			file1 = file_name
			if file2 != "":
				shutil.copyfile(file1, file2)

		if __debug__:
			logging.info("creating new my_list")

		with open(self.filename, SLControl.write_to_file) as f:
			for lw in ll:
				for ww in lw:
					f.write(ww.replace(SLControl.comma, self.comma_substitution_char))
					f.write(SLControl.comma)
				f.write(SLControl.file_newline)
		return 0

	def save_values_to_file(self, ll, filename, mode = SLControl.write_to_file):
		if __debug__:
			logging.info("saving backups")

		if __debug__:
			logging.info("creating new file " + filename)

		with open(filename, mode) as f:
			for ww in ll:
				f.write(ww.replace(SLControl.comma, self.comma_substitution_char))
				f.write(SLControl.comma)
			f.write(SLControl.file_newline)
		return 0

