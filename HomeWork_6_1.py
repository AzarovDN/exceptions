import re
def getWords(text):
    return re.compile('\w+').findall(text)

data = input('Введите выражение в польском формате. Например: a + b нужно записать + a b:')
operator = ''

for letter in data:
    if letter == '+' or letter == '-' or letter == '*' or letter == '/':
        operator = letter
        break

numbers = getWords(data)

result = 0

exit = False

if operator == '+':
    result = int(numbers[0]) + int(numbers[1])
elif operator == '-':
    result = int(numbers[0]) - int(numbers[1])
elif operator == '/':
    result = int(numbers[0]) / int(numbers[1])
elif operator == '*':
    result = int(numbers[0]) * int(numbers[1])
else:
    exit = True

if exit == True:
    print('Данные введены некоректно')
else:
    print('Ваш результат {}'.format(result))






