def chislo():
    c = int(input("Введите Ваше число"))
    if c % 3 == 0:
        print("Делится")
    else:
        print("Не делится")
chislo()

def delen():
    try:
        c = 100
        pc = int(input("Введите Ваше число"))
        print(c // pc)
    except(ValueError, ZeroDivisionError):
        print("Ощибка! a = " + str(c))
delen()

def date():
    d = int(input("Введите день"))
    m = int(input("Введите месяц"))
    g = int(input("Введите две последние цифры года"))
    if (d * m == g):
        print("Магическая дата")
    else:
        print("Немагическая дата")
date()

def bilet():
    summa1 = 0
    summa2 = 0
    n = input("Введите номер")
    if len(n) % 2 == 1:
        print("Допишите ещё цифру")
    elif len(n) % 2 == 0:
        d = len(n) // 2
        d1 = n[:d]
        d2 = n[d:]
        for i in d1:
            summa1 += int(i)
        for j in d2:
            summa2 += int(j)
        if summa1 == summa2:
            print("Билет счастливый")
        else:
            print("Попробуйте ещё раз :)")
bilet()