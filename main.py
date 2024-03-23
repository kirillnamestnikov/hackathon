import sys
import os

from PyQt5.QtWidgets import QApplication

from app.widgets.MainWidget import HMainWIndow

if __name__ == "__main__":
    sys.path.append(os.path.dirname(sys.executable))
    sys.path.append(r"C:\Users\winte\source\repos\hackathon")

    qtApp = QApplication(sys.argv)
    mwidget = HMainWIndow()
    mwidget.show()
    qtApp.exec_()