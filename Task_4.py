# Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла, найти в нем с помощью регулярных
# выражений все подстроки определенного вида, в соответствии с вариантом.


import re


def find_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for num_line, line in enumerate(f):
            required = re.findall(r'\d{2}-\d{2}-\d{4}', line)
            for _ in required:
                print(f"Строка {num_line + 1}, позиция {line.find(required[0])} : найдено '{required[0]}'")


if __name__ == "__main__":
    find_data('test.txt')