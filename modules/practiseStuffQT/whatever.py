from PyQt4.QtCore import *
from PyQt4.QtGui  import *

import sys

class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget) 


class FormWidget(QWidget):

    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

app = QApplication([])
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())