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
## Class SLFrameOver - Override of SLFrame
###########################################################################
import wx
import wx.xrc

from datetime import date
from SLFrame import SLFrame1
from SLFiler import SLFiler
from SLControl import SLControl


def clear_ctrl(ctrl):
	while ctrl.ItemCount > 0:
		ctrl.DeleteItem(0)


def hydrate_ctrl(ctrl1, list1):
	position = 0 #the position in the list
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
	line = filer.get_last_line(filename)
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


def re_save_mylists_old(ctrls):
	ll = build_list_of_lists_from_ctrls(ctrls)
	filer = SLFiler()
	filer.save_values(ll, SLControl.my_lists_filename, SLControl.my_lists_version)
	return 0


class SLFrameOver(SLFrame1):

	def __init__(self, parent):
		SLFrame1.__init__(self, parent)
		self.save_flag = 0
		self.m_button1.SetId(1)
		self.m_button2.SetId(2)
		self.m_button3.SetId(3)
		self.buttons = [self.m_button1, self.m_button2, self.m_button3, self.m_button4]
		self.filer = None

		self.m_comboBox1.SetId(2001)
		self.m_comboBox2.SetId(2002)
		self.m_comboBox3.SetId(2003)
		self.m_comboBox4.SetId(2004)
		self.combos = [self.m_comboBox1, self.m_comboBox2, self.m_comboBox3, self.m_comboBox4]

		self.m_listCtrl1.SetId(1001)
		self.m_listCtrl2.SetId(1002)
		self.m_listCtrl3.SetId(1003)
		self.m_listCtrl4.SetId(1004)
		self.ctrls = [self.m_listCtrl1, self.m_listCtrl2, self.m_listCtrl3, self.m_listCtrl4]

		self.m_staticText1.SetId(101)
		self.m_staticText2.SetId(102)
		self.m_staticText3.SetId(103)
		self.m_staticText4.SetId(104)
		self.statics = [self.m_staticText1, self.m_staticText2, self.m_staticText3, self.m_staticText4]

		self.m_textCtrl1.SetId(201)
		self.m_textCtrl2.SetId(202)
		self.m_textCtrl3.SetId(203)
		self.m_textCtrl4.SetId(204)
		self.texts = [self.m_textCtrl1, self.m_textCtrl2, self.m_textCtrl3, self.m_textCtrl4]

		self.SetTitle(SLControl.owner_name + "'s SuperList")

	def hydrate_lists(self, dic, displayed):
		i = 0
		displayed_lists = []
		for d in displayed:
			displayed_lists.append(dic[d])
		hydrate_object(self.ctrls, displayed_lists, False)

	def hydrate_combos(self, my_lists):
		hydrate_object(self.combos, my_lists, True)

	def __del__(self):
		pass

	# Virtual event handlers, override them in your derived class
	def add_item_to_list(self, event):
		texts_id = event.GetEventObject().GetId()
		list_id = texts_id - 200
		tb = event.GetEventObject()
		if __debug__:
			print(tb.GetId())
			print("value= ", tb.GetValue())
		new_text = tb.GetValue().strip()
		if new_text == "":
			return
		if __debug__:
			print(new_text)
		lb = self.ctrls[list_id - 1]
		lb.InsertItem(0, new_text)
		if __debug__:
			print("inserted ", new_text, "into list ctrl ", list_id)
		return self.re_save_mylists(self.ctrls)

	def on_event_save(self, event):
		self.save_flag = 1

	def save_if_needed(self, event):
		if self.save_flag == 1:
			self.save_flag = 0
			return self.re_save_mylists(self.ctrls)
		return 1

	def on_key_up(self, event):
		keycode = event.GetKeyCode()
		if __debug__:
			print("on_key_up ", keycode)
		if keycode == 13:
			self.save_if_needed(event)
		event.Skip()

	def on_close(self, event):
		if __debug__:
			print("on_close")
		self.save_if_needed(event)
		event.Skip()

	def on_list_key_down(self, event):
		keycode = event.GetKeyCode()
		if __debug__:
			print("on_list_key_down: ", keycode)
		if keycode == wx.WXK_DELETE or keycode == wx.WXK_BACK:
			self.on_delete(event)
		if keycode == 13:
			self.re_save_mylists(self.ctrls)
		if keycode == 67:
			self.on_copy(event)
		event.Skip()

	def on_copy(self, event):
		if __debug__:
			print("on copy")
		self.clip_it(self.get_selected_text(event))

	def get_selected_text(self, event):
		c = event.GetEventObject()
		j = c.GetFirstSelected()
		x = c.GetItemText(j)
		isel = c.GetSelectedItemCount()
		for i in range(1, isel):
			x = x + ","
			j = c.GetNextSelected(j)
			x = x + c.GetItemText(j)
		return x

	def clip_it(self, set_text):
		clipdata = wx.TextDataObject()
		clipdata.SetText(set_text)
		wx.TheClipboard.Open()
		wx.TheClipboard.SetData(clipdata)
		wx.TheClipboard.Close()

	def on_delete(self, event):
		ctrl_id = event.GetEventObject().GetId()
		if __debug__:
			print("on delete:", ctrl_id)
		for ctrl in self.ctrls:
			i = 0  # safety valve
			item = 0
			if ctrl.GetId() == ctrl_id:
				while item != -1 and i < 100:
					item = ctrl.GetFirstSelected(None)
					if item != -1:
						ctrl.DeleteItem(item)
					i = i + 1
		self.re_save_mylists(self.ctrls)
		event.Skip()

	def on_click_archive(self, event):
		achievements_filename = SLControl.my_achievements_file
		svi = 0  # safety valve
		l_archive = []
		the_latest = get_last_date_archived(achievements_filename)
		if the_latest != "current":
			l_archive.append("\n")
			l_archive.append(the_latest)
		# else we append to the current line
		c = 0
		for c_ctrl in self.ctrls:
			c = c + 1
			c_item = 0
			while c_item != -1 and svi < 1000:
				c_item = c_ctrl.GetFirstSelected(None)
				if c_item != -1:
					l_archive.append(c_ctrl.GetItemText(c_item))
					c_ctrl.DeleteItem(c_item)
				svi = svi + 1
		if self.re_save_mylists(self.ctrls) == 0:
			archive(l_archive, achievements_filename)
		event.Skip()

	def hydrate_statics(self, my_displayed_lists):
		i = 0
		for sta in self.statics:
			sta.SetName(my_displayed_lists[i])
			sta.SetLabelText(my_displayed_lists[i])
			i = i + 1

	def cb_item_selected(self, event):
		combo = event.GetEventObject()
		combo_id = event.GetEventObject().GetId()
		print(combo)
		print(combo_id)
		event.Skip()

	def on_text(self, event):
		print(event.GetEventObject().GetId())
		print("text entered")
		event.Skip()

	def re_save_mylists(self, ctrls):
		refresh_dic = {}
		ll = build_list_of_lists_from_ctrls(ctrls)
		i = 0
		for s in self.statics:
			refresh_dic[s.GetLabelText()] = ll[i]
			i = i + 1
		self.filer.save_values(refresh_dic, SLControl.my_lists_filename, SLControl.my_lists_version)
		return 0

	def on_combo_box(self, event):
		controls = self.ctrls
		cb = event.GetEventObject()
		if __debug__:
			print("on_combo_box", cb, cb.GetId(), cb.GetValue())
		my_lists = self.filer.main_dict["My Lists"]
		list_id = cb.GetId() - 2000
		new_list = self.filer.main_dict[cb.GetValue()]
		self.statics[list_id - 1].SetLabelText(cb.GetValue())
		my_lists[list_id - 1] = cb.GetValue()
		clear_ctrl(controls[list_id - 1])
		hydrate_ctrl(controls[list_id - 1], new_list)
		self.re_save_mylists(controls)
		event.Skip()
