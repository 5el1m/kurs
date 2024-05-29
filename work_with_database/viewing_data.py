from prettytable import PrettyTable


def browse_books(Books):
    """
        Функция вывода базы данных
            Входные данные:
                Books - база данных
    """
    tab = PrettyTable(title='Список книг', border=True, header=True,
                      vertical_char='│',
                      horizontal_char='─',
                      junction_char='┼',
                      left_junction_char='├',
                      right_junction_char='┤',
                      top_left_junction_char='┌',
                      top_right_junction_char='┐',
                      top_junction_char='┬',
                      bottom_junction_char='┴',
                      bottom_right_junction_char='┘',
                      bottom_left_junction_char='└',
                      start=0,
                      )

    tab.field_names = ['ISBN', 'Название', 'Город', 'Издательство', 'Страницы', 'Стоимость']
    tab.align['ISBN'] = 'l'
    tab.align['Название'] = 'l'
    tab.align['Город'] = 'с'
    tab.align['Издательство'] = 'с'
    tab.align['Страницы'] = 'c'
    tab.align['Стоимость'] = 'r'
    tab.sortby = 'ISBN'

    for isbn, properties in Books.items():
        pr = [isbn]
        for property in properties:
            pr = pr + [property]
        tab.add_row(pr)
    print(tab)
