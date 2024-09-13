class Calc:
    @staticmethod
    def sum(a, b):
        try:
            return a+b
        except Exception as error:
            print(error)
            return False

    @staticmethod
    def sub(a, b):
        try:
            return a-b
        except Exception as error:
            print(error)
            return False

    @staticmethod
    def mul(a, b):
        try:
            return a*b
        except Exception as error:
            print(error)
            return False

    @staticmethod
    def div(a, b):
        try:
            return a/b
        except Exception as error:
            print(error)
            return False


class Expression:
    def __init__(self, expression):
        self.expression = expression

    def __calculate(self, operator, a, b):
        if operator == "+":
            return Calc.sum(a, b)

        if operator == "-":
            return Calc.sub(a, b)

        if operator == "*":
            return Calc.mul(a, b)

        if operator == "/":
            return Calc.div(a, b)

    def __check_index(self, operator, array_expression):
        try:
            index = array_expression.index(operator)
            return index
        except ValueError:
            print(f"O operator '{operator}' não está na lista")
            return False

    def __calc_from_index(self, operator, array_expression):
        index = self.__check_index(operator, array_expression)

        if not index:
            return array_expression
        if type(index) is int:
            index = [index]

        i = index[0]
        index.pop(0)

        a = array_expression[i+1]
        b = array_expression[i-1]

        array_expression.pop(i-1)
        array_expression.pop(i-1)
        array_expression.pop(i-1)

        calc = self.__calculate(operator, float(a), float(b))
        array_expression.insert(i-1, calc)

        index = self.__check_index(operator, array_expression)

        if not index:
            return array_expression
        if type(index) is int:
            index = [index]

        if len(index) != 0:
            array_expression = self.__calc_from_index(operator, array_expression)

        return array_expression

    def __calc_operator(self, array_expression, operator):
        result = []

        result = self.__calc_from_index(operator, array_expression)

        return result

    def calc(self):
        array_expression = list(self.expression)

        result = self.__calc_operator(array_expression, "*")
        result = self.__calc_operator(result, "/")
        result = self.__calc_operator(result, "+")
        result = self.__calc_operator(result, "-")

        return result


if __name__ == "__main__":
    ex = Expression("2+2*1*1*1+1")
    print(ex.calc())
