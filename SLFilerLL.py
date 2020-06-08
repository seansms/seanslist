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
import shutil
import os
import yaml


class SLFilerLL:

	def __init__(self):
		self.read_from_file = 'r'
		self.write_to_file = 'w'
		self.comma = ','
		self.comma_substitution_char = ';'
		self.file_newline = '\n'
		self.append_mode = 'a'
		self.main_dict = None
		dir_path = os.environ['LOCALAPPDATA'] + '\\Seanslist'
		if not os.path.isdir(dir_path):
			# print('The directory is not present. Creating a new one..')
			os.mkdir(dir_path)
		# else:
			# print('The directory is present.')

	@staticmethod
	def prepare_filename(filename):
		local_folder = 'seanslist'
		local_app_data = os.environ['LOCALAPPDATA']
		if local_folder in filename:
			if local_app_data in filename:
				return filename
		writable_file = os.path.join(local_app_data, local_folder, filename)
		return writable_file

# unused
	def print_words(self, filename1):
		filename = self.prepare_filename(filename1)
		with open(filename, self.read_from_file) as f:
			for line in f:
				words = line.split(self.comma)
				for w in words:
					print(w)
				print()

	def get_last_line(self, filename1):
		filename = self.prepare_filename(filename1)
		with open(filename, self.read_from_file) as f:
			for line in f:
				last_line = line
		return last_line

	def copy_file_base_to_local(self, base_file, local_file):
		filename = self.prepare_filename(local_file)
		shutil.copyfile(base_file, filename)

	def open_file_read(self, filename1):
		filename = self.prepare_filename(filename1)
		return open(filename, self.read_from_file)

	def open_file_write(self, filename1):
		filename = self.prepare_filename(filename1)
		return open(filename, self.write_to_file)

	def open_file_append(self, filename1):
		filename = self.prepare_filename(filename1)
		return open(filename, self.append_mode)

	# unused
	@staticmethod
	def print_lists(my_lists):
		for next_list in my_lists:
			for word in next_list:
				print(word)
			print()

	def copy_file_local_to_local(self, file1, file2):
		filename1 = self.prepare_filename(file1)
		filename2 = self.prepare_filename(file2)
		shutil.copyfile(filename1, self.prepare_filename(filename2))

	def save_values(self, changed_dic, filename1, file_version, backups):
		self.backup_files(filename1, file_version, backups)
		filename = self.prepare_filename(filename1)
		for key in changed_dic:
			self.main_dict[str(key).strip()] = changed_dic[key]
		with open(filename, self.write_to_file) as f:
			f.write("My Lists v0.1")
			f.write(self.file_newline)
			for key in self.main_dict:
				method = "Local,"
				f.write(method)
				f.write(str(key).strip())
				# c = len(self.main_dict[key])
				for w in self.main_dict[key]:
					f.write(self.comma)
					f.write(w.replace(self.comma, self.comma_substitution_char).strip())
				f.write(self.file_newline)
		return 0



	def backup_files(self, filename1, file_version, backups):
		print("file version:", file_version)
#		filename = self.prepare_filename(filename1)
		file_names = []
		file_names.insert(0, filename1)
		for file_name in backups:
			file_names.insert(0, file_name)
		file1 = ""
		for file_name in file_names:
			file2 = file1
			file1 = file_name
			try:
				if file2 != "":
					shutil.copyfile(file1, file2)
			except FileNotFoundError:
				for file_name1 in backups:
					shutil.copyfile(filename, self.prepare_filename(file_name1))
				break
		return 0

	def append_values_to_file(self, ll, filename1, mode='a'):
		filename = self.prepare_filename(filename1)
		with open(filename, mode) as f:
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

	def make_my_lists(self, my_filename):
		filename = self.prepare_filename(my_filename)
		shutil.copyfile('my_lists.txt', filename)

	def get_main_dict(self, my_lists_filename, my_lists_version, all_list):
		try:
			my_lists = self.get_my_lists(my_lists_filename, my_lists_version)
		except FileNotFoundError:
			self.make_my_lists(my_lists_filename)
			my_lists = self.get_my_lists(my_lists_filename, my_lists_version)
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

	def check_config(self, file_name):
		file = self.prepare_filename(file_name)
		try:
			shutil.copyfile(file, file+".bak")
		except FileNotFoundError:
			print('warning: file does not exist')
			return False

		with open(file, self.read_from_file) as f:
			for word in f:
				filename = word
				break
		file = filename
		file = self.prepare_filename(file)
		try:
			shutil.copyfile(file, file+".bak")
		except FileNotFoundError:
			# file doesn't exist
			return False
		return True

	def dump_yaml(self, filename, dict_file):
		param = self.prepare_filename(filename)
		with open(param, 'w') as file:
			documents = yaml.dump(dict_file, file)
		return documents

	def load_config_yaml(self):
		owner_name1 = self.get_owner()
		_cache_list: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = None
		file_name2 = owner_name1 + "_config.yaml"
		file_name2 = self.prepare_filename(file_name2)
		with open(file_name2) as file2:
			_cache_list = yaml.load(file2, yaml.FullLoader)
		return _cache_list

	def get_owner(self):
		_owner: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = None
		file_name = r'config.yaml'
		file_name = self.prepare_filename(file_name)
		with open(file_name) as file1:
			_owner = yaml.load(file1, yaml.FullLoader)
			owner_name = _owner["owner"]
		return str(owner_name)
