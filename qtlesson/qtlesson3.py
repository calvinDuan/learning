import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class Win(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('qtlesson3.ui', self)

        self._ui.btn_add.clicked.connect(self.add_method)


        self.show()

    def add_method(self):



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    sys.exit(app.exec_())