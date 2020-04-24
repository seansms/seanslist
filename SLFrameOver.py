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


def get_last_date_archived():
	# same as the last row first word
	t_now = date.today()
	s_now = t_now.strftime("%y-%m-%d")
	last_date_archived = s_now
	filer = SLFiler()
	line = filer.get_last_line(SLControl.my_achievements_file)
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


def re_save_mylists(ctrls):
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
		self.m_button4.SetId(4)
		self.buttons = [self.m_button1, self.m_button2, self.m_button3, self.m_button4]

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

		for sta in self.statics:
			sta.SetLabelText(SLControl.list_names[sta.GetId()-101])
		self.SetTitle(SLControl.owner_name + "'s SuperList")

	def hydrate_lists(self, my_lists):
		hydrate_object(self.ctrls, my_lists, False)

	def hydrate_combos(self, my_lists):
		hydrate_object(self.combos, my_lists, True)

	def __del__(self):
		pass

	# Virtual event handlers, override them in your derived class
	def add_item_to_list(self, event):
		combo_id = event.GetEventObject().GetId()
		list_id = combo_id - 2000
		cb = self.combos[list_id - 1]
		if __debug__:
			print(cb.GetId())
			print("count= ", cb.GetCount())
			print("current_selection= ", cb.GetCurrentSelection())
			print("insertion_point= ", cb.GetInsertionPoint())
			print("selection= ", cb.GetSelection())
			print("string_selection= ", cb.GetStringSelection())
			print("value= ", cb.GetValue())
		new_text = cb.GetValue().strip()
		if new_text == "":
			return
		if __debug__:
			print(new_text)
		lb = self.ctrls[list_id - 1]
		lb.InsertItem(0, new_text)
		if __debug__:
			print("inserted ", new_text, "into list ctrl ", list_id)
		return re_save_mylists(self.ctrls)

	def on_event_save(self, event):
		self.save_flag = 1

	def save_if_needed(self, event):
		if self.save_flag == 1:
			self.save_flag = 0
			return re_save_mylists(self.ctrls)
		return 1

	def on_key_up(self, event):
		if __debug__:
			print ("on key up")
		keycode = event.GetKeyCode()
		if __debug__:
			print (keycode)
		if (keycode == 13):
			self.save_if_needed(event)
		event.Skip()

	def on_close(self, event):
		self.save_if_needed(event)
		event.Skip()

	def on_list_key_down(self, event):
		print ("event key down")
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_DELETE or keycode == wx.WXK_BACK:
			self.on_delete(event)
		if keycode == 13:
			re_save_mylists(self.ctrls)
		event.Skip()

	def on_delete(self, event):
		ctrl_id = event.GetEventObject().GetId()
		for ctrl in self.ctrls:
			i = 0  # safety valve
			item = 0
			if ctrl.GetId() == ctrl_id :
				while item != -1 and i < 100 :
					item = ctrl.GetFirstSelected(None)
					if item != -1:
						ctrl.DeleteItem(item)
					i = i + 1
		re_save_mylists(self.ctrls)
		event.Skip()

	def on_click_archive(self, event):
		svi = 0  # safety valve
		l_archive = []
		the_latest = get_last_date_archived()
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
		if re_save_mylists(self.ctrls) == 0:
			archive(l_archive, SLControl.my_achievements_file)
		event.Skip()
