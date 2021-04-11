
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

def sqrt(num):
    temp = 0
    sqrt = 0
    sqrt = num / 2
    while sqrt != temp:
        temp = sqrt
        sqrt = (num/temp + temp)/2.0
    return sqrt




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
            if S.right:
                if S.flag_v:
                    print("слишком много знаков =")
                    return 1
            else:
                S.right = True
                # return 0
            # if len(arg) == 1:
            #     if S.right:
            #         if S.flag_v:
            #             print("слишком много знаков =")
            #         return 1
            #     S.right = True
            #     return 0
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
                if S.flag_v:
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
    if S.right and '=' != arg[(len(arg) - 1)]: #защита от Х=, но =Х не работает теперь
        int_1 = -int_1
        # print("должно идти сисло или переменная")
    # теперь все возможные ситуации:
    if flag_x: # переменная есть
        # в зависимости от того какая степень:
        if int_2 != 1 and int_2 != 0 and (int_2.isdigit() or ('.' in int_2 and int_2.replace('.','').isdigit())):
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


