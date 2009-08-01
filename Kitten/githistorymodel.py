# -*- coding: utf-8 -*-

from PyQt4.QtCore import *

from git import *

class GitHistoryModel(QAbstractTableModel):
  columns = ('Summary', 'Author', 'Date', 'Id')
  column_mapping = {'Summary': 'summary', 'Author': 'author', 'Date': 'authored_date', 'Id': 'id_abbrev'}

  def __init__(self, repository, branch = 'master', parent = None):
    QAbstractTableModel.__init__ (self, parent)
    self.repository = repository
    self.branch = branch
    self.reset()

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

  def reset(self):
    self.commits = self.repository.commits(start = self.branch, max_count = self.rowCount())
    QAbstractTableModel.reset(self)

  def rowCount(self, parent = QModelIndex()):
    return self.repository.commit_count(self.branch)
