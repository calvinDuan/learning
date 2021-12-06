from GUI.UI.ChatClient import Ui_MainWindow
from Tools.Signals import Signals


class GuiDisplay:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._signals = Signals()

        self._signals.display_signal.connect(self._display)

    def _display(self, msg: str):
        self._ui.output_screen.append(msg)


