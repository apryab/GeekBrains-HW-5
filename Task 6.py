import codecs


def numb_from_str(my_string):
    my_temp_string = ''
    if len(my_string) == 0:
        return 0
    else:
        for item in my_string:
            if 48 <= ord(item) <= 57:
                my_temp_string += item
            else:
                break
    try:
        my_temp_string = int(my_temp_string)
        return my_temp_string
    except(TypeError, ValueError):
        return 0


name_list = []
time_list = []
my_dict = dict()
try:
    with codecs.open('input6.txt', encoding='utf-8') as my_file:
        content = my_file.readlines()
        for elem in content:
            temp_list = elem.split(' ')
            temp_sum = 0
            for i in range(1, len(temp_list)):
                temp_sum += numb_from_str(temp_list[i])
            my_dict[temp_list[0][:-1]] = temp_sum
    print('Итоговый словарь:', my_dict)
except IOError:
    print('Проблема с файлом')
