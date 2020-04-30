my_file = open("output1.txt", "w")
length = 1
while length != 0:
    choice = input("Введите, что бы вы хотели добавить в файл: ")
    length = len(choice)
    if length > 0:
        my_file.write(choice)
        my_file.write("\n")
