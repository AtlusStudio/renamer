import re
from PySide6.QtCore import QObject, Signal


class Calculator(QObject):
    result_calculated = Signal(float)

    def __init__(self, input_box):
        super().__init__()
        self.input_box = input_box

    def calculate(self):
        expression = self.get_expression()
        result = self.evaluate_expression(expression)
        self.result_calculated.emit(result)

    def get_expression(self):
        return self.input_box.text()

    def evaluate_expression(self, expression):
        try:
            pattern = r'(\d+)\s*([+-/*])\s*(\d+)'
            matches = re.findall(pattern, expression)
            if matches:
                num1, operator, num2 = matches[0]
                num1 = int(num1)
                num2 = int(num2)
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    result = num1 / num2
                else:
                    raise ValueError("Invalid operator")
                return result
            else:
                raise ValueError("Invalid expression")
        except Exception as e:
            return str(e)
