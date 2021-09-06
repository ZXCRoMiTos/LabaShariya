# Напишите скрипт reorganize.py, который в директории --source создает две директории: Archive и Small.
# В первую директорию помещаются файлы с датой изменения, отличающейся от текущей даты на количество дней более
# параметра --days (т.е. относительно старые файлы). Во вторую – все файлы размером меньше параметра --size байт.
# Каждая директория должна создаваться только в случае, если найден хотя бы один файл, который должен быть
# в нее помещен.


import sys
import os


def reorganize(argv):

    day = 172800

    if argv[1] == '--source' and argv[3] == '--days' and argv[5] == '--size':
        for _, _, files in os.walk(argv[2]):
            for name in files:

                path_to_file = argv[2] + f"\{name}"

                if os.stat(path_to_file).st_size < int(argv[6]):
                    dir_name = argv[2] + "\Small"
                    try:
                        os.mkdir(dir_name)
                    except FileExistsError:
                        pass
                    os.replace(path_to_file, dir_name + f"\{name}")
                    continue

                if os.path.getmtime(path_to_file) / day > int(argv[4]):
                    dir_name = argv[2] + "\Archive"
                    try:
                        os.mkdir(dir_name)
                    except FileExistsError:
                        pass
                    os.replace(path_to_file, dir_name + f"\{name}")


if __name__ == "__main__":
    reorganize(sys.argv)