from PyQt5.QtCore import QObject, pyqtSignal
from Tools.Singleton import singleton

@singleton
class Signals(QObject):

    send_signal = pyqtSignal(str)
    display_signal = pyqtSignal(str)

