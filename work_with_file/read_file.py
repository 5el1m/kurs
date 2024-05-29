def read():
    """
        Функция получения базы данных из файла
            Выходные данные:
                Books - база данных
    """

    file = r"C:\Users\Никита\Desktop\Курсовая\data.txt"
    Books = {}
    with open(file, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            book = line.strip().split(',')
            Books[book[0]] = [book[1], book[2], book[3], book[4], book[5]]
    return Books


