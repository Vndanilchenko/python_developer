"""
This module calculates results of a game
@author: vndanilchenko@gmail.com
"""

class WrongSymbol(Exception):
    pass

class DoubleSymbols(Exception):
    pass

class EmptyList(Exception):
    pass

class BadLastSymbol(Exception):
    pass

class TooManySets(Exception):
    pass

class WrongFirstSymbol(Exception):
    pass

class OverTenError(Exception):
    pass

class WrongSymbolsCountError(Exception):
    pass

class CalculateResult:

    def __init__(self, result, name):
        self.game_sum = 0
        self.qnty_sets = 0
        if result:
            self.result = result.upper()
        # пустой список
        else:
            raise EmptyList('не передан результат')
        self.name = name

    def run(self):
        # считаем количество потенциальных пар
        temp_len = str.replace(self.result, 'Х', '')
        temp_len = len(str.replace(temp_len, 'X', ''))
        if temp_len:
            if temp_len % 2 != 0:
                raise WrongSymbolsCountError('\nне заполнен один из фреймов')

        is_frame = 0

        for i in range(len(self.result)):
            if is_frame == 1:
                # if i <= len(self.result):
                    # i += 1
                is_frame = 0
            tmp_char = self.result[i]
            # слишком много сетов
            if self.qnty_sets > 10:
                raise TooManySets(self.qnty_sets)
            if self.result[i] not in {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'Х', '/', '-'}:  # TODO 0 не валидный символ
                raise WrongSymbol(self.result[i])
            # страйк
            if self.result[i]=='Х' or self.result[i]=='X':
                self.game_sum += 20
                self.qnty_sets += 1
                is_frame = 1
                # i -= 2
                continue
            # был разделитель
            elif self.result[i] == '/':
                # вместо самого первого символа
                if i == 0:
                    raise WrongFirstSymbol('/')
                # вообще
                else:
                    pass
            elif (self.result[i]=='-' or self.result[i].isnumeric()) and i != 0:
                if self.result[i-1]=='-':
                    if is_frame == 0:
                        is_frame = 1
                        continue
            # если это не последний символ
            if i < len(self.result)-1:
                if self.result[i] == '/':
                    if self.result[i+1] == '/':
                        raise DoubleSymbols(self.result[i])
                elif self.result[i].isnumeric() and is_frame == 0:
                    if self.result[i+1] == '/':
                        self.game_sum += 15
                        self.qnty_sets += 1
                        is_frame = 1
                        continue
                    elif self.result[i+1] == '-':
                        self.game_sum += int(self.result[i])
                        self.qnty_sets += 1
                        is_frame = 1
                        continue
                    elif self.result[i+1].isnumeric():
                        temp_sum = int(self.result[i]) + int(self.result[i + 1])
                        if temp_sum > 10:
                            raise OverTenError('сумма очков больше 10: %i' % temp_sum)
                        else:
                            self.game_sum += temp_sum
                            self.qnty_sets += 1
                            is_frame = 1
                            continue
                elif self.result[i]=='-':
                    if is_frame == 0:
                        if self.result[i + 1].isnumeric():
                            self.game_sum += int(self.result[i + 1])
                            self.qnty_sets += 1
                            is_frame = 1
                            continue
                        elif self.result[i + 1] == '-':
                            self.qnty_sets += 1
                            is_frame = 1
                            continue
            # # особая обработка последнего символа
            # elif i == len(self.result):
            #     # считаем что после такого символа всегода должна идти цифра (даже 0)
            #     if is_frame == 0:
            #         raise BadLastSymbol('нельзя использовать "-" вконце')

# TODO ваше решение считает следующие валидные данные неправильными
# "11--11"
# "111-"
#
# CalculateResult("11--11", "aaa").run()



