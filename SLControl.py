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
from SLFiler import SLFiler
from initialize import Initialize
from setup_formOver import OptionsFrameOver1
import wx


def wizard():
    try:
        app = wx.App()
        s = OptionsFrameOver1(None)
        s.Show(True)
        app.MainLoop()
    except:
        init = Initialize()
        init.save_config("me")


class SLControl:
    _cache_list: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = None
    filer = SLFiler()
    if _cache_list is None:
        try:
            _cache_list = filer.load_config_yaml()
        except TypeError:
            print('file not found config.yaml - could be first time initialization')
            i_c = Initialize()
            i_b = i_c.initialized()
            # while not i_b:
            #    i_b = i_c.setup()
            print("A100")
            if not i_b:
                wizard()
            _cache_list = filer.load_config_yaml()
        except FileNotFoundError:
            print('file not found for the owner, make new files')
            i_c = Initialize()
            try:
                unchecked_owner = filer.get_owner()
                i_b = i_c.save_config(unchecked_owner)
                # while not i_b:
                #    i_b = i_c.setup()
                if not i_b:
                    wizard()
                print("A200")
                _cache_list = filer.load_config_yaml()
            except FileNotFoundError:
                print('file not found config.yaml again? - could be first time initialization')
                i_c = Initialize()
                i_b = i_c.initialized()
                print("A300")
#                while not i_b:
#                    i_b = i_c.setup()
                if not i_b:
                    wizard()
                b = False
                i = 5
                while not b and i > 1:
                    try:
                        _cache_list = filer.load_config_yaml()
                        b = True
                    except FileNotFoundError:
                        i = i - 1
                        if i > 1:
                            wizard()
                        else:
                            print('No owner name given.  Try again.')
                            exit()

    if _cache_list is None:
        print('problem loading config values into cache')
        exit()
    _cache = {}
    for t in _cache_list:
        for k, v in t.items():
            _cache[k] = v

    # File name for your list
    my_lists_filename = _cache["my_lists_filename"]
    # File names for your backups limit to 99
    my_lists_backups = _cache["my_lists_backups"]
    # this will substitute a comma in a word
    comma_substitution_char = _cache["comma_substitution_char"]
    # this will perform comma substitution if True
    perform_comma_substitution = _cache["perform_comma_substitution"]
    # this is a comma, used for word separator
    comma = _cache["comma"]
    # this is the newline character used in the file
    file_newline = '\n'
    # file to save achievements to
    my_achievements_file = _cache["my_achievements_file"]
    # frame title, i.e. the owner of these lists
    owner_name = _cache["owner_name"]
    # append mode (binary)
    append_mode = _cache["append_mode"]
    my_lists_version = _cache["my_lists_version"]
    AllList = _cache["AllList"]
    colorListsPalette = _cache["color_lists_palette"]
    available_palette_list = _cache["available_palettes"]
    defaultPalette = _cache["default_palette"]

    availablePalettes = {}
    for p in available_palette_list:
        availablePalettes[p] = _cache[p]

    try:
        p = availablePalettes[colorListsPalette]
    except:
        p = _cache_list[defaultPalette]
    color_scheme = p
