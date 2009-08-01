# -*- coding: utf-8 -*-

from ui_mainwindow import Ui_MainWindow
from githistorymodel import GitHistoryModel

from PyKDE4.kdeui import KMainWindow

class MainWindow(KMainWindow):
  def __init__(self):
    KMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    historyModel = GitHistoryModel(parent = self.ui.historyTableView)
    self.ui.historyTableView.setModel(historyModel)
