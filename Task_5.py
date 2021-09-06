# Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все слова, которые начинаются с большого
# латинского символа (от A до Z) и заканчиваются 2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002».
# Используйте регулярные выражения.


import re


def find_words(text):
    return list(map(lambda x: x[0] + x[1], re.findall(r"(\b[A-Z][a-z]+\d{2}\b)|(\b[A-Z][a-z]+\d{4}\b)", text)))


if __name__ == "__main__":
    print(find_words(input()))