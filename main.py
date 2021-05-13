import os
import sys

import qdarkstyle as qdarkstyle
from PySide2.QtWidgets import QApplication

from user_interface import MainWindow
# Run app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api=os.environ['PYQTGRAPH_QT_LIB']))
    window = MainWindow()
    window.show()
    app.exec_()
