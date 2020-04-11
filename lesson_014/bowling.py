"""
This module calculates results of a game
@author: vndanilchenko@gmail.com
"""

class WrongSymbol(Exception):
    pass

class EmptyList(Exception):
    pass

class TooManySets(Exception):
    pass

class OverTenError(Exception):
    pass

class WrongSymbolsCountError(Exception):
    pass

class DoubleSlashError(Exception):
    pass

class ZerroExistsError(Exception):
    pass

class WrongFirstSymbolError(Exception):
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

        # проверим есть ли лишние символы в результате
        good_symbols = '123456789/-XХ'
        check_symbols = self.result
        for i in range(len(good_symbols)):
            check_symbols = str.replace(check_symbols, good_symbols[i], '')
        if len(check_symbols) > 0:
            raise WrongSymbol('undefined')

        # считаем количество потенциальных пар
        excl_strike = str.replace(self.result, 'Х', '')
        excl_strike = str.replace(excl_strike, 'X', '')
        if len(excl_strike):
            if len(excl_strike) % 2 != 0:
                raise WrongSymbolsCountError('\nне заполнен один из фреймов')

        # сразу просуммируем количество очков для X
        self.game_sum += 20 * (len(self.result) - len(excl_strike))
        self.qnty_sets += (len(self.result) - len(excl_strike))

        for i in range(0, len(excl_strike), 2):
            first_eval = str.replace(excl_strike[i:i+2], '-', '')
            # если были только --, то 0
            if len(first_eval) == 0:
                self.qnty_sets += 1
                continue
            # если был один -, то суммируем остальное число
            elif len(first_eval) == 1:
                if first_eval == '/':
                    self.game_sum += 15
                    self.qnty_sets += 1
                    continue
                else:
                    self.game_sum += int(first_eval)
                    self.qnty_sets += 1
                    continue
            else:
                # поищем /
                second_eval = str.replace(first_eval, '/', '')
                # если было два /, то ошибка
                if len(second_eval) == 0:
                    raise DoubleSlashError(i)
                elif len(second_eval) == 1:
                    # проверим на наличие / на первом месте
                    if first_eval[0] == '/':
                        raise WrongFirstSymbolError(i)
                    else:
                        self.game_sum += 15
                        self.qnty_sets += 1
                        continue
                else:
                    # проверим на все числа, отличные от 0
                    third_eval = str.replace(second_eval, '0', '')
                    # если было хотя бы один 0, то ошибка
                    if len(third_eval) < 2:
                        raise ZerroExistsError(i)
                    else:
                        flag_numeric = 0
                        for j in range(2):
                            if third_eval[j].isnumeric():
                                flag_numeric += 1
                        # проверим, что все числа, иначе ошибка
                        if flag_numeric == 2:
                            # проверим не больше ли 10 сумма очков
                            tmp_sum = sum(int(i) for i in third_eval)
                            if tmp_sum > 10:
                                raise OverTenError(i)
                            else:
                                self.game_sum += tmp_sum
                                self.qnty_sets += 1
                                continue
                        else:
                            raise WrongSymbol(i)
        if self.qnty_sets > 10:
            raise TooManySets(self.qnty_sets)

# вы исправили ошибку, а тесты не добавили...эта ошибка может опять появиться,
# для этого и нужны юнит тесты
# зачет!