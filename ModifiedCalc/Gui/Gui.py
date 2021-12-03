from Gui.UI.CalcUi import Ui_MainWindow
from Gui._GuiClick import GuiClick
from Gui._GuiOutput import GuiOutput


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._gui_click = GuiClick(ui=ui)
        self._gui_output = GuiOutput(ui=ui)
