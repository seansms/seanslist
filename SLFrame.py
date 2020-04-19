# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SLFrame1
###########################################################################

class SLFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sean's Lists", pos = wx.DefaultPosition, size = wx.Size( 651,491 ), style = wx.DEFAULT_FRAME_STYLE|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 112, 112, 112 ) )
		
		fgSizer3 = wx.FlexGridSizer( 3, 4, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.AddGrowableCol( 2 )
		fgSizer3.AddGrowableCol( 3 )
		fgSizer3.AddGrowableRow( 2 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3.SetMinSize( wx.Size( -5,-5 ) ) 
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"Working On", wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox1Choices, 0|wx.NO_BORDER )
		self.m_comboBox1.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )
		
		fgSizer3.Add( self.m_comboBox1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Follow Up", wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox2Choices, 0|wx.NO_BORDER )
		self.m_comboBox2.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		fgSizer3.Add( self.m_comboBox2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		m_comboBox3Choices = []
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Goals", wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox3Choices, 0|wx.NO_BORDER )
		self.m_comboBox3.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		fgSizer3.Add( self.m_comboBox3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		m_comboBox4Choices = []
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"Favorites", wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox4Choices, 0|wx.NO_BORDER )
		self.m_comboBox4.SetBackgroundColour( wx.Colour( 128, 255, 255 ) )
		
		fgSizer3.Add( self.m_comboBox4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"push", wx.DefaultPosition, wx.Size( 160,-1 ), 0|wx.NO_BORDER )
		self.m_button1.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )
		
		fgSizer3.Add( self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0|wx.NO_BORDER )
		self.m_button2.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		fgSizer3.Add( self.m_button2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0|wx.NO_BORDER )
		self.m_button3.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		fgSizer3.Add( self.m_button3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0|wx.NO_BORDER )
		self.m_button4.SetBackgroundColour( wx.Colour( 128, 255, 255 ) )
		
		fgSizer3.Add( self.m_button4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_LIST|wx.LC_NO_HEADER|wx.NO_BORDER )
		self.m_listCtrl1.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )
		
		fgSizer3.Add( self.m_listCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_LIST|wx.LC_NO_HEADER|wx.NO_BORDER )
		self.m_listCtrl2.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		fgSizer3.Add( self.m_listCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_LIST|wx.LC_NO_HEADER|wx.NO_BORDER )
		self.m_listCtrl3.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		fgSizer3.Add( self.m_listCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_LIST|wx.LC_NO_HEADER|wx.NO_BORDER )
		self.m_listCtrl4.SetBackgroundColour( wx.Colour( 128, 255, 255 ) )
		
		fgSizer3.Add( self.m_listCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_comboBox1.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_comboBox2.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_comboBox3.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_comboBox4.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_button1.Bind( wx.EVT_BUTTON, self.add_item_to_list )
		self.m_button2.Bind( wx.EVT_BUTTON, self.add_item_to_list )
		self.m_button3.Bind( wx.EVT_BUTTON, self.add_item_to_list )
		self.m_button4.Bind( wx.EVT_BUTTON, self.add_item_to_list )
		self.m_listCtrl1.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_listCtrl2.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_listCtrl3.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_listCtrl4.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def add_item_to_list( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	def on_list_key_down( self, event ):
		event.Skip()
	
	
	
	

