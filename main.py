from modules.functions import *
from modules.database import *


def menu():
    """
        Функция вывода меню
            Выходные данные:
                num - номер пункта меню
    """

    print()
    print('    МЕНЮ    '.center(60, '*'))
    print("Действия для работы с базой данных:\n"
          "1 - Просмотр всех книг\n"
          "2 - Добавление новой книги\n"
          "3 - Удаление книги\n"
          "4 - Определение стоимости книг, изданных в одном городе\n"
          "5 - Завершение работы\n")

    while True:
        num = int(input('Выберите действие: '))
        if (num < 1) or (num > 5):
            print('Неправильное действие.')
        else:
            break
    return num


while True:
    number = menu()
    Books = txt_to_dict()
    match number:
        case 1:
            browse_books(Books)
        case 2:
            Books = add_book(Books)
        case 3:
            Books = delete_book(Books)
        case 4:
            all_books_cost(Books)
        case 5:
            print("Завершение работы!")
            break
    dict_to_txt(Books)
