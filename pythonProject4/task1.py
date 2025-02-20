from csv import DictWriter, DictReader
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(first_name) < 5:
                raise NameError("Слишком короткфя фамилия")
        except NameError as err:
            print(err)
        else:
            flag = True
    phone = "+73287282037"
    return [first_name, last_name, phone]


def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standard_write(filename, res)


def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена"


def delete_row(filename):
    row_number = int(input("Введите номер строки"))
    res = read_file(filename)
    res.pop(row_number-1)
    standard_write(filename, res)


def standard_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def change_row(filename):
    row_number = int(input("Введите номер строки"))
    res = read_file(filename)
    data = get_data()
    res[row_number-1]["Имя"] = data[0]
    res[row_number - 1]["Фамилия"] = data[1]
    res[row_number - 1]["Телефон"] = data[2]
    standard_write(filename, res)


def copy_row(source_file, target_file):
    row_number = int(input("Введите номер строки для копирования: "))
    res = read_file(source_file)
    if row_number < 1 or row_number > len(res):
        print("Неверный номер строки.")
        return
    row_to_copy = res[row_number - 1]
    write_file(target_file, [row_to_copy["Имя"], row_to_copy["Фамилия"], row_to_copy["Телефон"]])
    print(f"Запись {row_number} успешно скопирована в {target_file}.")


filename = 'phone.csv'


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(read_file(filename))
        elif command == "f":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(filename))
        elif command == "d":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            delete_row(filename)
        elif command == "d":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            elif command == "c":
                source_file = input("Введите имя исходного файла: ")
                target_file = input("Введите имя целевого файла: ")
                if not exists(source_file):
                    print(f"Файл {source_file} не существует.")
                    continue
                if not exists(target_file):
                    create_file(target_file)
                copy_row(source_file, target_file)
            elif command == "e":
                if not exists('phone.csv'):
                    print("Файл не существует. Создайте его.")
                    continue
            change_row(filename)


main()