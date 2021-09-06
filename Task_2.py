# Напишите скрипт, позволяющий искать в заданной директории и в ее подпапках файлы-дубликаты на основе сравнения
# контрольных сумм (MD5). Файлы могут иметь одинаковое содержимое, но отличаться именами. Скрипт должен вывести группы
# имен обнаруженных файловдубликатов.


import os
import hashlib


def find_duplicate_file(path):
    cash = {}
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            with open(os.path.join(root, name), 'r', encoding='utf-8') as f:
                cash[name] = hashlib.md5(f.read().encode('utf-8')).hexdigest()
    return cash


def find_duplicate(dictionaries):
    result = []
    for key_one, value_one in dictionaries.items():
        for key_two, value_two in dictionaries.items():
            if value_one == value_two and key_one != key_two:
                result.append(key_one)
    return result


if __name__ == "__main__":
    print(find_duplicate(find_duplicate_file('./')))
