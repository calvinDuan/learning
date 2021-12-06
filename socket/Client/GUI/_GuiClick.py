from GUI.UI.ChatClient import Ui_MainWindow
from Tools.Signals import Signals


class GuiClick:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._ui.btn_send.clicked.connect(self._send_msg)
        self._signal = Signals()

    def _send_msg(self):
        msg = self._ui.input_bar.text()
        self._ui.input_bar.clear()
        self._signal.send_signal.emit(msg)

