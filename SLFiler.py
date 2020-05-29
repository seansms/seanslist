#    Sean's SuperList - A to-do and general list manager.
#    Copyright (C) 2020  Sean Shannon
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import logging
import shutil

from SLControl import SLControl


class SLFiler:

	def __init__(self):
		self.backups = SLControl.my_lists_backups
		self.comma_substitution_char = SLControl.comma_substitution_char.replace(",", ";")
		self.main_dict = None

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
				if line.startswith("#"):  # is a comment
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

	def save_values(self, changed_dic, filename, file_version):
		self.backup_files(filename, file_version)
		if __debug__:
			logging.info("creating new my_list " + filename)
		for key in changed_dic:
			self.main_dict[str(key).strip()] = changed_dic[key]
		with open(filename, SLControl.write_to_file) as f:
			f.write("My Lists v0.1")
			f.write(SLControl.file_newline)
			for key in self.main_dict:
				method = "Local,"
				f.write(method)
				f.write(str(key).strip())
				c = len(self.main_dict[key])
				for w in self.main_dict[key]:
					f.write(SLControl.comma)
					f.write(w.replace(SLControl.comma, self.comma_substitution_char).strip())
				f.write(SLControl.file_newline)
		return 0

	def backup_files(self, filename, file_version):
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
					word = word.strip()
					if next_comma != "":
						f.write(SLControl.comma)
					f.write(word.replace(SLControl.comma, self.comma_substitution_char))
					next_comma = ","
		return 0

	def get_main_dict(self):
		my_lists = self.get_my_lists(SLControl.my_lists_filename, SLControl.my_lists_version)
		d_my_lists = {}
		all_list_keys = []
		# get the retrieval type for each list
		for l1 in my_lists:
			if l1.pop(0) != "Local":
				continue  # for future feature
			key = l1.pop(0)
			d_my_lists[key] = l1
			all_list_keys.append(key)
		d_my_lists[SLControl.AllList] = all_list_keys
		return d_my_lists
