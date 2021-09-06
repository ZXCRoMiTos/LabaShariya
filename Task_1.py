# Напишите скрипт, который читает текстовый файл и выводит символы в порядке убывания частоты встречаемости в тексте.
# Регистр символа не имеет значения. Программа должна учитывать только буквенные символы (символы пунктуации, цифры и
# служебные символы слудет игнорировать).


import collections


def frequency_analysis(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        filtered_text = map(lambda x: x.lower(), filter(lambda x: x.isalpha(), text))

        list_text = collections.Counter(filtered_text).items()
        result = []

        for letters, number in list_text:
            result.append(f"{letters} : {round((number / len(text)), 2)}")

        return result


def presentation(list):
    for el in list:
        print(el)


if __name__ == '__main__':
    presentation(frequency_analysis('test.txt'))