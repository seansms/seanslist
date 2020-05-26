import yaml
import shutil
import os

file_name = "config.yaml"
if os.path.exists(file_name):
    print("A config.yaml file exists, do you want to continue? 1=Yes")
    x = input()
    if x != '1':
       exit()
    shutil.copyfile("config.yaml", "config.yaml.bak")

print("What is the owner name [default=my]?")
x = input()
owner_name = "my"
if x.strip() != "":
    owner_name = x.strip()

my_file = {'my_lists_filename': owner_name + '_lists.txt'}
my_file_backups = [owner_name + "_lists2.txt", owner_name + "_lists3.txt", owner_name + "_lists4.txt"]
my_achievements_file = {'my_achievements_file' : owner_name + "_achievements.txt"}
dict_file = [my_file,
# File names for your backups limit to 99
             {'my_lists_backups':my_file_backups},
# this will substitute a comma in a word
             {'comma_substitution_char':";"},
# this will perform comma substitution if True
             {'perform_comma_substitution':True},
# this is a comma, used for word separator
             {'comma' : ","},
# this is the control flag for reading a file
             {'read_from_file' : "r"},
# this is the control flag for writing to a file
             {'write_to_file' : "w"},
# file to save achievements to
             my_achievements_file,
# frame title, i.e. the owner of these lists
             {'owner_name' : owner_name},
# append mode (binary)
             {'append_mode' : "a"},
# my lists file format version
             {'my_lists_version' :  "My Lists v0.1"},
# all lists name in the mylists file
             {'AllList' : "all_list_names" }]

with open(r'config.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)

print ('File config.yaml created.')

#create the lists file and backups if they don't exist
for k, v in my_file.items():
    if not os.path.exists(v):
        shutil.copyfile("my_lists.txt", v)

for f in my_file_backups:
    if not os.path.exists(f):
        shutil.copyfile("my_lists.txt", f)

for k, v in my_achievements_file.items():
    if not os.path.exists(v):
        shutil.copyfile("my_achievements.txt", v)

