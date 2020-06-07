# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from setup_form import OptionsFrame1
from initialize import Initialize

###########################################################################
## Class OptionsFrame1
###########################################################################


class OptionsFrameOver1 ( OptionsFrame1 ):

	def __init__(self, parent):
		self.ok_to_close = False
		OptionsFrame1.__init__(self, parent)
		self.Layout()

	def onSubmitSetup( self, event ):
		init = Initialize()
		init.save_config(self.m_textCtrl1.GetValue())
		self.ok_to_close = True
		self.Close()

	def onCancel(self, event):
		self.ok_to_close = True
		self.Close()

	def __del__( self ):
		pass
