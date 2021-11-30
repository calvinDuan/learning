from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from EvenOdd import Ui_mainWindow
import threading
import time


class Win(QMainWindow):
    spin_signal_even = QtCore.pyqtSignal(bool, int)
    spin_signal_odd = QtCore.pyqtSignal(bool, int)

    def __init__(self):
        super(Win, self).__init__()
        self._ui = Ui_mainWindow()
        self._ui.setupUi(self)

        self.even_stopped = False
        self.odd_stopped = False

        # create thread for two display tasks
        self.even_thread = threading.Thread()
        self.odd_thread = threading.Thread()

        # keep track of the current value
        self.cur_even = 1
        self.cur_odd = 0

        # start and stop buttons
        self._ui.even_start.clicked.connect(self.start_worker_even)
        self._ui.odd_start.clicked.connect(self.start_worker_odd)
        self._ui.even_stop.clicked.connect(self.stop_worker_even)
        self._ui.odd_stop.clicked.connect(self.stop_worker_odd)

        self.spin_signal_odd.connect(self.update_display)
        self.spin_signal_even.connect(self.update_display)

        self._ui.spinbox_even.setMinimum(1)
        self._ui.spinbox_odd.setMinimum(1)

    def start_worker_even(self):
        if self.even_stopped:
            self._ui.text_browser_even.clear()
        if not self.even_thread.is_alive():
            self.even_stopped = False
            self._ui.even_start.setEnabled(False)
            self.even_thread = threading.Thread(target=self.display_num, args=[True])
            self.even_thread.start()
        else:
            pass

    def start_worker_odd(self):
        if self.odd_stopped:
            self._ui.text_browser_odd.clear()
        if not self.odd_thread.is_alive():
            self.odd_stopped = False
            self._ui.odd_start.setEnabled(False)
            self.odd_thread = threading.Thread(target=self.display_num, args=[False])
            self.odd_thread.start()

    def stop_worker_even(self):
        self._ui.even_start.setEnabled(True)
        self.even_stopped = True
        self.cur_even = 1

    def stop_worker_odd(self):
        self._ui.odd_start.setEnabled(True)
        self.odd_stopped = True
        self.cur_odd = 0

    def display_num(self, is_even: bool):
        if is_even:
            for num in range(1, 100):
                if self.even_stopped:
                    return
                sleep_time = round(2 / self._ui.spinbox_even.value(), 2)
                if num % 2 == 0:
                    if self.even_stopped:
                        return
                    time.sleep(sleep_time)
                    if self.even_stopped:
                        return
                    self.spin_signal_even.emit(True, num)
                    if self.even_stopped:
                        return
        else:
            for num in range(1, 100):
                if self.odd_stopped:
                    return
                sleep_time = round(2 / self._ui.spinbox_odd.value(), 2)
                if num % 2 != 0:
                    if self.odd_stopped:
                        return
                    time.sleep(sleep_time)
                    if self.odd_stopped:
                        return
                    self.spin_signal_odd.emit(False, num)
                    if self.odd_stopped:
                        return

    def update_display(self, is_even: bool, num: int):
        if is_even:
            self._ui.text_browser_even.append(str(num))
            self.cur_even = num
        else:
            self._ui.text_browser_odd.append(str(num))
            self.cur_odd = num


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())
