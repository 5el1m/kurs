def add_book(Books):
    """
        Функция добавления новой записи в базу данных
            Входные данные:
                Books - база данных
            Выходные данные:
                Books - база данных
    """

    new_isbn = input("Введите ISBN книги: ")
    new_name = input("Введите название новой книги: ")
    new_city = input("Укажите город издания книги: ")
    new_publisher = input("Укажите издательство книги: ")
    new_pages = input("Укажите кол-во страниц в книге: ")
    new_cost = input("Укажите стоимость книги: ")

    if new_isbn in Books.keys():
        print("Вы ввели ISBN существующей книги, повторите попытку!")
        return

    if not new_city.isalpha():
        print("Название города введено неправильно, повторите попытку!")
        return

    if not new_pages.isdigit():
        print("Количество страниц в книге введено неправильно, повторите попытку!")
        return

    if not new_cost.isdigit() or new_cost == 0:
        print("Стоимость книги введена неправильно, повторите попытку!")
        return

    Books[new_isbn] = [new_name, new_city.capitalize(), new_publisher.capitalize(), new_pages, new_cost]

    return Books

def delete_book(Books):
    """
        Функция удаления записей из базы данных
            Входные данные:
                Books - база данных
            Выходные данные:
                Books - база данных
    """

    while True:
        answer = input("Вы действительно хотите удалить книгу? (Да/Нет) ").lower()

        if answer == 'да':
            book_for_del = input("Введите ISBN книги, которую хотите удалить: ")

            if book_for_del in Books:
                del Books[book_for_del]
                print('Книга удалена')
                continue
            else:
                print('Такой книги нет')

        elif answer == 'нет':
            break

        else:
            print("Такой ответ невозможно обработать, повторите попытку!")
            continue

    return Books

def all_books_cost(Books):
    """
        Функция определения цены всех книг, изданных в одном городе
            Входные данные:
                Books - база данных
    """
    city = input("Введите город, в котором вы хотите узнать стоимость изданных книг: ")
    full_cost = 0

    for book in Books.values():
        if book[1] == city:
            full_cost += int(book[4])

    if full_cost == 0:
        print(f"В базе данных нет книг изданных в городе {city}!")
        return

    print(f"Стоимость книг, изданных в городе {city}: {full_cost}")