# -*- coding: utf-8 -*-

from PyQt4.QtCore import *

from git import *

class GitHistoryModel(QAbstractTableModel):
  def __init__(self, repo_path = "", branch = "master", parent = None):
    QAbstractTableModel.__init__ (self, parent)
    self.repository = Repo(repo_path)
    self.branch = branch
    self.columnNames = ("Summary", "Author", "Date", "Id")

  def columnCount(self, parent = QModelIndex()):
    return len(self.columnNames)

  def data(self, index, role = Qt.DisplayRole):
    if not index.isValid() or role != Qt.DisplayRole:
      return QVariant()
    else:
      commit = self.repository.commits(start = self.branch, max_count = 1, skip = index.row())[0]
      column = index.column()
      if column == 0:
        return QVariant(commit.summary)
      elif column == 1:
        return QVariant(commit.author)
      elif column == 2:
        return QVariant(commit.authored_date)
      elif column == 3:
        return QVariant(commit.id_abbrev)
      else:
        return QVariant()

  def headerData(self, section, orientation, role = Qt.DisplayRole):
    if orientation != Qt.Horizontal or role != Qt.DisplayRole:
      return QVariant()
    else:
      return QVariant(self.columnNames[section])

  def rowCount(self, parent = QModelIndex()):
    return self.repository.commit_count(self.branch)
