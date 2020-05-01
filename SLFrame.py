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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sean's Lists", pos = wx.DefaultPosition, size = wx.Size( 651,525 ), style = wx.DEFAULT_FRAME_STYLE|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 112, 112, 112 ) )
		
		fgSizer3 = wx.FlexGridSizer( 5, 4, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.AddGrowableCol( 2 )
		fgSizer3.AddGrowableCol( 3 )
		fgSizer3.AddGrowableRow( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3.SetMinSize( wx.Size( -5,-5 ) ) 
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText1.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )
		
		fgSizer3.Add( self.m_staticText1, 0, wx.ALIGN_BOTTOM, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel ", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		fgSizer3.Add( self.m_staticText2, 0, wx.ALIGN_BOTTOM|wx.ALL, 0 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel ", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText3.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		fgSizer3.Add( self.m_staticText3, 0, wx.ALIGN_BOTTOM, 0 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel ", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText4.SetBackgroundColour( wx.Colour( 128, 255, 255 ) )
		
		fgSizer3.Add( self.m_staticText4, 0, wx.ALIGN_BOTTOM, 0 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), wx.TE_NOHIDESEL|wx.TE_PROCESS_ENTER|wx.NO_BORDER )
		self.m_textCtrl1.SetBackgroundColour( wx.Colour( 255, 236, 236 ) )
		
		fgSizer3.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER, 0 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), wx.TE_NO_VSCROLL|wx.TE_PROCESS_ENTER|wx.NO_BORDER )
		self.m_textCtrl2.SetBackgroundColour( wx.Colour( 255, 255, 225 ) )
		
		fgSizer3.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), wx.TE_NO_VSCROLL|wx.TE_PROCESS_ENTER|wx.NO_BORDER )
		self.m_textCtrl3.SetBackgroundColour( wx.Colour( 236, 255, 236 ) )
		
		fgSizer3.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), wx.TE_NO_VSCROLL|wx.TE_PROCESS_ENTER|wx.NO_BORDER )
		self.m_textCtrl4.SetBackgroundColour( wx.Colour( 236, 255, 255 ) )
		
		fgSizer3.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_EDIT_LABELS|wx.LC_LIST|wx.LC_NO_HEADER|wx.FULL_REPAINT_ON_RESIZE|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.m_listCtrl1.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )
		
		fgSizer3.Add( self.m_listCtrl1, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 0 )
		
		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_EDIT_LABELS|wx.LC_LIST|wx.LC_NO_HEADER|wx.FULL_REPAINT_ON_RESIZE|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.m_listCtrl2.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		fgSizer3.Add( self.m_listCtrl2, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 0 )
		
		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_EDIT_LABELS|wx.LC_LIST|wx.LC_NO_HEADER|wx.FULL_REPAINT_ON_RESIZE|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.m_listCtrl3.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		fgSizer3.Add( self.m_listCtrl3, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 0 )
		
		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,400 ), wx.LC_EDIT_LABELS|wx.LC_LIST|wx.LC_NO_HEADER|wx.FULL_REPAINT_ON_RESIZE|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.m_listCtrl4.SetBackgroundColour( wx.Colour( 128, 255, 255 ) )
		
		fgSizer3.Add( self.m_listCtrl4, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 0 )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox1Choices, wx.CB_READONLY|wx.NO_BORDER )
		self.m_comboBox1.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )
		
		fgSizer3.Add( self.m_comboBox1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND, 0 )
		
		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox2Choices, wx.CB_READONLY|wx.NO_BORDER )
		self.m_comboBox2.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		fgSizer3.Add( self.m_comboBox2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND, 0 )
		
		m_comboBox3Choices = []
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox3Choices, wx.CB_READONLY|wx.NO_BORDER )
		self.m_comboBox3.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		fgSizer3.Add( self.m_comboBox3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND, 0 )
		
		m_comboBox4Choices = []
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), m_comboBox4Choices, wx.CB_READONLY|wx.NO_BORDER )
		self.m_comboBox4.SetBackgroundColour( wx.Colour( 128, 255, 255 ) )
		
		fgSizer3.Add( self.m_comboBox4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND, 0 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Archive", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Action 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.Hide()
		
		fgSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.Hide()
		
		fgSizer3.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.Hide()
		
		fgSizer3.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.m_textCtrl1.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_textCtrl3.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_textCtrl4.Bind( wx.EVT_TEXT_ENTER, self.add_item_to_list )
		self.m_listCtrl1.Bind( wx.EVT_KEY_UP, self.on_key_up )
		self.m_listCtrl1.Bind( wx.EVT_LIST_END_LABEL_EDIT, self.on_event_save1 )
		self.m_listCtrl1.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_listCtrl2.Bind( wx.EVT_KEY_UP, self.on_key_up )
		self.m_listCtrl2.Bind( wx.EVT_LIST_END_LABEL_EDIT, self.on_event_save )
		self.m_listCtrl2.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_listCtrl3.Bind( wx.EVT_KEY_UP, self.on_key_up )
		self.m_listCtrl3.Bind( wx.EVT_LIST_END_LABEL_EDIT, self.on_event_save )
		self.m_listCtrl3.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_listCtrl4.Bind( wx.EVT_KEY_UP, self.on_key_up )
		self.m_listCtrl4.Bind( wx.EVT_LIST_END_LABEL_EDIT, self.on_event_save )
		self.m_listCtrl4.Bind( wx.EVT_LIST_KEY_DOWN, self.on_list_key_down )
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.on_combo_box )
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.on_combo_box )
		self.m_comboBox3.Bind( wx.EVT_COMBOBOX, self.on_combo_box )
		self.m_comboBox4.Bind( wx.EVT_COMBOBOX, self.on_combo_box )
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_click_archive )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()
	
	def add_item_to_list( self, event ):
		event.Skip()
	
	
	
	
	def on_key_up( self, event ):
		event.Skip()
	
	def on_event_save1( self, event ):
		event.Skip()
	
	def on_list_key_down( self, event ):
		event.Skip()
	
	
	def on_event_save( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	def on_combo_box( self, event ):
		event.Skip()
	
	
	
	
	def on_click_archive( self, event ):
		event.Skip()
	

