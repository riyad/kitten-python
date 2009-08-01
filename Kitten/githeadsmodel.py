# -*- coding: utf-8 -*-

from PyQt4.QtCore import *

from git import *

class GitHeadsModel(QAbstractTableModel):
  def __init__(self, repository, parent = None):
    QAbstractTableModel.__init__ (self, parent)
    self.repository = repository
    self.reset()

  def columnCount(self, parent = QModelIndex()):
    return 1

  def data(self, index, role = Qt.DisplayRole):
    if not index.isValid() or role != Qt.DisplayRole:
      return QVariant()
    else:
      return QVariant(self.heads[index.row()].name)

  def reset(self):
    self.heads = self.repository.heads
    QAbstractTableModel.reset(self)

  def rowCount(self, parent = QModelIndex()):
    return len(self.heads)
