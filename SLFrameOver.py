# -*- coding: utf-8 -*- 

###########################################################################
## Class SLFrameOver - Override of SLFrame
###########################################################################
import wx
import wx.xrc

from SLFrame import SLFrame1
from SLFiler import SLFiler


class SLFrameOver(SLFrame1):

	def __init__(self, parent):
		SLFrame1.__init__(self, parent)
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
		self.dc = {1: self.m_comboBox1, 2: self.m_comboBox2, 3: self.m_comboBox3, 4: self.m_comboBox4}
		self.dl = {1: self.m_listCtrl1, 2: self.m_listCtrl2, 3: self.m_listCtrl3, 4: self.m_listCtrl4}

	def hydrate(self, myLists):
		i = 0
		for c in self.combos:
			c.SetItems(myLists[i])
			i = i + 2
		i = 1
		for t in self.ctrls:
			self.hydrate_ctrl(t, myLists[i])
			i = i + 2

	def hydrate_ctrl(self, ctrlX, listX):
		i = 0
		for word in listX:
			ctrlX.InsertItem(i, word)
			i = i + 1

	def __del__(self):
		pass

	# Virtual event handlers, override them in your derived class
	def add_item_to_list(self, event):
		btn_id = event.GetEventObject().GetId()
		cb = self.dc[btn_id]
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
		print(new_text)
		lb = self.dl[btn_id]
		lb.InsertItem(0, new_text)
		print("inserted ", new_text, "into list ctrl ", btn_id)
		self.reSave()

	def build_lists(self):
		ll = []
		c = len(self.combos)
		i = 0
		for combo in self.combos:
			ll.append(self.build_list(combo))
			ll.append(self.build_list_from_ctrl(self.ctrls[i]))
			i = i + 1
		return ll

	def build_list(self, box):
		out_list = []
		c = box.GetCount()
		for j in range(c):
			s = box.GetString(j).rstrip()
			if s != "" or s != "\n":
				print("8", s, "8")
				out_list.append(s)
		return out_list

	def build_list_from_ctrl(self, ctrl):
		l = []
		item = -1
		while 1:
			item = ctrl.GetNextItem(item, wx.LIST_NEXT_ALL, wx.LIST_STATE_DONTCARE)
			if item == -1:
				break
			print(ctrl.GetItemText(item, 0))
			l.append(ctrl.GetItemText(item, 0))
		return l

	def re_save(self):
		ll = self.build_lists()
		filer = SLFiler()
		filer.save_values(ll)

	def on_key_up(self, event):
		keycode = event.GetKeyCode()
		if (keycode == wx.WXK_DELETE):
			self.onDelete()
		event.Skip()

	def on_delete(self):
		self.cleanFromList(self.m_listCtrl1)

	def clean_from_list(self, box):
		l = []
		nl = []
		c = box.GetCount()
		for j in range(c):
			s = box.GetString(j)
			l.append(s)
		selectedItems = box.GetStringSelection()
		box.clear()
		for w in l:
			if w != selectedItems:
				box.append(w)
