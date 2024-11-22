def recieve_give(operand):
    '''Функция, принимающая от пользователя арифметическое выражение и возвращающая его результат'''
    result = None
    master_list = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
                   'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
                   'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                   'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    dozen_list = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
                  'восемьдесят', 'девяносто']
    hundred_list = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот',
                    'восемьсот', 'девятьсот']
    thousand_list = ['тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч',
                     'семь тысяч', 'восемь тысяч', 'девять тысяч']
    numbers_list = []

    for dozen in dozen_list:
        for digit in ([''] + master_list[1:10]):
            if digit != '':
                master_list.append(dozen + ' ' + digit)
            else:
                master_list.append(dozen + digit)

    for hundred in hundred_list:
        for dozen in ([''] + master_list[1:100]):
            if dozen != '':
                master_list.append(hundred + ' ' + dozen)
            else:
                master_list.append(hundred + dozen)

    for thousand in thousand_list:
        for hundred in ([''] + master_list[1:1000]):
            if hundred != '':
                master_list.append(thousand + ' ' + hundred)
            else:
                master_list.append(thousand + hundred)


    for num in range(10000):
        numbers_list.append(num)

    if ('  ' in operand) or (operand[0] == ' ') or (operand[-1] == ' ') or (operand == ""):
        print('Некорректный ввод. Перезапустите программу')
        return True
    operand = operand.replace('минус', '-')
    operand = operand.replace('плюс', '+')
    operand = operand.replace('умножить на', '*')
    operand = operand.replace('скобка открывается', '(')
    operand = operand.replace('скобка закрывается', ')')
    for ind, num in enumerate(reversed(master_list[0:100])):
        operand = operand.replace(num, str(numbers_list[100 - ind - 1]))
    try:
        result = eval(operand)
    except SyntaxError:
        print('Введены некорректные данные. Перезапустите программу.')
    except NameError:
        print('Введены некорректные данные. Перезапустите программу.')
    if result or (int(result == 0)):
        operand = operand.replace(' ', '')
        if (('**' in operand) or ('++' in operand) or (operand[0] == '+')  or
                ('---' in operand) or ('-+' in operand) or ('+--' in operand) or ('*--' in operand)):
            print('Введены некорректные данные')
            return True
        else:
            try:
                if (str(result)[0]) == '-':
                    result = int(str(result[1:]))
                    print('минус ' + master_list[numbers_list.index(result)])
                else:
                    print(master_list[numbers_list.index(result)])
            except ValueError:
                print('Введены некорректные данные ')


try:
    recieve_give(input('Введите арифметическое выражение: '))
except IndexError:
    print("Обнаружена ошибка ввода. Перезапустите программу.")
except ValueError:
    print('Обнаружена ошибка ввода. Перезапустите программу.')
