import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class MyForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('qtlesson1.ui', self)

        self._ui.btn_calc.clicked.connect(self.calc_method)
        self._ui.btn_clear.clicked.connect(lambda: self._ui.label_sum.clear())

        self.show()

    def calc_method(self):
        num1 = int(self._ui.line_edit_1.text())
        num2 = int(self._ui.line_edit_2.text())
        sum = num1 + num2
        self._ui.label_sum.setText(str(sum))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    sys.exit(app.exec_())