import logging


class SLControl:
    #File name for your list
    my_lists_filename = "my_lists.txt"
    #File names for your backups limit to 99
    my_lists_backups = ["my_lists2.txt", "my_lists3.txt", "my_lists4.txt"]
    #this will substitute a comma in a word
    comma_substitution_char = ";"
    #this will perform comma substitution if True
    perform_comma_substitution = True
    #this is a comma, used for word separator
    comma = ","
    #this is the newline character used in the file
    file_newline = "\n"
    #this is the control flag for reading a file
    read_from_file = "r"
    #this is the control flag for writing to a file
    write_to_file = "w"
    #file to save achievements to
    my_achievements_file = "achievements.txt"
    #frame title, i.e. the owner of these lists
    owner_name = "Sean"
    #append mode (binary)
    append_mode = "a"
    my_lists_version = "My Lists v0.1"
    AllList = "all_list_names"
