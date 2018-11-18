number = int(input('Введите число:'))
trigger = False

try:
    assert number > 0
except AssertionError:
    print('Введенное число {} отрицательное или равно 0'.format(number))
    trigger = True

if trigger == False:
    print('Число {} положительное'.format(number))


