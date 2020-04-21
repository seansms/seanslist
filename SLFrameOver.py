# -*- coding: utf-8 -*- 

###########################################################################
## Class SLFrameOver - Override of SLFrame
###########################################################################
import wx
import wx.xrc

from SLFrame import SLFrame1
from SLFiler import SLFiler
from SLControl import SLControl


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
		self.dc = {1: self.m_comboBox1, 2: self.m_comboBox2, 3: self.m_comboBox3, 4: self.m_comboBox4}
		self.dl = {1: self.m_listCtrl1, 2: self.m_listCtrl2, 3: self.m_listCtrl3, 4: self.m_listCtrl4}
		for sta in self.statics:
			sta.SetLabelText(SLControl.list_names[sta.GetId()-101])
		self.SetTitle(SLControl.owner_name + "'s SuperList")

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
		if btn_id > 2000:  #the event was fired from a ctrl
			btn_id = btn_id - 2000
		cb = self.dc[btn_id]
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
		lb = self.dl[btn_id]
		lb.InsertItem(0, new_text)
		if __debug__:
			print("inserted ", new_text, "into list ctrl ", btn_id)
		self.re_save()

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
				out_list.append(s)
		return out_list

	def build_list_from_ctrl(self, ctrl):
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

	def on_event_save(self, event):
		self.save_flag = 1

	def save_if_needed(self, event):
		if self.save_flag == 1:
			self.save_flag = 0
			self.re_save()

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

	def re_save(self):
		ll = self.build_lists()
		filer = SLFiler()
		filer.save_values(ll)

	def on_list_key_down(self, event):
		print ("event key down")
		keycode = event.GetKeyCode()
		if (keycode == wx.WXK_DELETE):
			self.on_delete(event)
		if (keycode == 13):
			self.re_save()
		event.Skip()

	def on_delete(self, event):
		ctrl_id = event.GetEventObject().GetId()
		for ctrl in self.ctrls:
			i = 0  #safety valve
			item = 0
			if ctrl.GetId() == ctrl_id :
				while item != -1 and i < 100 :
					item = ctrl.GetFirstSelected(None)
					if item != -1:
						ctrl.DeleteItem(item)
					i = i + 1
		self.re_save()

