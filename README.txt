Sean's SuperList 0_9 (alpha)
Sean's SuperList runs on Python 3.7
and WxPython 4.x

Windows installation file available!
Executable build zip file available!

All files now stored here (on Windows):
C:\Users\<your windows username>\AppData\Local\Seanslist
Yes, this is a hidden folder, but you should be able to access it.

New start!
The program begins with a simple startup window.  Simply type in a short name and press submit.
This will create your file set and open a default set of lists in the interface.

File Listing
1. config.yaml
The config.yaml stores the owner of the file.  You can edit this file and it will create new default files for the new name automatically.

sample contents
owner: sean

2. owner_config.yaml
This file has the configuration chosen for this owner.  It is not recommended to change this file without talking to tech support first.

3. owner_achievements.txt
This file keeps a log of your achievements as you select and press Archive.  Careful not to delete items from your lists.

4. owner_lists.txt
This is where your lists are kept.  Add lists or modify lists using a text editor.  Be sure to put "Local,<ListName>," at the beginning of your list.

5. backups, e.g. owner_lists2.txt
Every time a change is made a copy is pushed to version 2, etc.  Look to these files in case you made a mistake!  Sorry, the UNDO function is still in development.

Start Sean's List manually
In Windows:
py seanslist0.py

This will launch a four-color interface of four lists.  If you don't see this, then there was a problem with your python
3 configuration and you may have to use a different platform or import some libraries.

my_lists.txt file format
The first line of my_lists.txt must be "My Lists v0.1" or the program will not load your lists.

Every list is a comma separated WITHOUT quotation marks.  Each list's first item must be: "Local" followed by a comma,
then the list name.  Copy blank_lists.txt to <owner>_lists.txt and restart to start with blank lists.

Sean's SuperList 0_9 supports many lists.

By default, semicolons are translated from the file to a comma in the list, allowing for commas in the text.  Ask support if you need to change this.

Email support: sean@shannonkids.com
Use subject: Sean's List Help!

