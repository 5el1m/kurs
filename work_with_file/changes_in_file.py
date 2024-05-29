def overwrite(Books):
    """
        Функция перезаписи базы данных в файле
            Входные данные:
                Books - база данных
    """

    file = r"C:\Users\Никита\Desktop\Курсовая\data.txt"
    with open(file, mode='w', encoding='utf-8') as f:
        for key, val in Books.items():
            s = key + ',' + ','.join(val) + '\n'
            f.write(s)
