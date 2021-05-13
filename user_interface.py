# Imports
import os

from PySide2.QtWidgets import QMainWindow, QPushButton, QFileDialog, QDialog

from luts_apply.luts_func import get_all_LUTS, generate_photos_with_applied_filter

os.environ['PYQTGRAPH_QT_LIB'] = 'PySide2'


# Create class which handle GUI
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LUT applier")
        button = QPushButton("Select Photo")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(button)

    # Function which generate photos with applied LUTS and close app after selected photo
    def the_button_was_clicked(self):
        filter = 'JPEG (*.jpg *.jpeg)'
        file = QFileDialog(self, filter)
        self.setCentralWidget(file)
        if file.exec_() == QDialog.Accepted:
            path = file.selectedFiles()[0]  # returns a list
            luts_to_use = get_all_LUTS()
            generate_photos_with_applied_filter(luts_to_use, path)
            self.close()
