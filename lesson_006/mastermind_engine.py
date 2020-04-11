# this module contains an engine of our game

import random

# план
# 1. создаем числа
# 2. получаем пользовательские числа и сравниваем с текущими
# - проходим индекс=индекс:
#     * совпадение - записываем индекс в список быков
#     * закончился цикл и длина списка быков меньше 4, то ищем остальные числа в списке и записываем в список коров
# 3. отдаем пользователю лину списка быков и длину списка коров
# 4. если все числа отгаданы, предлагаем сыграть снова или закончить
# - если да, то запускаем generate_numbers()
# - если нет, то заканчиваем

# lets create a list to hold our numbers
choice = []
MAX_NUM_LEN = 4
ANSWER_VARIANTS = ['да', 'нет', 'yes', 'no', 'y', 'n']

# сгенерируем число с заданной длиной
def generate_numbers():
    while True:
        samples = random.sample(range(0, 10), MAX_NUM_LEN)
        if samples[0] != 0:
            return samples

# проверка на длину входящего числа
def check_length(income_numbers):
    # Игрок вводит четырехзначное число c неповторяющимися цифрами
    while len(set(income_numbers))!=MAX_NUM_LEN and len(income_numbers) != MAX_NUM_LEN:
        if len(set(income_numbers))==0:
            print('enter unique numbers, should be {}'.format(MAX_NUM_LEN))
        else:
            print('wrong count of unique numbers, should be {}'.format(MAX_NUM_LEN))
        income_numbers = input('repaste please\n')
    else:
        pass
    return income_numbers

# проверка на выбор продолжения
def check_yes_no(answer):
    while answer not in ANSWER_VARIANTS:
        print('выберите что-то одно:{}'.format(ANSWER_VARIANTS))
        answer = input('repaste please\n')
    return answer

# сравниваем два числа
def compare_choice(income_numbers='1234', choice=[1,2,3,4]):
    income_numbers = check_length(income_numbers)
    bulls = []
    cows = []
    # print('income type ', type(income_numbers))
    # print('choice ', choice)
    # print('income ', income_numbers)
    for i in range(len(choice)):
        if int(income_numbers[i]) == choice[i]:
            bulls.append(i)
    if len(bulls)<len(choice):
        for i in range(len(choice)):
            if i not in bulls:
                if int(income_numbers[i]) in choice:
                    cows.append(i)
    print('bulls: {}, cows: {}'.format(len(bulls), len(cows)))
    return len(bulls), len(cows)

# compare_choice()?