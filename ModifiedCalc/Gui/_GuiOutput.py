from Utils.Signals import Signals
from Gui.UI.CalcUi import Ui_MainWindow
from PyQt5.QtWidgets import QListWidgetItem
from Utils.Const import CONST


class GuiOutput:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._signal = Signals()
        self._signal.output_signal.connect(self._output_screen)
        self._signal.clear_signal.connect(self._set_btn_text)
        self._signal.step_signal.connect(self._step_screen)
        self._signal.clear_step_signal.connect(self._ui.step_screen.clear)
        self._signal.btn_border_signal.connect(self._set_border_color)
        self._signal.clear_border_signal.connect(self._clear_border_color)

        self.btn_map = {CONST.PLUS: self._ui.btn_add, CONST.MINUS: self._ui.btn_minus,
                        CONST.MULTIPLY: self._ui.btn_mult, CONST.DIVISION: self._ui.btn_div,
                        CONST.MODULO: self._ui.btn_mod, CONST.EQUAL: self._ui.btn_eq}

    def _output_screen(self, output: str):
        self._ui.output_screen.setText(output)

    def _step_screen(self, output: str):
        item = QListWidgetItem(output)
        self._ui.step_screen.addItem(item)

    def _set_btn_text(self, btn_text: str):
        self._ui.btn_clear.setText(btn_text)

    def _set_border_color(self, prev_btn: str, current_btn: str):
        if prev_btn != '':
            if prev_btn == CONST.MODULO:
                self.btn_map[prev_btn].setStyleSheet('color: rgb(7, 8, 6);'
                                                     'background-color: rgb(239, 227, 193);'
                                                     'border: 2px solid rgb(255, 255, 255);'
                                                     'border-radius: 10px;')
            else:
                self.btn_map[prev_btn].setStyleSheet('background-color: rgb(246, 170, 11);'
                                                     'border: 2px solid rgb(255, 255, 255);'
                                                     'border-radius: 10px;')
        if current_btn == CONST.MODULO:
            self.btn_map[current_btn].setStyleSheet('color: rgb(7, 8, 6);'
                                                    'background-color: rgb(239, 227, 193);'
                                                    'border: 2px solid rgb(35, 247, 11);'
                                                    'border-radius: 10px;')
        else:
            self.btn_map[current_btn].setStyleSheet('background-color: rgb(246, 170, 11);'
                                                    'border: 2px solid rgb(35, 247, 11);'
                                                    'border-radius: 10px;')

    def _clear_border_color(self, prev_btn: str, current_btn: str):
        if prev_btn != '':
            if prev_btn == CONST.MODULO:
                self.btn_map[prev_btn].setStyleSheet('color: rgb(7, 8, 6);'
                                                     'background-color: rgb(239, 227, 193);'
                                                     'border: 2px solid rgb(255, 255, 255);'
                                                     'border-radius: 10px;')
            else:
                self.btn_map[prev_btn].setStyleSheet('background-color: rgb(246, 170, 11);'
                                                     'border: 2px solid rgb(255, 255, 255);'
                                                     'border-radius: 10px;')
        if current_btn == CONST.MODULO:
            self.btn_map[current_btn].setStyleSheet('color: rgb(7, 8, 6);'
                                                    'background-color: rgb(239, 227, 193);'
                                                    'border: 2px solid rgb(255, 255, 255);'
                                                    'border-radius: 10px;')
        else:
            self.btn_map[current_btn].setStyleSheet('background-color: rgb(246, 170, 11);'
                                                    'border: 2px solid rgb(255, 255, 255);'
                                                    'border-radius: 10px;')
