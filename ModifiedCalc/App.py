import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from Gui.UI import CalcUi
from Gui.Gui import Gui
from Operation.Calc import Calc


class Win(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = CalcUi.Ui_MainWindow()
        self._ui.setupUi(self)
        self._gui = Gui(ui=self._ui)
        self._calc = Calc(ui=self._ui)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())
