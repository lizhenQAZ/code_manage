import sys
import os
import win32api
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        for line in range(10):
            qlb11 = QLabel('APP' + str(line + 1), self)
            qbtn1 = QPushButton('Start', self)
            qbtn1.clicked.connect(self.start)
            qbtn2 = QPushButton('Stop', self)
            qbtn2.clicked.connect(self.stop)
            grid.addWidget(qlb11, *(line, 0))
            grid.addWidget(qbtn1, *(line, 1))
            grid.addWidget(qbtn2, *(line, 2))
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Quick Start')
        self.setWindowIcon(QIcon("E4_Dance.jpg"))
        self.show()

    def center(self):
        fg = self.frameGeometry()
        qdwc = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(qdwc)
        self.move(fg.topLeft())

    def start(self):
        win32api.ShellExecute(0, 'open', 'F:\Xshell5\Xshell.exe', '', '', 1)
        # subprocess.Popen("F:\Xshell5\Xshell.exe")

    def stop(self):
        os.system("taskkill /F /IM Xshell.exe")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
