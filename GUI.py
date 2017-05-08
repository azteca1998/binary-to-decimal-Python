#!/usr/bin/env python3
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import binarytodecimal
if __name__ == "__main__":
# Create an PyQT5 application object.
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
    textbox1 = QLineEdit(w)
    textbox1.move(20, 20)
    textbox1.resize(280,40)

    textbox1.textChanged.connect(binarytodecimal.decimal)
    
    textbox2 = QLineEdit(w)
    textbox2.move(20, 20)
    textbox2.resize(280,40)

    textbox2.textChanged.connect(binarytodecimal.binary)


    w.show()

    sys.exit(a.exec_())

