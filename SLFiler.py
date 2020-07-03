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
from typing import Dict, List, Any, Union, Hashable
import os
import yaml
from SLFilerLL import SLFilerLL


class SLFiler:

	def __init__(self):

		self.read_from_file = 'r'
		self.write_to_file = 'w'
		self.comma = ','
		self.comma_substitution_char = ';'
		self.file_newline = '\n'
		self.append_mode = 'a'
		self.main_dict = None
		self.low_level = SLFilerLL()
		dir_path = os.environ['LOCALAPPDATA'] + '\\Seanslist'
		if not os.path.isdir(dir_path):
			# print('The directory is not present. Creating a new one..')
			os.mkdir(dir_path)
		# else:
			# print('The directory is present.')

	def get_last_line_in_achievements(self, achievements, filename):
		try:
			return self.low_level.get_last_line(filename)
		except FileNotFoundError:
			try:
				self.low_level.copy_file_base_to_local(achievements, filename)
				return self.low_level.get_last_line(filename)
			except:
				print("failed copying achievements")
				return ""

	def get_my_lists(self, filename, validation_string):
		my_lists = []
		i = 0
		with self.low_level.open_file_read(filename) as f:
			for line in f:
				if line.startswith("#"):  # is a comment
					continue
				if i == 0:
					if line.strip() == validation_string:
						i = i + 1
						continue
					print("Not a valid my lists file, expected v0.1")
					break
				else:
					new_list = []
					words = line.split(self.comma)
					for w in words:
						# hydrate the substitute char back to a comma
						w = w.replace(self.comma_substitution_char, self.comma)
						# remove whitespace
						x = w.strip()
						# don't append blanks
						if x != "":
							new_list.append(x)
						i = i + 1
					my_lists.append(new_list)
		return my_lists

	def save_values(self, changed_dic, filename, file_version, backups):
		self.backup_files(filename, backups)
		old_key = ""
		for key in changed_dic:
			if len(changed_dic[key]) == 1:
				p = changed_dic[key][0]
				if p == "remove0evomer":
					self.main_dict.pop(key)
					old_key = key
				else:
					self.main_dict[key] = changed_dic[key]
			else:
				self.main_dict[key] = changed_dic[key]
		if old_key != "":
			changed_dic.pop(old_key)
		with self.low_level.open_file_write(filename) as f:
			f.write("My Lists v0.1")
			f.write(self.file_newline)
			for key in self.main_dict:
				method = "Local,"
				f.write(method)
				f.write(key)
				# c = len(self.main_dict[key])
				if key == "My Lists":
					for w in changed_dic:
						f.write(self.comma)
						f.write(w.replace(self.comma, self.comma_substitution_char).strip())
					f.write(self.file_newline)
				else:
					for w in self.main_dict[key]:
						f.write(self.comma)
						f.write(w.replace(self.comma, self.comma_substitution_char).strip())
					f.write(self.file_newline)
		return 0

	def backup_files(self, filename, backups):
		backup_files = []
		backup_files.insert(0, filename)
		for backup_file in backups:
			backup_files.insert(0, backup_file)
		file1 = ""
		for file_name in backup_files:
			file2 = file1
			file1 = file_name
			# copy the second-to-last file to the last file, etc.
			# but if the file is not found, then it is probably
			# the first time, so copy the current file to all the backup
			# file names
			try:
				if file2 != "":
					self.low_level.copy_file_local_to_local(file1, file2)
			except FileNotFoundError:
				for backup_file in backups:
					self.low_level.copy_file_local_to_local(filename, backup_file)
				break
		return 0

	def append_values_to_file(self, ll, filename):
		with self.low_level.open_file_append(filename) as f:
			next_comma = ","
			for word in ll:
				if word == "\n":
					f.write(self.file_newline)
					next_comma = ""
				else:
					word = word.strip()
					if next_comma != "":
						f.write(self.comma)
					f.write(word.replace(self.comma, self.comma_substitution_char))
					next_comma = ","
		return 0

	def copy_file_base_to_local(self, base_filename, filename):
		self.low_level.copy_file_base_to_local(base_filename, filename)

	def make_my_lists(self, my_filename):
		self.copy_file_base_to_local('my_lists.txt', my_filename)

	def get_main_dict(self, my_lists_filename, my_lists_version, all_list):
		my_lists = []
		try:
			my_lists = self.get_my_lists(my_lists_filename, my_lists_version)
		except FileNotFoundError:
			self.make_my_lists(my_lists_filename)
			my_lists = self.get_my_lists(my_lists_filename, my_lists_version)
		except:
			print('get_main_dict unhandled exception')
		d_my_lists = {}
		all_list_keys = []
		# get the retrieval type for each list
		for l1 in my_lists:
			if l1.pop(0) != "Local":
				continue  # for future feature
			key = l1.pop(0)
			d_my_lists[key] = l1
			all_list_keys.append(key)
		d_my_lists[all_list] = all_list_keys
		return d_my_lists

	def check_config(self, filename):
		backup_filename = filename + ".bak"
		try:
			self.low_level.copy_file_local_to_local(filename, backup_filename)
		except FileNotFoundError:
			print('warning: file does not exist')
			return False
		file = filename
		with self.low_level.open_file_read(file) as f:
			for word in f:
				filename = word
				break
		backup_filename = filename + ".bak"
		try:
			self.low_level.copy_file_local_to_local(filename, backup_filename)
		except FileNotFoundError:
			# file doesn't exist
			print(filename + ', ' + backup_filename + ' do not exist')
			return False
		return True

	def dump_yaml(self, filename, dict_file):
		with self.low_level.open_file_write(filename) as file:
			documents = yaml.dump(dict_file, file)
		return documents

	def load_config_yaml(self):
		owner_name1 = self.get_owner()
		_cache_list: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = None
		filename = owner_name1 + "_config.yaml"
		with self.low_level.open_file_read(filename) as f:
			_cache_list = yaml.load(f, yaml.FullLoader)
		return _cache_list

	def get_owner(self):
		_owner: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = None
		filename = r'config.yaml'
		with self.low_level.open_file_read(filename) as f:
			_owner = yaml.load(f, yaml.FullLoader)
			owner_name = _owner["owner"]
		return str(owner_name)
