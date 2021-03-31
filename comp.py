# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import math


class Start:
    def __init__(self):
        # Manage inputs outputs in a natural form.

        # Display the solution(s) under the form of irrational fractions when it is interesting..
        self.flag_v = False # Manage errors on the input (lexicon and syntax)
        self.flag_s = False # Display intermediate steps. = Отображение промежуточных шагов
        self.flag_help = False #для показа стартового сообщения
        self.flag_f = False # возможность считать из файла

        self.a = 0
        self.b = 0
        self.c = 0
        self.other_dict = {}
        self.minus = False
        self.right = False # то что есть = и число справа
        # для текущего одного аргумента
        self.int_2_flag = False
def read_file(name):
    vih = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            line.replace("'", '')
            vih = line.split(' ')
    return vih

def print_help():
    print("Для отображения информации о возможности программы: python comp.py -h",
          "для отображение промежуточных шагов -s",
          "для чтения выражения из файла -f",
          "для отображение ошибок входа -v",
          "неравенство должно быть квадратным и не содержать отрицательных стеепней",
          "общий вид выражения: a*x^2 + b*x^1 +c = 0",
          "я справлюсь с вещественными числами и сокращением подобных членов,",
          "смогу вывести ирроцианальные корни и переживу, если ты пропустишь * или ^ для первой степени",
          "давай поиграем кто быстрее? введи: python comp.py x^2 + 3x - 4 = 0")


def sqrt(num):
    temp = 0
    sqrt = 0
    sqrt = num / 2
    while sqrt != temp:
        temp = sqrt
        sqrt = (num/temp + temp)/2.0
    return sqrt


def equat(S):
    # a*x^2 + b x + c
    #S - главная структкра
    if S.a == 0:
        if S.b == 0 and S.c == 0:
            if S.flag_s:
                print('a=b=c: это точно надо решать?')
            print('all the real numbers are solution')
            return 0
        elif S.b == 0:
            print('c !0 в этой вселенной => Уравнение не имеет решений')
        elif S.с == 0:
            print("c == a == 0: solution is ", 0)
        else: # a == 0
            print("уравнение линейное")
            x_1 = -S.c/S.b
            print("solution is ", x_1)
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
                print('комплексные корни')
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
                if S.flag_s:
                    print('комплексные корни D<0')
                D = int(D)
                betta = (f'\u221A{D} / {2 * S.a}')
            print("Discriminant is strictly negative, the two irrational solution are: ")
            print(f"{alpha} + ({betta}) *i")
            print(f"{alpha} - ({betta}) *i")

        else:
            if S.flag_s:
                print('2 комплексныx корня')
            X_1 = (- S.b + sqrt(D))/(2*S.a)
            X_2 = (- S.b - sqrt(D))/(2*S.a)
            if X_1 % 1 ==0:
                X_1 = int(X_1)
            else:
                X_1 = (f'({- S.b} + \u221A{int(D)})/ {2 * S.a}')
            if X_2 % 1 ==0:
                X_2 = int(X_2)
            else:
                X_2 =  (f'({- S.b} - \u221A{int(D)})/ {2 * S.a}')
            print("Discriminant is strictly positiv, the two solution are: ")
            print(X_1)
            print(X_2)
    #решение уравнения

    # число в 0 степени = 1
