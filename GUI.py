#!/usr/bin/env python3
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import binarytodecimal
if __name__ == "__main__":
    # Create an PyQT4 application object.
    a = QApplication(sys.argv)
     
    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()
     
    # Set window size.
    w.resize(320, 240)
     
    # Set window title
    w.setWindowTitle("GUI!")

    btn = QPushButton('Hello World!', w)
    btn.setToolTip('Click to quit!')
    btn.clicked.connect(exit)
    btn.resize(btn.sizeHint())
    btn.move(100, 100)

     # Create textbox
    textbox = QLineEdit(w)
    textbox.move(20, 20)
    textbox.resize(280,40)
    textbox.textChanged.connect(binarytodecimal.decimal())

    # vull que 

    w.show()
     
    sys.exit(a.exec_())

