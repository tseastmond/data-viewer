#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import wx
import wx.lib.mixins.listctrl  as  listmix



###############################################################################
###############################################################################
###############################################################################
class _data(wx.Panel):
    '''
    Here we set up the actual data view window.
    '''

    def __init__(self, parent, df, rows=100):
        # Initialize the panel.
        wx.Panel.__init__(self, parent)
        

        # Make the listctrl.
        self.list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES | wx.LC_SINGLE_SEL| wx.LB_NEEDED_SB)


        # Make headers.
        for num, x in enumerate(df.columns):
            # Keep the column width, which will be twice the length of the label or the minimum of 50 and the longest string.
            self.list.InsertColumn(num, x)
            self.list.SetColumnWidth(num, width=max(len(x)*20, min(50*10, df[x].astype(str).str.len().max()*10)))


            # Set the font for the whole columns.
            font = wx.Font(13, wx.ROMAN, wx.NORMAL, wx.FONTWEIGHT_BOLD)
            self.list.SetFont(font)


        # Size the panel.
        sizer = wx.BoxSizer()
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)


        # We will default to only seeing the first 100 rows, the user can get more.
        self.first = True
        
        if len(df) >= abs(rows) and rows > 0:
            self.view = rows
        elif len(df) >= abs(rows) and rows < 0:
            self.view = abs(rows)
            self.first = False
        else:
            self.view = len(df)


        # Loop over the data.
        for x in range(self.view):
            # Set the item.
            if self.first:
                index = self.list.InsertItem(x, str(df[df.columns[0]].iloc[x]))
            else:
                index = self.list.InsertItem(x, str(df[df.columns[0]].iloc[-(x+1)]))
            
            # Set alternate row colors.
            if x % 2 == 0:
                self.list.SetItemBackgroundColour(x, wx.Colour(235, 240, 255))
            else:
                pass
                

            # Set the font for the item.
            font = wx.Font(11, wx.ROMAN, wx.NORMAL, wx.NORMAL)
            self.list.SetItemFont(index, font)
            

            # Loop over columns.
            for y in range(len(df.columns)):
                # Set the rest of the columns.
                if self.first:
                    self.list.SetItem(index, y, str(df[df.columns[y]].iloc[x]))
                else:
                    self.list.SetItem(index, y, str(df[df.columns[y]].iloc[-(x+1)]))