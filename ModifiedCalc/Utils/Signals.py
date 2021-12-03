from PyQt5.QtCore import QObject, pyqtSignal
from Utils.Singleton import singleton


@singleton
class Signals(QObject):

    output_signal = pyqtSignal(str)
    clear_signal = pyqtSignal(str)
    step_signal = pyqtSignal(str)
    clear_step_signal = pyqtSignal()
    btn_border_signal = pyqtSignal(str, str)
    clear_border_signal = pyqtSignal(str, str)
