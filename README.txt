Sean's SuperList 0_7
Sean's SuperList runs on Python 3.7
and WxPython 4.x

Get WxPython: 
pip install -U wxPython


Start Sean's List in the same folder as the seanslist0.py file.
In windows:
py seanslist0.py

my_lists.txt file format
The first line of my_lists.txt must be "My Lists v0.1" or the program will not load your lists.
Each list's first item must be: "Local" followed by the list name.  Copy blank_lists.txt to
my_lists.txt for a clean start.

<owner>_achievements.txt file format
You must create this file. Yes, it's a bug.
The first line is blank.  Each subsequent line is blank followed by a comma separated list.  Select items in all your lists and click Archive to move items here.
If you don't want them archived, then just delete with the del or backspace key.
Pressing the Archive button puts selected items from all lists in this file and removes them from their
list.

Sean's SuperList 0_7 supports many lists.  By default, semicolons are translated from the file
to a comma in the list, allowing for commas in the text.

After each new entry to a list, all lists are saved to <owner>_list.txt and two backups
are made my_list2.txt and my_list3.txt.  I recommend installing Sean's SuperList in a folder
that is copied to the cloud for a backup and to be reached from other locations.

Look at SLControl.py for options and to set <owner>.  This will be replaced in the future.
  Make a backup copy and manually merge before you upgrade.

