# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import math
from comp_v1 import *
# sys.stderr - сообщения об ошибках и собственные запросы переводчика.
# я ошибок синтаксиса командной строки и 1 для всех других видов ошибок.
# Если передается объект другого типа, то None эквивалентен передаче
# нуля, а любой другой объект выводится на sys.stderr и приводит к коду
# zвыхода 1. В частности, sys.exit() - это быстрый способ выйти из программы при возникновении ошибки.
#  0 == успешное завершение


def print_help():
    print('"Для отображения информации о возможности программы: python computorv1 -h", "для отображение промежуточных шагов -s",\
 "для чтения выражения из файла -f", "для отображение ошибок входа -v",\
 "неравенство должно быть квадратным и не содержать отрицательных стеепней", "общий вид выражения: a*x^2 + b*x^1 +c = 0",\
 "я справлюсь с вещественными числами и сокращением подобных членов,", "смогу вывести ирроцианальные корни и переживу, если ты пропустишь * или ^ для первой степени",\
 "давай поиграем кто быстрее? введи: python comp.py x^2 + 3x - 4 = 0"')



def equat(S):
    # a*x^2 + b x + c
    #S - главная структкра
    if S.a == 0:
        if S.b == 0 and S.c == 0:
            if S.flag_s:
                print('a=b=c: это точно надо решать?')
            print('all the real numbers are solution')
            sys.exit(0)
        elif S.b == 0:
            print('c !0 в этой вселенной => Уравнение не имеет решений')
        elif S.c == 0:
            print("c == a == 0: solution is ", 0)
            sys.exit(0)
        else: # a == 0
            if S.flag_v or S.flag_s:
                print("уравнение линейное")
            x_1 = -S.c/S.b
            print("solution is ", x_1)
            # sys.exit(0)
            return 0
    if S.b == 0 or S.c == 0:
        print("неполное квадратное уравнение")
        if S.b == 0 and S.c != 0:
            d = -S.c/S.a
            if d >0: # два корня
                x_1 = sqrt(d)
                x_2 = -sqrt(d)
                print("the two solution are:",x_1,x_2)
            # else:
                #мнимое
        elif S.c == 0 and S.b == 0:
                    print("c == b == 0: solution is ", 0)
        else: # S.c == 0 and S.b != 0
            x_1 = 0
            x_2 = -(S.b/S.a)
            print("c == 0 the two solution are:",x_1,x_2)
    else:
        if S.flag_s:
            print(f"D = b^2 - 4*a*c => {S.b}^2 - 4 * {S.a * S.c}")
        D = S.b**2 - 4*S.a*S.c
        if S.flag_s:
            print('D = ', D)
        if D == 0:
            if S.flag_s:
                print("один корень, D = 0") #(-b\2a)
            x_1 = -S.b / (2* S.a)
            print("solution is ", x_1)
        elif D< 0:
            if S.flag_s:
                print('комплексные корни, D < 0')
            D_minus = sqrt(-D)
            alpha = -S.b/(2*S.a)
            if alpha % 1 == 0:
                alpha = int(alpha)
            else:
               alpha = (f'{-S.b}/{2*S.a}')
            betta = D_minus/(2*S.a)
            if betta % 1 ==0:
                betta = int(betta)
            else:
                # if S.flag_s:
                #     print(f'D = {D}')
                D = int(D)
                betta = (f'\u221A{D} / {2 * S.a}')
            print("Discriminant is strictly negative, the two irrational solution are: ")
            print(f"{alpha} + ({betta}) *i")
            print(f"{alpha} - ({betta}) *i")
            # sys.exit(0)
            return 0

        else:
            if S.flag_s:
                print('2 комплексныx корня')
            X_1 = (- S.b + sqrt(D))/(2*S.a)
            X_2 = (- S.b - sqrt(D))/(2*S.a)
            if X_1 % 1 ==0:
                X_1 = int(X_1)
            else:
                sqrt_D = sqrt(D)
                if sqrt_D % 1 ==0:
                    X_1 = (f'({- S.b + sqrt_D}/ {2 * S.a}')
                # else:
                #     X_1 = (f'({- S.b} + \u221A{int(D)})/ {2 * S.a}')
            if X_2 % 1 ==0:
                X_2 = int(X_2)
            else:
                sqrt_D = sqrt(D)
                if sqrt_D % 1 ==0:
                    X_2 = (f'({- S.b - sqrt_D}/ {2 * S.a}')
                # else:
                #     X_2 =  (f'({- S.b} - \u221A{int(D)})/ {2 * S.a}')
            print("Discriminant is strictly positiv, the two solution are: ")
            print(round(X_1,6))
            print(round(X_2, 6))
            # sys.exit(0)
            return 0
    #решение уравнения

    # число в 0 степени = 1


