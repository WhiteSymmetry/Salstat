#!/usr/bin/env python

import time, os, os.path
import urlparse, urllib, codecs
import wx
import images
import sys, numpy
import AllRoutines


class WithinSubjectsClass(wx.Panel):
    def __init__(self, parent, columnList):
        wx.Panel.__init__(self, parent, -1)
        helpWithin = "Within-subjects tests are when participants only take part in one of the conditions."
        t20 = wx.StaticText(self,-1,label=helpWithin,pos=(20,20))
        t20.Wrap(620)
        t21 = wx.StaticText(self,-1,"Select the test you want:",pos=(60,80))
        t22 = wx.StaticText(self,-1,"Select your variables:",pos=(320,80))
        self.test1 = wx.CheckBox(self,-1,"T-test (unpaired)",pos=(60,110))
        self.test2 = wx.CheckBox(self,-1,"Wilcoxon Signed Ranks",pos=(60,140))
        self.test3 = wx.CheckBox(self,-1,"Paired sign test",pos=(60,170))
        self.DVBox = wx.CheckListBox(self,-1,pos=(320,100),size=(300,120),choices=columnList)

class BetweenSubjectsClass(wx.Panel):
    def __init__(self, parent, columnList):
        wx.Panel.__init__(self, parent, -1)
        helpBetween = "Between-subjects tests are when participants take part in all conditions."
        t10 = wx.StaticText(self,-1,label=helpBetween,pos=(20,20))
        t10.Wrap(620)
        t11 = wx.StaticText(self,-1,"Select the test you want:",pos=(60,80))
        t12 = wx.StaticText(self,-1,"Select your independent variable:",pos=(320,80))
        t13 = wx.StaticText(self,-1,"Select your dependent variable:",pos=(320,150))
        self.test1 = wx.CheckBox(self,-1,"T-test (unpaired)",pos=(60,110))
        self.test2 = wx.CheckBox(self,-1,"Mann-Whitney U",pos=(60,140))
        self.test3 = wx.CheckBox(self,-1,"Kolmogorov-Smirnov test",pos=(60,170))
        self.test4 = wx.CheckBox(self,-1,"F-test for variance ratio",pos=(60,200))
        self.test4.Enable(False)
        self.IVBox = wx.Choice(self,211, (324,100), (160,20), columnList)
        self.DVBox = wx.Choice(self,212, (324,170), (160,20), columnList)

class TestDialog(wx.Dialog):
    def __init__(self, columnList, testFlag = False):
        wx.Dialog.__init__(self, None, title="Analyse 2 or more conditions",\
                size=(700,425))
        self.testFlag = testFlag
        helpTop = "These tests allow you to compare two conditions for significant differences. "
        t1 = wx.StaticText(self,-1, label=helpTop, pos=(20,30),size=(-1,660))
        t1.Wrap(660)
        self.decider = wx.Notebook(self, -1, pos=(20,65), size=(660,290))
        self.betweenSubs = BetweenSubjectsClass(self.decider, columnList)
        self.withinSubs = WithinSubjectsClass(self.decider, columnList)
        self.decider.InsertPage(0, self.betweenSubs,"Between-subjects")
        self.decider.InsertPage(1, self.withinSubs,"Within-subjects")
        okayButton = wx.Button(self,211,"Analyse",pos=(540,360),size=(125,-1))
        cancelButton = wx.Button(self,212,"Cancel",pos=(390,360),size=(125,-1))
        okayButton.SetDefault()
        wx.EVT_BUTTON(self, 211, self.AnalyseButton)
        wx.EVT_BUTTON(self, 212, self.CancelButton)

    def AnalyseButton(self, event):
        page = self.decider.GetSelection()
        self.results = {}
        tests = []
        if page == 0: # between-subjects test chosen
            self.results["testType"] = 'between'
            if self.betweenSubs.test1.IsChecked():
                tests.append('ttestunpaired')
            if self.betweenSubs.test2.IsChecked():
                tests.append('mannwhitneyu')
            if self.betweenSubs.test3.IsChecked():
                tests.append('kolmogorov')
            if self.betweenSubs.test4.IsChecked():
                tests.append('ftest')
            val = self.betweenSubs.IVBox.GetSelection()
            if val != wx.NOT_FOUND:
                self.results["IV"] = [val]
            val = self.betweenSubs.DVBox.GetSelection()
            if val != wx.NOT_FOUND:
                self.results["DV"] = [val]
            self.results["tests"] = tests
        elif page == 1: # within-subjects tests
            self.results["testType"] = 'within'
            if self.withinSubs.test1.IsChecked():
                tests.append('ttestpaired')
            if self.withinSubs.test2.IsChecked():
                tests.append('wilcoxon')
            if self.withinSubs.test3.IsChecked():
                tests.append('pairedsign')
            self.results["IV"] = []
            self.results["DV"] = self.withinSubs.DVBox.GetChecked()
            self.results["tests"] = tests
        else:
            self.results = None
        self.Close()
        return self.results

    def CancelButton(self, event):
        self.Close()
        return None



#---------------------------------------------------------------------------
# main loop, just for testing
if __name__ == '__main__':
    cList = ['a','b','c']
    app = wx.App()
    frame = TestDialog(cList, testFlag=True)
    frame.Show(True)
    app.MainLoop()

    