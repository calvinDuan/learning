import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.uic import loadUi


class Win(QMainWindow):
    value_signal = QtCore.pyqtSignal(int)
    sign_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self._ui = loadUi('calcPrac.ui', self)

        self.current_value = 0
        self.ans = 0
        self.is_clear = False
        self.is_dot = False
        self.current_key_type = None
        self.sign_list = list()
        self.ans_list = [0]
        self.btn_list = [self._ui.btn_eq, self._ui.btn_add, self._ui.btn_minus, self._ui.btn_mult, self._ui.btn_div,
                         self._ui.btn_mod]

        self._ui.output_screen.setText(str(self.ans))

        self._ui.btn_0.clicked.connect(self.get_key)
        self._ui.btn_1.clicked.connect(self.get_key)
        self._ui.btn_2.clicked.connect(self.get_key)
        self._ui.btn_3.clicked.connect(self.get_key)
        self._ui.btn_4.clicked.connect(self.get_key)
        self._ui.btn_5.clicked.connect(self.get_key)
        self._ui.btn_6.clicked.connect(self.get_key)
        self._ui.btn_7.clicked.connect(self.get_key)
        self._ui.btn_8.clicked.connect(self.get_key)
        self._ui.btn_9.clicked.connect(self.get_key)
        self._ui.btn_dot.clicked.connect(self.get_key)
        self._ui.btn_eq.clicked.connect(self.get_key)
        self._ui.btn_add.clicked.connect(self.get_key)
        self._ui.btn_minus.clicked.connect(self.get_key)
        self._ui.btn_mult.clicked.connect(self.get_key)
        self._ui.btn_div.clicked.connect(self.get_key)
        self._ui.btn_mod.clicked.connect(self.get_key)
        self._ui.btn_neg.clicked.connect(self.negative)
        self._ui.btn_clear.clicked.connect(self.clear_value)

        self.value_signal.connect(self.get_value)
        self.sign_signal.connect(self.calculate)

        self._ui.step_screen.itemDoubleClicked.connect(self.back_track)

        self.show()

    def get_key(self):
        self.is_clear = False
        self._ui.btn_clear.setText("Del")
        key = self.sender().objectName().split('_')
        if key[1].isnumeric():
            self.current_key_type = 'num'
            self.value_signal.emit(int(key[1]))
        elif key[1] == 'dot':
            if not self.is_dot:
                self.is_dot = True
                self._ui.output_screen.setText(str(self.current_value)+'.')
        else:
            for btn in self.btn_list:
                btn_name = btn.objectName().split('_')
                if btn_name[1] == key[1]:
                    if btn_name[1] == 'mod':
                        btn.setStyleSheet('color: rgb(7, 8, 6);'
                                          'background-color: rgb(239, 227, 193);'
                                          'border: 2px solid rgb(35, 247, 11);'
                                          'border-radius: 10px;')
                    else:
                        btn.setStyleSheet('background-color: rgb(246, 170, 11);'
                                          'border: 2px solid rgb(35, 247, 11);'
                                          'border-radius: 10px;')
                else:
                    if btn_name[1] == 'mod':
                        btn.setStyleSheet('color: rgb(7, 8, 6);'
                                          'background-color: rgb(239, 227, 193);'
                                          'border: 2px solid rgb(255, 255, 255);'
                                          'border-radius: 10px;')
                    else:
                        btn.setStyleSheet('background-color: rgb(246, 170, 11);'
                                          'border: 2px solid rgb(255, 255, 255);'
                                          'border-radius: 10px;')

            if self.current_key_type == 'num' or len(self.sign_list) == 0:
                self.current_key_type = 'sign'
                self.sign_list.append(key[1])
                self.sign_signal.emit()
            elif key[1] != 'eq':
                self.sign_list[-1] = key[1]
            elif key[1] == 'eq' and self.current_key_type == 'num' and len(self.sign_list) > 0:
                self.sign_signal.emit()

    def get_value(self, num: int):
        if not self.is_dot:
            self.current_value = self.current_value * 10 + num
            self._ui.output_screen.setText(str(self.current_value))

        else:
            num_str = self._ui.output_screen.text() + str(num)
            self.current_value = float(num_str)
            self._ui.output_screen.setText(num_str)

    def calculate(self):
        self.is_dot = False
        self.is_clear = False
        self._ui.btn_clear.setText("Del")
        if len(self.sign_list) > 1:
            if self.sign_list[-2] == 'eq':
                self.current_value = 0
                self._ui.output_screen.setText('Please include operator')
                return
            if self.sign_list[-2] == 'add':
                step = f'{self.ans} + {self.current_value}'
                self.ans += self.current_value
                if round(self.ans) == self.ans:
                    self.ans = round(self.ans)
                self.current_value = 0
                self.ans_list.append(self.ans)
            elif self.sign_list[-2] == 'minus':
                step = f'{self.ans} - {self.current_value}'
                self.ans -= self.current_value
                if round(self.ans) == self.ans:
                    self.ans = round(self.ans)
                self.current_value = 0
                self.ans_list.append(self.ans)
            elif self.sign_list[-2] == 'mult':
                step = f'{self.ans} * {self.current_value}'
                self.ans *= self.current_value
                if round(self.ans) == self.ans:
                    self.ans = round(self.ans)
                self.current_value = 0
                self.ans_list.append(self.ans)
            elif self.sign_list[-2] == 'div':
                if self.ans != 0:
                    step = f'{self.ans} / {self.current_value}'
                    self.ans /= self.current_value
                    self.ans = round(self.ans, 10)
                    if round(self.ans) == self.ans:
                        self.ans = round(self.ans)
                    self.current_value = 0
                    self.ans_list.append(self.ans)
            elif self.sign_list[-2] == 'mod':
                step = f'{self.ans} % {self.current_value}'
                self.ans = self.ans % self.current_value
                self.current_value = 0
                self.ans_list.append(self.ans)
            self._ui.output_screen.setText(str(self.ans))
            item = QListWidgetItem(step)
            self._ui.step_screen.addItem(item)
        else:
            self.ans = self.current_value
            self.current_value = 0

    def negative(self):
        if self.current_value != 0:
            self.current_value = -self.current_value
            if self.current_value < 0:
                self._ui.output_screen.setText('-' + self._ui.output_screen.text())
            else:
                self._ui.output_screen.setText(self._ui.output_screen.text()[1:])
        else:
            if self.ans != 0:
                self.ans = -self.ans
                if self.ans < 0:
                    self._ui.output_screen.setText('-' + self._ui.output_screen.text())
                else:
                    self._ui.output_screen.setText(self._ui.output_screen.text()[1:])

    def back_track(self):
        start_step = self._ui.step_screen.currentRow()
        end_step = self._ui.step_screen.count()
        for step in range(start_step+1, end_step):
            self._ui.step_screen.takeItem(start_step+1)
        self.ans_list = self.ans_list[:start_step+2]
        print(self.ans_list)
        self.current_value = 0
        self.ans = self.ans_list[-1]
        self._ui.output_screen.setText(str(self.ans))


    def clear_value(self):
        if not self.is_clear:
            self.is_clear = True
            self._ui.btn_clear.setText("Clear")
            self._ui.output_screen.clear()
            self.current_value = 0
            self.is_dot = False
        else:
            self.is_clear = False
            self._ui.btn_clear.setText("Del")
            self._ui.step_screen.clear()
            self.ans = 0
            self.sign_list = list()
            self.ans_list = [0]
            self._ui.output_screen.setText(str(self.ans))
            for btn in self.btn_list:
                btn_name = btn.objectName().split('_')
                if btn_name[1] == 'mod':
                    btn.setStyleSheet('color: rgb(7, 8, 6);'
                                      'background-color: rgb(239, 227, 193);'
                                      'border: 2px solid rgb(255, 255, 255);'
                                      'border-radius: 10px;')
                else:
                    btn.setStyleSheet('background-color: rgb(246, 170, 11);'
                                      'border: 2px solid rgb(255, 255, 255);'
                                      'border-radius: 10px;')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    sys.exit(app.exec_())