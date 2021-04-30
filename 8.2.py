class ZeroError(Exception):
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide_by_null(dividend, divider):
        try:
            return dividend / divider
        except:
            return (f"Деление на ноль недопустимо")
