import sys, os
from PyQt4 import QtGui
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

#This module will create subject specific window for our app.
#i (bharath) recommend this as, a student can open multiple windows,
#load the videos and watch them one after another. (he need not wait for buffering and all that)
#ping me at your own risk if you donot understand this!!

class WindowSubject(QtGui.QDialog):
    #define the names for the buttons and declare them here
    gridNames = ["Phyics","Chemistry","Math","Biology","CS","EC"]
    subjectProps = ["Videos","Assignments", "Other blah blah!"]

    def __init__(self):
        super(WindowSubject, self).__init__()
        
        self.WindowSubUI()
        
    def WindowSubUI(self):               

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        j = 0
        for i in self.subjectProps:
            button = QtGui.QPushButton(i,self)
            button.setCheckable(True)
            button.move(j+200, 10)
            j += 200
            button.clicked[bool].connect(self.selectSubTileWindow) 
       
        self.setLayout(hbox)
        #self.square = QtGui.QFrame(self) #might have to change this frame thing based on tile window implementation.
        # if tile window pops out another window for videos(which bharath recommends), then this can probably be removed
        self.showMaximized()
       
    def selectSubTileWindow(self, pressed):
        source = self.sender()
        #donot import this at the beginning, as the object
        #for SubjectWindow would not have been created and results in error!!
        #from SubjectWindow import WindowSubject

        if pressed : 
            val = 255
        else : val = 0

        print ("Code to link the tile windows here")