def parse_arg(arg, S):
#     парсинг аргументов (одного)
#     ищет все флаги
#     смотрит есть ли переменная
#     и какой множитель
#     и какая степень
    arg = arg.replace('\n', ' ')
    arg = arg.replace(' ', '')
    if S.flag_v or S.flag_s:
        print("рассмотрим arg = ", arg)
    spis_x = ['x', 'X','х','Х'] #список возможных обозначений переменных
    int_1 = ''
    int_2 = ''
    int_2_flag = 0 # наличие степени ^
    flag_x = 0 # наличие x
    flag_minus = 0 # минус инт1
    flag_minus_2 = 0 # минус инт2
    flag_mul = 0 # умножение = pass
    flag_point = 0 # вещественное число
    lenp = len(arg)
    for i in range(len(arg)):
        if arg[i] == '-':
            if int_2_flag:
                flag_minus_2 = 1
            else:
                flag_minus = 1
            if len(arg) == 1:
                S.minus = True # значит - для след аргумента
                return

            # может быть минус, а может флаг
            # если минус перед числом, может быть конкретно перед членом, а может перед выражением 1 - 2, а еще может быть перед скобкой 1 - (2 +3)
        elif arg[i] == '=':
            if len(arg) == 1:
                if S.right:
                    if S.flag_v:
                        print("слишком много знаков =")
                    return 1
                S.right = True
                return 0
                #если еще не было, то == минусу для всех коэфициентов


        elif (arg[i] >= '0' and arg[i] <='9') or (arg[i] == '.'): #идет число
            if arg[i] == '.':
                if flag_point:
                    if S.flag_v:
                        print("слишком много точек в числе")
                    return 1
                # if flag_x or int_2_flag:
                #     if S.flag_v:
                #         if arg[1+1] != '0':
                #             print('вижу пытаешься точку ты в степени поставить, вероятно в следующей серии смогу решить такое, но не теперь =( arg =', arg)
                #             return  0
                else:
                    flag_point = 1

            if int_2_flag:
                int_2 = int_2 + str(arg[i])
            elif flag_x:
                if S.flag_v:
                    print("похоже число после переменной без ^, arg = ", arg)
                return 1
            elif int_1:
                int_1 = str(int_1) + str(arg[i])
            else:
                int_1 = str(arg[i])
        elif arg[i] in spis_x: #значит есть переменная
            if S.flag_s:
                print("переменная есть")
            if flag_x:
                print('Много переменных для одного аргумента, возможно будет доступно в следущей версии. arg = ', arg)
                return 1
            flag_x = 1
        elif arg[i] == '^':
            if S.flag_s:
                print("степень есть")
            if not flag_x:
                if S.flag_v:
                    print('степень есть, а переменной нет')
                return 1
            int_2_flag = 1
        elif flag_minus == 1:
            # flag_minus = 0
            if arg[i] == 'v':
                S.flag_v = True
            elif arg[i] == 's':
                S.flag_s = True
            elif arg[i] == 'h':
                S.flag_help = True
            elif arg[i] == 'f':
                S.flag_f = True
            else:
                # это минус от числа инт_1
                flag_minus = 1
        elif arg[i] == "*":
            if flag_mul:
                if S.flag_v:
                    print("Для возведения степень используйте ^, ** - не распознаваемый символ")
                return 1
            flag_mul = 1
        elif (arg[i] == '+') or (arg[i] == ' '):
            return 0
        else:
            print("символ не допустим для получения всех опций: comp_v1.py -h")
    # разберемся с полученными числами
    if int_2 and not int_2_flag:
        print("неопознаное число, если это степень добавьте: ^")
        return 1
    if int_1.isdigit() or ('.' in int_1 and int_1.replace('.','').isdigit()):
        int_1 = float(int_1)
    elif int_1 == '':
        if flag_x: #нет инт1, но есть переменная
            int_1 = 1
        else: #нет инт1, и переменной нет
            int_1 = 0
    if int_1 and not int_2:
        if not int_2_flag:
            if flag_x: #переменная есть, а степени нет / инт1 при этом есть
                int_2 = 1
            else: # переменной нет и степени нет == свободнфй член
                int_2 = 0
    elif int_1 == 0:
            int_2 = 0



    if int_2_flag:
        if flag_minus_2:
            int_2 = - int(int_2)
            if S.flag_v:
                print("Отрицательная степень не допустима заданием =(, флаг -h для просмотра всех опций")
            # return 0
        # elif S.right:
        #     print("Знак = в недопустимом месте")
    # else:
    #     int_1 = 1
    if S.minus and int_1:
            int_1 = -int_1
            S.minus = False # если перед скобкой, то !=
    if flag_minus == 1:
        int_1 = -int_1
    if S.right:
        int_1 = -int_1
        # print("должно идти сисло или переменная")
    # теперь все возможные ситуации:
    if flag_x: # переменная есть
        # в зависимости от того какая степень:
        if int_2 != 1 and (int_2.isdigit() or ('.' in int_2 and int_2.replace('.','').isdigit())):
            int_2 = float(int_2)
            if int_2 % 1 == 0:
                int_2 = int(int_2)
            else:
                print("степень такую сам решай, я устал! дай мне вещественное число! arg = ",arg)
                return 1
        elif ((int_2 == '') or (int(int_2) == 1)):
            int_2 = 1
            # S.b = S.b + int_1
        elif (int(int_2) == 0): # == свободный член
            int_2 = 0
            # S.c = S.c + int_1
        # elif int(int_2) == 2:
            # if int_1:
                # S.a = S.a + int(int_1)
    else:
        if int_1:
            int_2 = 0
            # S.c += int(int_1)
        # print(int_2)

    if int(int_2) not in S.other_dict:
        int_2 = int(int_2)
        if int_2 % 1 != 0:
            if S.flag_v:
                print('не могу понять значение степени: arg = ', arg)
            return 1
        S.other_dict[int_2] = 0
    int_2 = int(int_2)
    S.other_dict[int_2] = int(S.other_dict[int_2]) + int_1
    if S.flag_v and (2 < int_2 < 0):
            print(f"степень {int_2} не доступна по заданию")
            # return 0
    # elif int_1: #int(int_1):#просто число еще - без переменной (без переменной) == int_2 ==0 or int_2 == 0
    #     S.c = S.c + int(int_1)
        # S.right = False
    return 0
    # elif


