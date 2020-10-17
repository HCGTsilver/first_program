from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
import sys

# Learning and experimenting with PyQt5

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 300)
        self.setWindowTitle("Upload File")
        self.setWindowIcon(QtGui.QIcon('CircleBubbles.png'))

        extractAction = QtWidgets.QAction("&CLICK TO QUIT", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label goes here")
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Browse")
        self.button1.clicked.connect(self.clicked)
        self.button1.move(0, 100)

        extractAction = QtWidgets.QAction(QtGui.QIcon('BLeaves.png'), "Flee", self)
        extractAction.triggered.connect(self.close_application)

        self.toobar = self.addToolBar("Extraction")
        self.toobar.addAction(extractAction)

        checkBox = QtWidgets.QCheckBox ("Increase Window Size", self)
        checkBox.move(100, 25)
        #checkBox.toggle() if you want to start it checked, but then switch conditional logic in enlarge_window
        checkBox.stateChanged.connect(self.enlarge_window)

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def close_application(self):
        confirmation = QtWidgets.QMessageBox.question(self, "Leave",
                                                  "Are you sure you want to quit?",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirmation == QtWidgets.QMessageBox.Yes:
            print("Exiting Application...")
            sys.exit()
        else:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
