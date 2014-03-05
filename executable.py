import sys, os
#This is to solve the path kirik! don't worry "all is well here :)"
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/modules')
from MainWindow import WindowMain
from PyQt4 import QtGui

#This is the driver program which we will execute!!
#please keep this AS SIMPLE AS POSSIBLE
#put all your code in separate modules in modules folder, and make sure that,
#you give names to modules and classes meaningfully or atleast something which we can grasp in a go!
#Link all those modules internally and try your limits to avoid creating objects for them here in main code!
#Let the main code have only, WindowMainObject and nothing else! let us make this is clean..
def main():
    
    app = QtGui.QApplication(sys.argv)
    #WindowSubObject = WindowSubject()
    WindowMainObject = WindowMain()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()