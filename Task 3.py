import codecs

try:
    with codecs.open('input3.txt', encoding='utf-8') as my_file:
        contents = my_file.readlines()
        salary_list = []
        name_list = []
        for elem in contents:
            temp_list = elem.split(' ')
            try:
                if float(temp_list[1]) < 20:
                    name_list.append(temp_list[0])
                salary_list.append(float(temp_list[1]))
            except(TypeError, ValueError):
                print('Ошибка с данными в файле. Этот сотрудник не будет учтён.')
        print('Сотрудники с зарплатой меньше 20 тысяч:', name_list)
        my_sum = 0
        for item in salary_list:
            my_sum += item
        av_salary = my_sum / len(salary_list)
        print('Средняя зарплата сотрудников - {0:.3f}'.format(av_salary))
except IOError:
    print('Проблема с файлом')
