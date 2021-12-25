import random
import colorama
from colorama import Fore, Back, Style
import sys
colorama.init()

def is_int(ch):
    global fint
    try:
        int(ch)
        fint = True
    except ValueError:
        fint = False


def player_hod():
    global step, kol
    if step == '+1':
        kol += 1
    if step == '+4':
        kol += 4
    if step == '*2':
        kol *= 2


def strategy():
    global i, N, strategies
    strategies = [0 for i in range(N)]
    for i in reversed(range(N)):
        if (i + 1 >= N) or (i + 4 >= N) or (i * 2 >= N):
            strategies[i] = True
        elif strategies[i + 1] and strategies[i + 4] and strategies[i * 2]:
            strategies[i] = False
        else:
            strategies[i] = True


def check_step():
    global step, order, mode
    while step != '+1' and step != '+4' and step != '*2':
        print(Fore.RED + ' Так нельзя. Загляни в правила')
        print(' Попробуй еще раз')
        if mode == '0' and order:
            sys.stdout.write(Fore.LIGHTGREEN_EX + ' Ход первого игрока:')
            step = input()
        elif mode == '0' and not order:
            sys.stdout.write(Fore.LIGHTMAGENTA_EX + ' Ход второго игрока:')
            step = input()
        else:
            sys.stdout.write(Fore.LIGHTGREEN_EX + ' Твой ход:')
            step = input()


def right_step():
    global step
    if strategies[kol]:
        if kol + 1 < N:
            if not strategies[kol + 1]:
                step = '+1'
            if kol + 4 < N:
                if not strategies[kol + 4]:
                    step = '+4'
                if kol * 2 < N:
                    if not strategies[kol * 2]:
                        step = '*2'
                else:
                    step = '*2'
            else:
                step = '+4'
        else:
            step = '+1'
    else:
        step = '+1'


def choosing_response(d):
    global step, kloh
    variants = {1: '+1', 2: '+4', 3: '*2'}
    loh = False
    if d == '3':
        if kloh == 3:
            loh = True
    if d == '2':
        if kloh == 2:
            loh = True
    if d == '1':
        loh = True
    if loh:
        if (kol * 2 >= N):
            step = '*2'
        elif kloh == 2 or kloh == 3:
            step = variants[random.randint(1, 2)]
        else:
            step = variants[random.randint(1, 3)]
        kloh = 1
    else:
        right_step()
        kloh += 1


def check_N():
    global N
    is_int(N)
    while not fint:
        if not fint:
            print(Fore.RED + ' Вводить нужно целое число...')
            print(' Попробуй еще раз')
            sys.stdout.write(Fore.LIGHTBLUE_EX + ' Напиши, сколько камней нужно собрать:')
            N = input()
            is_int(N)
    N = int(N)
    if N <= 4:
        if N <= 0:
            print(Style.RESET_ALL + Fore.RED + ' Это невозможно')
            print(' Попробуй еще раз')
            sys.stdout.write(Fore.LIGHTBLUE_EX + ' Напиши, сколько камней нужно собрать:')
            N = input()
            check_N()
        else:
            print(Style.RESET_ALL + ' Это слишком просто и неинтересно')
            print(' Давай больше')
            sys.stdout.write(Fore.LIGHTBLUE_EX + ' Напиши, сколько камней нужно собрать:')
            N = input()
            check_N()


