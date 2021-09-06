# Задан путь к директории с музыкальными файлами (в названии которых нет номеров, а только названия песен) и
# текстовый файл, хранящий полный список песен с номерами и названиями в виде строк формата «01. Freefall [6:12]».
# Напишите скрипт, который корректирует имена файлов в директории на основе текста списка песен.


import os


def add_number_for_music(file, path):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if line.split(' ')[1] == name:
                        number = line.split(' ')[0]
                        new_name = number + name
                        os.rename(os.path.join(root, name), os.path.join(root, new_name))


if __name__ == "__main__":
    add_number_for_music('my_cnf.txt', 'C:\\Users\kalga\OneDrive\Рабочий стол\music')
