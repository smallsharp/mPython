#coding=utf-8


"""
Py40 PyQt5 tutorial

This example shows three labels on a window
using absolute positioning.

author: Jan Bodnar
website: py40.com
last edited: January 2015

绝对定位

程序指定每个控件的位置和大小(以像素为单位)。

绝对定位有以下限制:

如果我们调整窗口，控件的大小和位置不会改变
在各种平台上应用程序看起来会不一样
如果改变字体，我们的应用程序的布局就会改变
如果我们决定改变我们的布局,我们必须完全重做我们的布局
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())