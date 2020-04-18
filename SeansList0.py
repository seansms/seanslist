#########################
# Sean's List 0         #
# A simple list manager #
# Author: Sean Shannon  #
# (c) 2020.4.15         #
#########################

import wx
import logging

from SLFiler import SLFiler
from SLFrameOver import SLFrameOver

# import lists from mylists.txt
filer = SLFiler()
my_lists = filer.get_my_lists()

if __debug__:
    logging.info(my_lists)

app = wx.App()
frame = SLFrameOver(None)
frame.hydrate(my_lists)
frame.Show(True)

app.MainLoop()

