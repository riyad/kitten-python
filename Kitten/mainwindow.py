# -*- coding: utf-8 -*-

from ui_mainwindow import Ui_MainWindow
from githeadsmodel import GitHeadsModel
from githistorymodel import GitHistoryModel

from PyKDE4.kdeui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from git import *

class MainWindow(KMainWindow):
  def __init__(self):
    KMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.connect(self.ui.action_OpenRepository, SIGNAL("triggered()"), self.openRepository)
    self.connect(self.ui.action_Quit, SIGNAL("triggered()"), KApplication.kApplication().quit)

    self.connect(self.ui.action_ReloadRepository, SIGNAL("triggered()"), self.reloadRepository)


  def initModels(self):
    self.disconnect(self.ui.branchComboBox, SIGNAL("currentIndexChanged(const QString&)"), self.branchChanged)
    headsModel = GitHeadsModel(self.repository, self.ui.branchComboBox)
    self.ui.branchComboBox.setModel(headsModel)
    self.connect(self.ui.branchComboBox, SIGNAL("currentIndexChanged(const QString&)"), self.branchChanged)

    historyModel = GitHistoryModel(self.repository, self.branch, self.ui.historyTableView)
    self.ui.historyTableView.setModel(historyModel)

  def openRepository(self):
    fd = QFileDialog(self)
    fd.setAcceptMode(QFileDialog.AcceptOpen)
    fd.setFileMode(QFileDialog.DirectoryOnly)
    self.repository_path = fd.getExistingDirectory().__str__()
    self.repository = Repo(self.repository_path)
    self.branch = 'master'

    self.initModels()
    self.reloadRepository()

  def reloadRepository(self):
    #self.ui.branchComboBox.model().reset()
    currentBranchIndex = self.ui.branchComboBox.findText(self.branch)
    self.ui.branchComboBox.setCurrentIndex(currentBranchIndex)

    self.ui.historyTableView.model().reset()

  def branchChanged(self, currentBranch):
    self.branch = currentBranch
    print "Switched to branch: %s" % currentBranch

    self.ui.historyTableView.model().setBranch(currentBranch)
