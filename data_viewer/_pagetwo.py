#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import wx
import wx.lib.mixins.listctrl  as  listmix



###############################################################################
###############################################################################
###############################################################################
class _pagetwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))