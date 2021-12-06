import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI.UI.ChatClient import Ui_MainWindow
from ClientNode.ChatClient import ChatClient
from GUI.Gui import Gui


class Win(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._gui = Gui(ui=self._ui)
        self._client = ChatClient()
        self._client.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())