def main_m(inarg=None):
    S = Start()
    # slide = ['-70x','+','x^2','+','x^3', '=','-100', '+', '-500x^0', '+','+','x^3']#['-', '-X^2','+','10','-',"x", '=', '0']
    # slide = ['42*x^4', '=', '42*x^4']
    # slide = ['x^2', '+', '4x', '+', '29', '=', '0'] # D <0
    # slide = ['x^2', '-', 'x', '+', '2', '=', '0'] # D <0
    # print('len == ', len(sys.argv))
    if inarg:
        args = inarg
    else:
        args = sys.argv.copy()
    if len(args) == 1:
        print_help()
        return 0
    args.remove(args[0])
    # args = ["-sv",'-v','x^2.0', "-", "4x", "-", "-4", "=", "0"]

    # print(args)
    ia = 0
    for arg_i in  args: # slide:  ['-4x', '=','-X^2', '+', '-4'] - 1 корень
            parse = parse_arg(arg_i, S)
            if parse == 1:
                print("Error")
                return 1
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
        return 0

    if not S.right:
        if S.flag_v:
            print("выражение не является неравенством, попробуй добавить = 0")
        return 0
    list_keys = list(S.other_dict.keys())
    for i in list_keys:
        if S.other_dict[i] == 0:
            del S.other_dict[i]
    if len(S.other_dict) > 0:
        list_keys = list(S.other_dict.keys())
        list_keys.sort() # отсортированные значения степени
        i_less_0 = 0
        i =len(list_keys)
        i_max = list_keys[i - 1] #последний ключ отсортированного массива - наибольшая степень
        while i and (not i_max):
            if S.other_dict[i_max] > 0:
                i_max = list_keys[i]
            else:
                i -= 1
        str_print = 'Reduced form: '

        for i in list_keys:
            if S.other_dict[i] != 0:
                i_max = i
                int_num = S.other_dict[i]
                if int_num % 1 ==0:
                    int_num = int(int_num)
                str_print += str(int_num) + 'X^' + str(i) + ' '
                if i != len(list_keys):
                    str_print += '+ '
                    if i  < i_less_0:
                        i_less_0= i
                        print("отрицательная степень недопустима заданием - члены не сокращены", i)
    else:
        print('0 = 0')
        print('all the real numbers are solution')
        return 0
    str_print += '= 0'
    print(str_print)
    if i_max > 2:
        print('не могу решить уравнения, выше квадратного')
        return 1
    print("Polynomial degree: ", i_max)
    if i_less_0 != 0:
        print("отрицательная степень недопустима заданием - члены не сокращены", i_less_0)
        return 1
    if 2 in list_keys:
        S.a = S.other_dict[2]
    if 1 in list_keys:
        S.b = S.other_dict[1]
    if 0 in list_keys:
        S.c = S.other_dict[0]
    equat(S)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    main_m()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
