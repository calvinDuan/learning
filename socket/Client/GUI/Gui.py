from GUI.UI.ChatClient import Ui_MainWindow
from GUI._GuiClick import GuiClick
from GUI._GuiDisplay import GuiDisplay


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._gui_click = GuiClick(ui=ui)
        self._gui_display = GuiDisplay(ui=ui)