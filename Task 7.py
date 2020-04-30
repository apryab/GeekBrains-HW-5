import codecs
import json


sum_of_pos_income = 0
numb_of_profitable = 0
my_dict = dict()
try:
    with codecs.open('input7.txt', encoding='utf-8') as my_file:
        contents = my_file.readlines()
        for elem in contents:
            temp_list = elem.split(' ')
            income = temp_list[2]
            loss = temp_list[3]
            try:
                income = float(income)
                loss = float(loss)
                dif = income - loss
                my_dict[temp_list[0]] = dif
                if dif >= 0:
                    numb_of_profitable += 1
                    sum_of_pos_income += dif
            except(ValueError, TypeError):
                print('Ошибка в данных компании. Она не будет учтена')
    if numb_of_profitable > 0:
        av_profit = sum_of_pos_income / numb_of_profitable
    else:
        av_profit = 0
    profit_dict = {'Average profit': av_profit}
    final_list = [my_dict, profit_dict]
    with codecs.open('output7.json', 'w', encoding='utf-8') as output_file:
        json.dump(final_list, output_file, ensure_ascii=False)
except IOError:
    print('Проблема с файлом')
