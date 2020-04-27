from itertools import count
from functools import reduce


def sum_func(var1, var2):
    return var1 + var2


my_file = open('output5.txt', 'w')
for el in count(2):
    my_file.write(str(el))
    if el > 10:
        break
    my_file.write(' ')
my_file.close()
my_file = open('output5.txt', 'r')
content = my_file.readline()
numb_list = content.split(' ')
float_numb_list = []
for i in range(len(numb_list)):
    float_numb_list.append(float(numb_list[i]))
my_sum = reduce(sum_func, float_numb_list)
print('Сумма всех чисел равна:', my_sum)
my_file.close()
