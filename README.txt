Sean's SuperList 0_8
Sean's SuperList runs on Python 3.7
and WxPython 4.x

Get WxPython: 
pip install -U wxPython

Other libraries used:
    logging
    yaml - config files
    shutil - file manipulation
    os - file information
    typing - helps with yaml file processing
    date

Start by creating a config file.
In windows:
py initialize.py
If a config.yaml file already exists, it will ask if you want to continue.  This is to protect you from accidentally overwriting your configuration.
If you want to continue, press 1.  Or if you don't have a config.yaml file, then it will go to the next question:
What is the owner name [default=my]?
 Sean's SuperList will save your lists as <owner>_lists.txt and your achievements as <owner>_achievements.txt.
 The default owner's name is "my."  Note that if you choose this, there is a good chance that your lists will disappear if you upgrade.
File config.yaml created.
 This means your config file has been created!

Config.yaml file options
Here are the contents of a config file with owner: Sean
- my_lists_filename: Sean_lists.txt
- my_lists_backups:
  - Sean_lists2.txt
  - Sean_lists3.txt
  - Sean_lists4.txt
- comma_substitution_char: ;
- perform_comma_substitution: true
- comma: ','
- read_from_file: r
- write_to_file: w
- my_achievements_file: Sean_achievements.txt
- owner_name: Sean
- append_mode: a
- my_lists_version: My Lists v0.1
- AllList: all_list_names

my_lists_filename: this is the file that holds your lists.
my_lists_backups: list up to ten different files here with any name you want.  Every time a change is made to your lists,
  the my_lists_filename file gets saved.  But before that happens a backup is copied up the chain of files listed.  You
  may even put these files into a folder that gets synced to a cloud.  Knowing where these files are will help if you need
  to recover some data.
comma_substitution_char: when lists are saved, commas are converted this character to distinguish them from the commas
  used to separate fields.  When the files are read back in, this character is turned back into a comma for display.  By
  default this is the semicolon (;).  If you plan on using semicolon in your lists, then consider changing this value.
read_from_file, write_to_file: These are codes used by the programmer.  Don't change these unless asked to.
my_achievements_file: this file is where your daily achievements are stored when you click the Archive button.
owner_name: Your name, I recommend not using a space here, but it might work.
append_mode: Code used for the programmer.
my_lists_version: This is used to identify the file format of the lists file.
AllList: this is the name of a list in my_lists_filename file that lists all the lists you have.  It's not recommended to
  change the contents of this list.  It's used to show you which lists you have.

Start Sean's List in the same folder as the seanslist0.py file from a command prompt.
In Windows:
py seanslist0.py

This will launch a four-color interface of four lists.  If you don't see this, then there was a problem with your python
3 configuration and you may have to use a different platform or import some libraries.

my_lists.txt file format
The first line of my_lists.txt must be "My Lists v0.1" or the program will not load your lists.

Every list is a comma separated without quotation marks.  Each list's first item must be: "Local" followed by a comma,
then the list name.  Copy blank_lists.txt to my_lists.txt (or <owner>_lists.txt) and restart to start from scratch.

Sean's SuperList 0_8 supports many lists.  By default, semicolons are translated from the file
to a comma in the list, allowing for commas in the text.

Make a backup copy of your lists and yaml files and manually merge before you upgrade.  This is less critical with the
change to the yaml file, but always a good suggestion nonetheless.

