# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    print(input_data[4])
    leeloo = int(input_data[4])
except ValueError as e:
    print(f'символ {(e.args[0].split()[-1])} невозможно преобразовать к числу ')
except IndexError as e:
    print(f'выход за границы списка ')
except:
    print('что-то пошло не так')

result = BRUCE_WILLIS * leeloo
print(f"- Leeloo Dallas! Multi-pass № {result}!")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
# зачет!