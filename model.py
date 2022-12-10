import random
import numexpr as ne


class ParenthesesTasks:

    def __init__(self, numbers_amount_limit, min_number, max_number):
        self.numbers_amount_limit = numbers_amount_limit
        self.min_number = min_number
        self.max_number = max_number

    def get_number(self, prev_number=100000, dividable=False):
        if dividable:
            while True:
                n = random.randint(self.min_number, min(self.max_number, prev_number))
                if n % prev_number == 0:
                    return n
        else:
            return random.randint(min(self.min_number, prev_number), min(self.max_number, prev_number))

    def get_task(self, filename):
        amount = random.randint(2, self.numbers_amount_limit)
        number = self.get_number()
        numbers = [number]
        s = str(number)
        s_expr = str(number)
        for i in range(1, amount):
            action = random.randint(0, 3)
            if action == 0:
                s += ' - '
                s_expr += '-'
            elif action == 1:
                s += ' + '
                s_expr += '+'
            elif action == 2:
                s += ' * '
                s_expr += '*'
            elif action == 3:
                s += ' : '
                s_expr += '/'

            if action == 0:
                number = self.get_number(numbers[-1])
            elif action == 3:
                number = self.get_number(numbers[-1], True)
            else:
                number = self.get_number()

            s += str(number)
            s_expr += str(number)
            numbers.append(number)

        answer = ne.evaluate(s_expr)

        with open(filename, 'a') as f:
            f.write('Task is ' + s + ' = ' + str(answer))
            f.write('\n')


        return s, answer

