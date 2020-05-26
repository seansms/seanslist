import logging
from typing import Dict, List, Any, Union, Hashable
import yaml


class SLControl:
    _cache_list: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = None
    if _cache_list is None:
        with open(r'config.yaml') as file:
            _cache_list = yaml.load(file, yaml.FullLoader)
    if _cache_list is None:
        print('problem loading config values into cache')
    _cache = {}
    for t in _cache_list:
        for k, v in t.items():
            _cache[k] = v

    #File name for your list
    my_lists_filename = _cache["my_lists_filename"]
    #File names for your backups limit to 99
    my_lists_backups = _cache["my_lists_backups"]
    #this will substitute a comma in a word
    comma_substitution_char = _cache["comma_substitution_char"]
    #this will perform comma substitution if True
    perform_comma_substitution = _cache["perform_comma_substitution"]
    #this is a comma, used for word separator
    comma = _cache["comma"]
    #this is the newline character used in the file
    file_newline = '\n'
    #this is the control flag for reading a file
    read_from_file = _cache["read_from_file"]
    #this is the control flag for writing to a file
    write_to_file = _cache["write_to_file"]
    #file to save achievements to
    my_achievements_file = _cache["my_achievements_file"]
    #frame title, i.e. the owner of these lists
    owner_name = _cache["owner_name"]
    #append mode (binary)
    append_mode = _cache["append_mode"]
    my_lists_version = _cache["my_lists_version"]
    AllList = _cache["AllList"]


