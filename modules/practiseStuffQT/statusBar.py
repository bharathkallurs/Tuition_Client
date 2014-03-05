import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.WindowUI()
        
    def WindowUI(self, statusMessage='Ready'):               
        #Pass the message a parameter to this function
        #default value will be StatuString.        
        self.statusBar().showMessage(statusMessage)
        
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Statusbar')    
        self.show()
