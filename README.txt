Sean's SuperList 0_6
Sean's SuperList runs on Python 3.7
and WxPython 4.x

Get WxPython: 
pip install -U wxPython


Start Sean's List in the same folder as the seanslist0.py file.
In windows:
py seanslist0.py

my_lists.txt file format
The first line of my_lists.txt must be "My Lists v0.0" or the program will not load your lists

my_combos.txt file format
The first line of my_lists.txt must be "My Combos v0.0" or the program will not load your combo boxes

my_achievements.txt file format
The first line is blank.  Each subsequent line is blank followed by a comma separated list.  Select items in all your lists and click Archive to move items here.
If you don't want them archived, then just delete with the del or backspace key.

SeansList 0_6 supports four lists.  By default, semicolons are translated from the file
to a comma in the list, allowing for commas in the text.

After each new entry to a list, all lists are saved to my_list.txt and two backups
are made my_list2.txt and my_list3.txt.  I recommend installing Sean's SuperList in a folder
that is copied to the cloud for a backup and to be reached from other locations.

Look at SLControl for options.  Make a backup copy and manually merge before you upgrade.