def main_m():
    S = Start()
    # slide = ['-70x','+','x^2','+','x^3', '=','-100', '+', '-500x^0', '+','+','x^3']#['-', '-X^2','+','10','-',"x", '=', '0']
    # slide = ['42*x^4', '=', '42*x^4']
    # slide = ['x^2', '+', '4x', '+', '29', '=', '0'] # D <0
    # slide = ['x^2', '-', 'x', '+', '2', '=', '0'] # D <0
    # print('len == ', len(sys.argv))

    args = sys.argv
    if len(args) == 1:#если нет входных параметров
        print_help()
        return 0
        # sys.exit(0)
    elif len(args) == 2:# или 1 входной параметр или строка
        str_arg = args[1]
        if ('*' in str_arg):
            str_arg = str_arg.replace(' * ', '')
            args = str_arg.split(' ')
    else:# каждый параметр = аргумент
            args.remove(args[0])
    # args = ["-sv",'-v','x^2.0', "-", "4x", "-", "-4", "=", "0"]

    # print(args)
    ia = 0
    for arg_i in  args: # slide:  ['-4x', '=','-X^2', '+', '-4'] - 1 корень
            parse = parse_arg(arg_i, S)
            if parse == 1:
                print("Error")
                sys.exit(1)
            else:
                pass
            if S.flag_f:
                file_args = read_file(args[ia + 1])
                args.remove(args[ia+1])
                for i_i in file_args:
                    args.append(i_i)
                S.flag_f = False
            ia += 1
    # print(f"Reduced form: {S.a} * X^2 + {S.b} * X + {S.c} = 0")
    if S.flag_s:
        print(args)
    if S.flag_help:
        print_help()
        sys.exit(0)

    if not S.right:
        if S.flag_v:
            print("выражение не является неравенством, попробуй добавить = 0")
        # sys.exit(1)
    list_keys = list(S.other_dict.keys())
    for i in list_keys:
        if S.other_dict[i] == 0:
            del S.other_dict[i]
    if len(S.other_dict) > 0:
        list_keys = list(S.other_dict.keys())
        list_keys.sort() # отсортированные значения степени
        i_less_0 = 0
        # i =len(list_keys)
        # i_max = list_keys[i - 1] #последний ключ отсортированного массива - наибольшая степень
        list_keys.reverse()
        i_max = list_keys[0]
        list_keys.reverse()
    #else: 0 = 0
        str_print = 'Reduced form: '

        for i in list_keys:
            if S.other_dict[i] != 0:
                i_max = i
                int_num = S.other_dict[i]
                if int_num % 1 ==0:
                    int_num = int(int_num)
                str_print += str(int_num) + 'X^' + str(i) + ' '
                if i != list_keys[-1]:
                    str_print += '+ '
                    if i  < i_less_0:
                        i_less_0= i
                        print("отрицательная степень недопустима заданием - члены не сокращены", i)
    else:
        print('Reduced form: 0 = 0')
        print('all the real numbers are solution')
        return 0
    str_print += '= 0'
    print(str_print)
    if i_max > 2:
        print("polynomial degree is stricly greater than 2, I can't solve.")
        return 1
    print("Polynomial degree: ", i_max)
    if i_less_0 != 0:
        print("отрицательная степень недопустима заданием - члены не сокращены", i_less_0)
        sys.exit(1)
    if 2 in list_keys:
        S.a = S.other_dict[2]
    if 1 in list_keys:
        S.b = S.other_dict[1]
    if 0 in list_keys:
        S.c = S.other_dict[0]
    equat(S)

if __name__ == '__main__':
    main_m()

