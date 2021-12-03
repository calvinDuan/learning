from Gui.UI.CalcUi import Ui_MainWindow
from Operation.Calc import Calc
from Utils.Const import CONST


class GuiClick:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._calc = Calc(ui=ui)

        self.num_btn = {0: self._ui.btn_0, 1: self._ui.btn_1, 2: self._ui.btn_2, 3: self._ui.btn_3,
                        4: self._ui.btn_4, 5: self._ui.btn_5, 6: self._ui.btn_6, 7: self._ui.btn_7,
                        8: self._ui.btn_8, 9: self._ui.btn_9}
        for num, btn in self.num_btn.items():
            btn.clicked.connect(lambda checked, n=num: self._calc.get_value(num=n))

        self.num_operator = {CONST.PLUS: self._ui.btn_add, CONST.MINUS: self._ui.btn_minus,
                             CONST.MULTIPLY: self._ui.btn_mult, CONST.DIVISION: self._ui.btn_div,
                             CONST.MODULO: self._ui.btn_mod, CONST.EQUAL: self._ui.btn_eq}

        for operator, op_btn in self.num_operator.items():
            op_btn.clicked.connect(lambda checked, op=operator: self._calc.update_operator(operator=op))

        self._ui.btn_dot.clicked.connect(self._calc.set_dot)
        self._ui.btn_clear.clicked.connect(self._calc.clear_value)
        self._ui.btn_neg.clicked.connect(self._calc.negative)

        self._ui.step_screen.itemDoubleClicked.connect(self._calc.back_track)