def check_kol():
    global kol, s
    is_int(kol)
    while not fint:
        print(Style.RESET_ALL + Fore.RED + ' Вводить нужно целое число...')
        print(' Попробуй еще раз')
        sys.stdout.write(Fore.LIGHTBLUE_EX + " Напиши, сколько камней уже в куче:")
        kol = input()
        is_int(kol)
    kol = int(kol)
    if (kol >= N // 2 or kol + 4 >= N) and kol < N:
        print(Style.RESET_ALL + ' Это слишком просто и неинтересно')
        print(' Давай меньше')
        sys.stdout.write(Fore.LIGHTBLUE_EX + " Напиши, сколько камней уже в куче:")
        kol = input()
        check_kol()
    if kol < 0:
        print(Style.RESET_ALL + Fore.RED + ' Это невозможно')
        print(' Попробуй еще раз')
        sys.stdout.write(Fore.LIGHTBLUE_EX + " Напиши, сколько камней уже в куче:")
        kol = input()
        check_kol()
    if kol >= N and not s:
        print(Style.RESET_ALL + Fore.LIGHTYELLOW_EX + ' Ты победил, умник')
        s = True


def check_choiсe2(choiсe):
    global selection
    while choiсe != '1' and choiсe != '2':
        print(Style.RESET_ALL + Fore.RED + ' Как это понять?! Есть только два варианта...Выбери:')
        print(Style.RESET_ALL + selection)
        choiсe = input(' ')
    return choiсe


def check_choiсe4(choiсe):
    global selection
    while choiсe != '1' and choiсe != '2' and choiсe != '3' and choiсe != '4':
        print('Как это понять?! Есть только четыре варианта...Выбери:')
        print(selection)
        choiсe = input()
    return choiсe

print(Fore.GREEN + ' Здравствуй, рад тебя видеть. Нам нужно собрать кучу из камней.')
print(' Можно добавлять 1 камень, 4 камня или увеличить количество камней в 2 раза.')
print(' Цель игры — набрать N камней или больше.')
print(' Побеждает тот, кто первым наберет нужное количество камней.')
print(Fore.CYAN + ' Список команд:')
print(' Увеличить на 1="+1"')
print(' Увеличить на 4="+4"')
print(' Умножить на 2 ="*2"')
print(Fore.YELLOW + " После каждой команды нужно нажимать Enter.")
game = True
fint = False
while game:
    order = False
    s = False
    print('')
    sys.stdout.write(Style.RESET_ALL + Fore.LIGHTBLUE_EX + " Напиши, сколько камней нужно собрать:")
    N = input()
    check_N()
    print('')
    sys.stdout.write(Fore.LIGHTBLUE_EX + ' Напиши, сколько камней уже в куче:')
    kol = input()
    check_kol()
    if not s:
        print(Style.RESET_ALL + Fore.LIGHTBLUE_EX + ' С кем будешь играть?')
        selection = Style.RESET_ALL + ' 1-С компьютером    2-С другим игроком'
        print(selection)
        mode = input(' ')
        mode = check_choiсe2(mode)
        if mode == '1':
            print(Style.RESET_ALL + Fore.LIGHTBLUE_EX + ' Выбери уровень сложности')
            selection = ' 1-Легкий  2-Средний  3-Сложный  4-Невозможный'
            print(Style.RESET_ALL + selection)
            difficulty = input(' ')
            difficulty = check_choiсe4(difficulty)
            kloh = 1
            print(Style.RESET_ALL + Fore.LIGHTBLUE_EX + ' Кто делает первый ход?')
            selection = (Style.RESET_ALL + ' 1-Игрок      2-Компьютер')
            print(selection)
            choice_order = input(' ')
            choice_order = check_choiсe2(choice_order)
            strategy()
            if choice_order == '1':
                order = True
            else:
                order = False
            while kol < N:
                if order:
                    sys.stdout.write(Fore.LIGHTGREEN_EX + ' Твой ход:')
                    step = input()
                    check_step()
                    player_hod()
                    if kol >= N:
                        print(Fore.LIGHTYELLOW_EX + ' Получилось =', kol)
                        print(Fore.LIGHTGREEN_EX + ' Поздравляю, светлейший. Ты меня одолел')
                    else:
                        print(Style.RESET_ALL + ' Камней в куче =', kol)
                        order = False
                if not order and kol < N:
                    choosing_response(difficulty)
                    print(Fore.LIGHTBLUE_EX + " Мой ход:", step)
                    player_hod()
                    if kol >= N:
                        print(Fore.LIGHTYELLOW_EX + ' Получилось =', kol)
                        print(Fore.LIGHTBLUE_EX + ' В другой раз, светлейший. Я тебя победил')
                    else:
                        print(Style.RESET_ALL + ' Камней в куче =', kol)
                        order = True
        if mode == '2':
            order = True
            while kol < N:
                if order:
                    sys.stdout.write(Fore.LIGHTGREEN_EX + ' Ход первого игрока:')
                    step = input()
                    check_step()
                    player_hod()
                    if kol >= N:
                        print(Fore.LIGHTYELLOW_EX + ' Получилось =', kol)
                        print(Fore.LIGHTGREEN_EX + ' Первый игрок победил. Поздравляю')
                    else:
                        print(Style.RESET_ALL + ' Камней в куче =', kol)
                        order = False
                if not order and kol < N:
                    sys.stdout.write(Fore.LIGHTMAGENTA_EX + ' Ход второго игрока:')
                    step = input()
                    check_step()
                    player_hod()
                    if kol >= N:
                        print(Fore.LIGHTYELLOW_EX + ' Получилось =', kol)
                        print(Fore.LIGHTMAGENTA_EX + ' Второй игрок победил. Поздравляю')
                    else:
                        print(Style.RESET_ALL + ' Камней в куче =', kol)
                        order = True
    print(Style.RESET_ALL + Fore.LIGHTBLUE_EX + ' Повторим?')
    selection = Style.RESET_ALL + ' 1-Да  2-Нет'
    print(selection)
    choise_game = input(' ')
    check_choiсe2(choise_game)
    if choise_game == '2':
        game = False
