S = int(input('Сумма чисел: '))
P = int(input('их произведение: '))

D = S * 2 - 4 * P

if D < 0:
    print('Решений нет')
else:
    x1 = - P + D * S / 2 
    x2 = - P - D * S / 2
    print('x1 = ',x1, 'x2 = ',x2)
    if x1 <= 1000 and x1 > 0:
        print('X = ', int(x1), 'Y = ', int(x1 - S))
    elif x2 <= 1000 and x2 > 0:
        print('X = ', int(x2), 'Y = ', int(x2 - S))
    else:
        print('Решений с числами до 1000 нет. ')
         
