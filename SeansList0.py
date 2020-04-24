#########################
# Sean's List 0         #
# A simple list manager #
# Author: Sean Shannon  #
# (c) 2020.4.15         #
#########################

import wx
import logging

from SLControl import SLControl
from SLFiler import SLFiler
from SLFrameOver import SLFrameOver

# import lists from mylists.txt
filer = SLFiler()
my_lists = filer.get_my_lists(SLControl.my_lists_filename, SLControl.my_lists_version)
my_combos = filer.get_my_lists(SLControl.my_combos_filename, SLControl.my_combos_version)

if __debug__:
    logging.info(my_lists)

app = wx.App()
frame = SLFrameOver(None)
frame.hydrate_lists(my_lists)
frame.hydrate_combos(my_combos)
frame.Show(True)

app.MainLoop()

