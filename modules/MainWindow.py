import sys, os
from PyQt4 import QtGui
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from SubjectWindow import WindowSubject

#This module is gonna create a main window for our application where
#subjects and other "kaage" will fly.

class WindowMain(QtGui.QWidget):
    #define the names for the buttons and declare them here
    gridNames = ["Phyics","Chemistry","Math","Biology","CS","EC"]

    def __init__(self):
        super(WindowMain, self).__init__()
        
        self.WindowMainUI()
        
    def WindowMainUI(self):               

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)

        j = 0
        for i in self.gridNames:
            button = QtGui.QPushButton(i,self)
            button.setCheckable(True)
            button.move(10,j+20)
            j += 30
            button.clicked[bool].connect(self.selectSubWindow)

        self.col = QtGui.QColor(0, 0, 0) 
       
        self.setLayout(vbox)
        self.square = QtGui.QFrame(self)
        #just was trying if i can load the inital subject window inside a frame in the main window.
        #if possible will modify this code accordingly. But as said earlier, hope that need doesnt really arise
        self.square.setGeometry(150, 20, 100, 100)
        self.showMaximized()
        #self.setGeometry(400, 400, 380, 270)
        self.setWindowTitle('Success Ladder')    
        self.show()
        
        #Exit the application Window entirely
        exitAction = QtGui.QAction(QtGui.QIcon('images/railings.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close) 

    def selectSubWindow(self, pressed):
        source = self.sender()
        #donot import this at the beginning, as the object
        #for SubjectWindow would not have been created and results in error!!
        #from SubjectWindow import WindowSubject

        if pressed : 
            val = 255
        else : val = 0 

        for subject in self.gridNames :
            if subject == source.text() :
                WindowSubObject = WindowSubject()
                WindowSubObject.exec_()