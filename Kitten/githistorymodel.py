# -*- coding: utf-8 -*-

from PyQt4.QtCore import *

from git import *

class GitHistoryModel(QAbstractTableModel):
  columns = ('Summary', 'Author', 'Date', 'Id')
  column_mapping = {'Summary': 'summary', 'Author': 'author', 'Date': 'authored_date', 'Id': 'id_abbrev'}

  def __init__(self, repository, parent = None):
    QAbstractTableModel.__init__ (self, parent)
    self.repository = repository
    self.commits = []
    self.branch = 'master'

  def columnCount(self, parent = QModelIndex()):
    return len(self.columns)

  def columnName(self, column):
    return self.columns[column]

  def data(self, index, role = Qt.DisplayRole):
    if not index.isValid() or role != Qt.DisplayRole:
      return QVariant()
    else:
      return QVariant(getattr(self.commits[index.row()], self.column_mapping[self.columnName(index.column())]))

  def headerData(self, section, orientation, role = Qt.DisplayRole):
    if orientation != Qt.Horizontal or role != Qt.DisplayRole:
      return QVariant()
    else:
      return QVariant(self.columnName(section))

  def loadCommits(self):
    self.commits = Commit.find_all(self.repository, self.branch)

  def reset(self):
    self.commits = []
    self.loadCommits()
    QAbstractTableModel.reset(self)

  def rowCount(self, parent = QModelIndex()):
    return len(self.commits)

  def setBranch(self, currentBranch):
    self.branch = currentBranch
    self.reset()
