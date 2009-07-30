#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyKDE4.kdecore import *
from PyKDE4.kdeui import *

class MainWindow(KMainWindow):
  pass

appName = "kitten"
catalog = ""
programName = ki18n("Kitten")
version = "0.1"
description = ki18n("A Git GUI")
license = KAboutData.License_GPL_V3
copyright = ki18n("(c) 2009 Riyad Preukschas")
text = ki18n("none")
homePage = ""
bugEmail = ""

aboutData = KAboutData(appName, catalog, programName, version, description,
license, copyright, text, homePage, bugEmail)

#aboutData.addAuthor("Riyad Preukschas", ki18n("Author"), "riyad@informatik.uni-bremen.de")

KCmdLineArgs.init(sys.argv, aboutData)

app = KApplication()

kitten = MainWindow()
kitten.show()

sys.exit(app.exec_())
