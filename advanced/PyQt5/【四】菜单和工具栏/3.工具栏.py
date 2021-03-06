#coding=utf-8
"""
Py40 PyQt5 tutorial

This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.
,我们创建一个简单的工具栏。工具栏有有一个按钮,点击关闭窗口。
author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('../exit.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        # exitAction.triggered.connect(self.printOk)

        # 创建一个简单的工具栏
        self.toolbar = self.addToolBar('Exit')

        # 添加事件
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

    def printOk(self):
        print("ok")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())