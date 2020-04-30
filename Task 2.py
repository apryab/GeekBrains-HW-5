try:
    with open("input2.txt") as my_file:
        contents = my_file.readlines()
        print("Количество строк в файле -", len(contents))
        n = 1
        for elem in contents:
            temp_list = elem.split(' ')
            print("Количество слов в строке №{0} равно: {1}".format(n, len(temp_list)))
            n += 1
except IOError:
    print('Проблема с файлом')
