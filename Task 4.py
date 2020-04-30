try:
    with open('input4.txt') as my_file:
        with open('output4.txt', 'w') as my_output_file:
            contents = my_file.readlines()
            eng_list = ['One', 'Two', 'Three', 'Four']
            rus_list = ['Один', 'Два', 'Три', 'Четыре']
            for elem in contents:
                temp_list = elem.split(' ')
                for i in range(len(eng_list)):
                    if temp_list[0] == eng_list[i]:
                        temp_list[0] = rus_list[i]
                        break
                my_output_file.write(' '.join(temp_list))
except IOError:
    print('Проблема с файлом')
