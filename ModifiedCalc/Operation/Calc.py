from Utils.Singleton import singleton
from Utils.Signals import Signals
from Utils.Const import CONST
from Gui.UI.CalcUi import Ui_MainWindow


@singleton
class Calc:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._current_value = 0
        self._ans = 0
        self._ans_list = [0]
        self._is_dot = False
        self._is_clear = False
        self.display_ans = True
        self._current_key_type = ''
        self._current_op_btn = ''
        self._prev_op_btn = ''
        self._sign_list = list()

        self.signal = Signals()

    def set_dot(self):
        if not self._is_dot:
            self._is_dot = True
            output = str(self._current_value)+'.'
            self._current_value = float(self._current_value)
            self.signal.output_signal.emit(output)

    def get_value(self, num: int):
        self.display_ans = False
        self._current_key_type = 'num'
        if not self._is_dot:
            self._current_value = self._current_value * 10 + num
        else:
            temp_val = self._current_value
            temp_str_val = str(temp_val)
            temp_str_digit = temp_str_val.split('.')
            if temp_str_digit[1] == '0':
                temp_str_val = temp_str_val[:-1] + str(num)
            else:
                temp_str_val = temp_str_val + str(num)
            self._current_value = float(temp_str_val)
        output = str(self._current_value)
        btn_text = 'Del'
        self._is_clear = False
        self.signal.output_signal.emit(output)
        self.signal.clear_signal.emit(btn_text)

    def clear_value(self):
        if not self._is_clear:
            self._is_clear = True
            self._current_value = 0
            self._is_dot = False
            output = '0'
            btn_text = 'Clear'
            self.signal.output_signal.emit(output)
            self.signal.clear_signal.emit(btn_text)
        else:
            self._is_clear = False
            self._ans = 0
            output = '0'
            btn_text = 'Del'
            self._sign_list = list()
            self.signal.output_signal.emit(output)
            self.signal.clear_signal.emit(btn_text)
            self.signal.clear_step_signal.emit()
            self.signal.clear_border_signal.emit(self._prev_op_btn, self._current_op_btn)
            self._prev_op_btn = ''
            self._current_op_btn = ''

    def negative(self):
        if not self.display_ans:
            if self._current_value != 0:
                self._current_value = -self._current_value
            output = str(self._current_value)
        else:
            if self._ans != 0:
                self._ans = -self._ans
            output = str(self._ans)
        self.signal.output_signal.emit(output)

    def update_operator(self, operator: str):
        self._is_dot = False
        self._is_clear = False
        btn_text = 'Del'
        self._prev_op_btn = self._current_op_btn
        self._current_op_btn = operator
        self.signal.btn_border_signal.emit(self._prev_op_btn, self._current_op_btn)
        self.signal.clear_signal.emit(btn_text)
        if self._current_key_type == 'num' and len(self._sign_list) > 0 and self._sign_list[-1] == CONST.EQUAL:
            self._ans = self._current_value
            self._current_value = 0
            self._sign_list = [operator]
        elif self._current_key_type == 'num' or len(self._sign_list) == 0:
            self._current_key_type = 'sign'
            self._sign_list.append(operator)
            self.calculate()
        elif operator != CONST.EQUAL:
            self._sign_list[-1] = operator
        else:
            self.calculate()

    def calculate(self):
        if len(self._sign_list) > 1:
            formula = [str(self._ans), self._sign_list[-2], str(self._current_value)]
            str_formula = ''.join(formula)
            self._current_value = 0
            try:
                self._ans = eval(str_formula)
            except ZeroDivisionError:
                output = 'Not a Number'
                self.signal.output_signal.emit(output)
                return
            output = str(self._ans)
            self.display_ans = True
            self._ans_list.append(self._ans)
            self.signal.step_signal.emit(str_formula)
            self.signal.output_signal.emit(output)
        else:
            self._ans = self._current_value
            self._current_value = 0
            output = str(self._ans)
            self.signal.output_signal.emit(output)

    def back_track(self):
        start_step = self._ui.step_screen.currentRow()
        end_step = self._ui.step_screen.count()
        for step in range(start_step+1, end_step):
            self._ui.step_screen.takeItem(start_step+1)
        self._ans_list = self._ans_list[:start_step+2]
        self._current_value = 0
        self._ans = self._ans_list[-1]
        output = str(self._ans)
        self.signal.output_signal.emit(output)
