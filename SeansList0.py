#########################
# Sean's List 0         #
# A simple list manager #
# Author: Sean Shannon  #
# (c) 2020.4.15         #
#########################

import wx

from SLLists import SLLists

app = wx.App()

superlist = SLLists()
superlist.engage()

app.MainLoop()

