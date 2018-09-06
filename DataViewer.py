#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Tanner S Eastmond
Date Updated: 9/5/2018
Version: 1.1
Purpose: This class is a data viewer for Pandas DataFrames that allows the user
    to view, filter, and calculate summary statistics for each column.
'''

import pandas as pd
import wx

class Data(wx.Panel):
    '''
    Here we set up the actual data view window.
    '''

    def __init__(self, parent, df, rows):
        # Initialize the panel.
        wx.Panel.__init__(self, parent)

        # Make the listctrl.
        self.list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

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
        if len(df) >= rows:
            self.view = rows
        else:
            self.view = len(df)

        # Loop over the data.
        for x in range(self.view):
            # Set the item.
            index = self.list.InsertItem(x, df[df.columns[0]].iloc[x])

            # Set the font for the item.
            font = wx.Font(11, wx.ROMAN, wx.NORMAL, wx.NORMAL)
            self.list.SetItemFont(index, font)

            # Loop over columns.
            for y in range(len(df.columns)):
                # Set the rest of the columns.
                self.list.SetItem(index, y, df[df.columns[y]].iloc[x])

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))

class DataViewer(wx.Frame):
    '''
    This class is a data viewer for Pandas DataFrames that allows the user
    to view, filter, and calculate summary statistics for each column.

    Parameters
    ----------
    df  - A Pandas DataFrame object.
    '''

    def __init__(self, df, rows=100):
        # Set up the actual frame.
        wx.Frame.__init__(self, None, title='Pandas DataFrame Viewer')

        # Make a panel and a notebook.
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        # Set up the pages.
        page1 = Data(notebook, df, rows)
        page2 = PageTwo(notebook)
        page3 = PageThree(notebook)

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





def View(df, rows=100):
    '''
    Create and run the main app.
    '''
    # Initialize the app.
    app = wx.App()

    # Call the class.
    ex = DataViewer(df, rows=rows)

    # Show and loop.
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\tanne\OneDrive\Python\stocks\data\batch4.csv', encoding='latin')
    df = df[df.columns[0:4]]
    df['name'] = 'Tanner Scott Eastmond'
    df.head()
    View(df)
