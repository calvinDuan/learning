import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class Win(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('qtlesson2.ui', self)

        self._ui.rb_reg_cut.clicked.connect(self.calc_total)
        self._ui.rb_senior_cut.clicked.connect(self.calc_total)
        self._ui.cb_shave.clicked.connect(self.calc_total)
        self._ui.cb_trim.clicked.connect(self.calc_total)
        self._ui.cb_beard.clicked.connect(self.calc_total)

        self.show()

    def calc_total(self):
        total = 0
        if self._ui.rb_reg_cut.isChecked():
            total += 15
        elif self._ui.rb_senior_cut.isChecked():
            total += 13
        if self._ui.cb_shave.isChecked():
            total += 4
        if self._ui.cb_trim.isChecked():
            total += 2
        if self._ui.cb_beard.isChecked():
            total += 4
        self._ui.label_cost.setText(f'Total Cost Is ${str(total)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    sys.exit(app.exec_())