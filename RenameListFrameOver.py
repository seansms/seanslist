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
# -*- coding: utf-8 -*-

###########################################################################
# Class RenameListFrameOver a popup form over SLFrame1
###########################################################################
import wx
import wx.xrc

from datetime import date
from SLFrame import SLFrame1, NewListFrame, RenameListFrame
from SLFiler import SLFiler
from SLControl import SLControl


def clear_ctrl(ctrl):
    while ctrl.ItemCount > 0:
        ctrl.DeleteItem(0)

def hydrate_ctrl(ctrl1, list1):
    position = 0  # the position in the list
    for word in list1:
        ctrl1.InsertItem(position, word)
        position = position + 1

def hydrate_object(controls, lists, list_at_a_time):
    i = 0
    for list1 in lists:
        if list_at_a_time:
            controls[i].SetItems(list1)
        else:
            hydrate_ctrl(controls[i], list1)
        i = i + 1


def build_list(box):
    out_list = []
    c = box.GetCount()
    for j in range(c):
        s = box.GetString(j).rstrip()
        if s != "" or s != "\n":
            out_list.append(s)
    return out_list


def build_list_from_ctrl(ctrl):
    l = []
    item = -1
    while 1:
        item = ctrl.GetNextItem(item, wx.LIST_NEXT_ALL, wx.LIST_STATE_DONTCARE)
        if item == -1:
            break
        if __debug__:
            print(ctrl.GetItemText(item, 0))
        l.append(ctrl.GetItemText(item, 0))
    if len(l) == 0:
        l.append("")
    return l


def archive(archive_list, filename):
    if __debug__:
        print("archive")
    filer = SLFiler()
    filer.append_values_to_file(archive_list, filename)

def get_last_date_archived(filename):
    # same as the last row first word
    t_now = date.today()
    s_now = t_now.strftime("%y-%m-%d")
    last_date_archived = s_now
    filer = SLFiler()
    line = filer.get_last_line_in_achievements('my_achievements.txt', filename)
    words = line.split(SLControl.comma)
    for w in words:
        last_date_archived = w
        break
    if s_now == last_date_archived:
        return "current"
    return s_now


def build_list_of_lists_from_ctrls(ctrls):
    ll = []
    i = 0
    for ctrl in ctrls:
        ll.append(build_list_from_ctrl(ctrl))
        i = i + 1
    return ll


class RenameListFrameOver(RenameListFrame):

    def __init__(self, parent):
        self.parent = parent
        RenameListFrame.__init__(self, parent)

    def __del__(self):
        pass

    def on_click_rename( self, event ):
        list_name = self.m_staticTextRename.GetLabelText()
        new_list_name = self.m_textCtrl_rename.GetValue()
        self.parent.re_save_mylists_plus_rename(self.parent.ctrls, list_name.strip(), new_list_name.strip())
        self.Hide()

    def on_click_cancel_rename( self, event ):
        self.Hide()
