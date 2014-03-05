import sys
from PyQt4 import QtGui

class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.WindowUI()
        
    def WindowUI(self):               

        gridNames = ["Phyics","Chemistry","Math","Biology","CS","EC"]

        vbox = QtGui.QVBoxLayout()
        j = 0
        vbox.addStretch(1)
        j = 0
        #pos = [(4,2), (6,2), (8,2), (10,2), (12,2),(14,2)]
        for i in gridNames:
            button = QtGui.QPushButton(i,self)
            #grid.addWidget(button)
            button.setCheckable(True)
            button.move(10,j+20)
            j += 30

        self.col = QtGui.QColor(0, 0, 0) 
        """
        j = 0
        for i in gridNames :
            if j < len(pos): #the position of the last button
                button = QtGui.QPushButton(i)
                grid.addWidget(button,pos[j][0],pos[j][0])
                j += 1
        """

        self.setLayout(vbox)
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  self.col.name())
        
        self.setGeometry(400, 400, 380, 270)
        self.setWindowTitle('Success Ladder')    
        self.show()
        
        #Exit the application Window entirely
        exitAction = QtGui.QAction(QtGui.QIcon('images/railings.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        """
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)  
        """   