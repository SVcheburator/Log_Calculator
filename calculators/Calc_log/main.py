import math

def func():
    print('••• LOGn(a) = x ••• a = n^x •••')
    print('--- Що цікавить?:')
    print('--- Значення логарифму?(x)/Підлогарифмічний вираз?(a)')
    pytannia = str(input('••• Мене цікавить значення: '))

    try:

        if pytannia == 'x':
            n = int(input('••• n = '))
            a = int(input('••• a = '))
            if n > 0 and n != 1 and a > 0:
                print('--> x = ', math.log(a, n))
            else:
                print('!!! Основа(n) та підлогарифмічний вираз(a) повинні бути числами, більшими за 0, а також основа(n) - не дорівнювати 1!')
        elif pytannia == 'a':
            n = int(input('••• n = '))
            x = int(input('••• x = '))
            if n > 0 and n != 1:
                print('--> a = ', n**x)
            else:
                print('!!! Основа(n) повинна бути більша за 0, а також - не дорівнювати 1!')
        else:
            print("!!! Ви маєте обрати між 'x' та 'a'!")

          
    except ValueError:
        print("!!! Значення некоректне!")  
        print("!!! Основа(n) та підлогарифмічний вираз(a) повинні бути числами, більшими за 0, а також основа(n) - не дорівнювати 1!")  
func()


while True:
    print('')
    again_yes_or_no = input('--- Заново? [y/n]: ')

    if again_yes_or_no == 'y':
        print('')
        func()
    else:
        break