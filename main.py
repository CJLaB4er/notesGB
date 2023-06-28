import json


def main():
    # data = {"notes": []}
    interface()


def interface():
    while True:
        print('Выберите одну из опций:\n'
              '1 - добавить заметку\n'
              '2 - Вывести список заметок\n'
              '3 - редактирование заметки\n'
              '4 - удалить заметку\n'
              '5 - выход из программы\n')

        answer = input()

        match answer:
            case "1":
                print("создание заметки")
            case "2":
                print("вывод списка заметок")
            case "3":
                print("редактирование заметки")
            case "4":
                print("удаление заметки")
            case "5":
                print("Программа завершена")
                break


def create_data():  # Функция открывает и считывает файл с заметками, при отсутствиии файла, создаёт новый словарь
    try:
        with open("notes1.json") as file:
            data = json.load(file)
    except:
        data = {"notes": [], "count_id": 0}

    return data


main()
