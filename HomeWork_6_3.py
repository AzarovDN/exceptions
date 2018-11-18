documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        # {"type": "Проверочка", "number": "000"} # ввел строку для проверки работы функции print_all_names

      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def print_whose_document():
  document_number = input('Введите номер документа, чтобы найти его владельца:')
  found = False
  for document in documents:
    if document["number"] == document_number:
      print('Хозяин документа {}'. format(document["name"]))
      found = True
  if found == False:
    print ('Документ не найден.')


def print_all_documents():
  for document in documents:
    print('{} "{}" "{}"'.format(document["type"], document["number"],  document["name"]))


def print_shelf_number():
  document_number = input('Введите номер документа, чтобы найти на какой полке он лежит:')
  found = False
  for number_shelf, numbers_documents in directories.items():
    if document_number in numbers_documents:
      print('Номер полки {}'.format(number_shelf))
      found = True
  if found == False:
    print ('Документ не найден.')

def find_shelf():
  shelf_number_list = []
  shelf = input('Введите номер полки:')
  while shelf != []:
    for shelf_number in directories.keys():
      if shelf_number == shelf:
        return shelf
      else:
        shelf_number_list.append(int(shelf_number))
    shelf_number_list.sort()
    print('Номера полок доступные для ввода:', end='')
    for shelf_number in directories.keys():
      print ('{}; '.format(shelf_number), end='')
    print('')
    shelf = input('Введите номер полки или введите "n", чтобы добавить новую полку')
    if shelf.lower() == 'n':
      add_shelf()


def add_document():
  number_document = input('Введите номер нового документа:')
  type_document = input('Введите тип документа:')
  name = input('Введите имя владельца документа:')
  shelf = find_shelf()
  documents.append({"type": type_document,
                   "number": number_document,
                   "name": name})
  for number_shelf, numbers_documents in directories.items():
    if number_shelf == shelf:
      numbers_documents.append(number_document)


def delete_document():
  number_document = input('Введите номер документа, который хотите удалить:')
  found = False
  for number, document in enumerate(documents):
    if document["number"] == number_document:
      documents.pop(number)
      found = True
  for number_shelf, numbers_documents in directories.items():
    if number_document in numbers_documents:
      numbers_documents.remove(number_document)
  if found == False:
    print('Документ не найден.')
  else:
    print('Документ удален.')


def move_document():
  found = False
  number_document = input('Введите номер документа, который хотите переместить:')
  print('Теперь нужно ввести номер полки, на которую вы хотите переместить документ.')
  shelf = find_shelf()
  for number_shelf, numbers_documents in directories.items():
    if number_document in numbers_documents and shelf == number_shelf:
      print('Документ уже находится на этой полке.')
      return
    if number_document in numbers_documents and shelf != number_shelf:
      numbers_documents.remove(number_document)
      directories[shelf].append(number_document)
      print('Документ перемещен.')
      return
  print('Документ не найден.')


def add_shelf():
  new_shelf = input('Добавьте номер полки:')
  if new_shelf in directories.keys():
    print('Данная полка уже существует.')
  else:
    directories[new_shelf] = []
    print('Полка добавлена')


def print_menu():
  print('''
p  – определяет вдадельца документа по его номеру;
l  – Вывод списка всех документов;
s  – Найти полку по номеру документа;
a  – добавить документ;
d  – удалить документ;
m  – переместить документ с текущей полки на целевую;
as – добавить новую полку;
ap - напечатать всех владельцев документа;
exit - выход из программы.''')

# дополнение. Задача 6. для проверки работы в списке словарей documents сделал и закомментил словарь без имени.
def print_all_names():
    for dictionary in documents:
        try:
            print(dictionary["name"])
        except KeyError:
            print('Имя в {} не обнаружено'.format(dictionary))
        # print(dictionary["name"])


print_menu()

while 1 == 1:
  action = input('Выберите команду из списка("menu" - напечатать меню):')
  action = action.lower()
  if action == 'menu':
    print_menu()
  elif action == 'p':
    print_whose_document()
  elif action == 'l':
    print_all_documents()
  elif action == 's':
    print_shelf_number()
  elif action =='a':
    add_document()
  elif action == 'd':
    delete_document()
  elif action == 'm':
    move_document()
  elif action == 'as':
    add_shelf()
  elif action == 'ap':
    print_all_names()
  elif action == 'exit':
    break
  else:
    print('Некорректные данные.')