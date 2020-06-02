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
import shutil
import os
import string
from SLFiler import SLFiler


class Initialize:

    def __init__(self):
        self.run_once = False
        self.filer = SLFiler()

    def initialized(self):
        file_name = "config.yaml"
        config_exists = self.filer.check_config(file_name)
        if not config_exists:
            x = self.setup()
            return x
        return True

    def setup(self):
        print("What is the owner name [default=my]? (less than 13 chars)")
        owner = input()
        return self.save_config(owner)

    def save_config(self, owner):
        x = self.validate(owner)
        owner_name = "my"
        if x != "":
            if len(x) < 13:
                owner_name = x.strip()
            if len(x) > 12:
                owner_name = x[0:12]
        dict_owner = {"owner": owner_name}
        self.filer.dump_yaml("config.yaml", dict_owner)
        return self.make_files(owner_name)

    def make_files(self, owner_name):
        my_file = {'my_lists_filename': owner_name + '_lists.txt'}
        my_file_backups = [owner_name + "_lists2.txt", owner_name + "_lists3.txt", owner_name + "_lists4.txt"]
        my_achievements_file = {'my_achievements_file': owner_name + "_achievements.txt"}
        dict_file = [my_file,
                     # File names for your backups limit to 99
                     {'my_lists_backups': my_file_backups},
                     # this will substitute a comma in a word
                     {'comma_substitution_char': ";"},
                     # this will perform comma substitution if True
                     {'perform_comma_substitution': True},
                     # this is a comma, used for word separator
                     {'comma': ","},
                     # this is the control flag for reading a file
                     {'read_from_file': "r"},
                     # this is the control flag for writing to a file
                     {'write_to_file': "w"},
                     # file to save achievements to
                     my_achievements_file,
                     # frame title, i.e. the owner of these lists
                     {'owner_name': owner_name},
                     # append mode (binary)
                     {'append_mode': "a"},
                     # my lists file format version
                     {'my_lists_version': "My Lists v0.1"},
                     # all lists name in the mylists file
                     {'AllList': "all_list_names"},
                     # the colors of the lists
                     {'color_lists_palette': 'default_palette'},
                     # palettes
                     {'available_palettes': ['default_palette', 'hotdog_palette', 'fresh_palette', 'pro_palette',
                                             'earth_palette', 'crisp_palette', 'system_palette', 'grey_palette',
                                             'surf_palette']},
                     {'default_palette': ['#375E97', '#FB6542', '#FFBB00', '#3F681C', 'white', 'black', 'black',
                                          'white']},
                     {'system_palette': ['#FF8080', '#FFFF80', '#80FF80', '#80FFFF', 'black', 'black', 'black',
                                         'black']},
                     {'grey_palette': ['#F0F0F0', '#A0A0A0', '#808080', '#303030', '#010101', '#010101', '#010101',
                                       '#F0F0F0']},
                     {'hotdog_palette': ['red', 'yellow', 'white', 'blue', 'black', 'black', 'black', 'white']},
                     {'fresh_palette': ['#F98866', '#FF420E', '#80BD9E', '#89DA59', 'black', 'black', 'black',
                                        'black']},
                     {'pro_palette': ['#90AFC5', '#336B87', '#2A3132', '#763626', 'white', 'white', 'white', 'white']},
                     {'earth_palette': ['#46211A', '#693D3D', '#BA5536', '#A43820', 'white', 'white', 'white',
                                        'white']},
                     {'crisp_palette': ['#505160', '#68829E', '#AEBD38', '#598234', 'white', 'white', 'white',
                                        'white']},
                     {'surf_palette': ['#F4CC70', '#DE7A22', '#20948B', '#6AB187', 'black', 'white', 'white', 'black']}]

        documents = self.filer.dump_yaml(owner_name + '_config.yaml', dict_file)

        print('File ' + owner_name + '_config.yaml created.')

        # create the lists file and backups if they don't exist
        for k, v in my_file.items():
            if not os.path.exists(v):
                shutil.copyfile("my_lists.txt", v)

        for f in my_file_backups:
            if not os.path.exists(f):
                shutil.copyfile("my_lists.txt", f)

        for k, v in my_achievements_file.items():
            if not os.path.exists(v):
                shutil.copyfile("my_achievements.txt", v)
        return True

    def validate(self, xx):
        valid_chars = "%s%s" % (string.ascii_letters, string.digits)
        filename = xx  # "This Is a (valid) - filename%$&$ .txt"
        return ''.join(c for c in filename if c in valid_chars)

