#########################
# Sean's List 0         #
# A simple list manager #
# Author: Sean Shannon  #
# (c) 2020.4.15         #
#########################
#    Sean's SuperList - A to-do and general list manager.
#    Copyright (C) 2020  Sean Shannon
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import wx
from SLLists import SLLists


class SeansList0:

    def main(self):
        app = wx.App()

        superlist = SLLists()
        superlist.engage()

        app.MainLoop()


s = SeansList0()
s.main()


