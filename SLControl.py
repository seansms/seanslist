import logging


class SLControl:
    #File name for your list
    my_lists_filename = "my_lists.txt"
    #File names for your backups limit to 99
    my_lists_backups = ["my_lists2.txt", "my_lists3.txt"]
    #this will substitute a comma in a word
    comma_substitution_char = ";;"
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
    my_achievements_file = "my_achievements.txt"
    #list names
    list_names = ["Team To-dos ", "Drive Bys ", "SL wants ", "Personal "]
    #frame title, i.e. the owner of these lists
    owner_name = "Sean"