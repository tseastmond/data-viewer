#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__title__ = 'DataViewer'
__author__ = 'Tanner S Eastmond'
__contact__ = 'https://github.com/tseastmond'
__license__ = 'MIT'


import pandas as pd
import wx
import wx.lib.mixins.listctrl  as  listmix

from _data import _data
from _pagetwo import _pagetwo
from _pagethree import _pagethree



###############################################################################
###############################################################################
###############################################################################
class DataViewer(wx.Frame):
    '''
    This class is a data viewer for Pandas DataFrames that allows the user
    to view, filter, and calculate summary statistics for each column.
    '''

    ###########################################################################
    ###########################################################################
    def __init__(self, df, rows=100):
        '''
        This class is a data viewer for Pandas DataFrames that allows the user
        to view, filter, and calculate summary statistics for each column.

        Parameters
        ----------
        df : Pandas DataFrame
            The data to view.
        rows : int
            Number of rows to show simultaneously.
        '''
        
        # Initialize the app.
        self.app = wx.App()
        
        
        # Set up the actual frame.
        wx.Frame.__init__(self, None, title='Pandas DataFrame Viewer')


        # Make a panel and a notebook.
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)


        # Set up the pages.
        page1 = _data(notebook, df, rows)
        page2 = _pagetwo(notebook)
        page3 = _pagethree(notebook)


        # Actually add the pages.
        notebook.AddPage(page1,'Data')
        notebook.AddPage(page2,'Page 2')
        notebook.AddPage(page3,'Page 3')
        

        # Size the notebook correctly.
        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        

        # Set a status bar.
        self.CreateStatusBar(1)
        self.SetStatusText('{0} Columns, {1} Rows'.format(len(df.columns), page1.list.GetItemCount()))
        
        
        # Ensure the app closes when exit button is clicked.
        closeBtn = wx.Button(panel, label="Close")
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        
        
        # Show and loop.
        self.Show()
        self.app.MainLoop()
        
        
        # Delete the app.
        del self.app
        
        
    ###########################################################################
    ###########################################################################
    def onClose(self, event):
        self.Destroy()



###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\tanne\OneDrive\Python\san_diego_unified\principals\clean.csv', encoding='latin')
    df.head()
    df.iloc[-2]
    df.tail()
    
    DataViewer(df, rows=-5)
