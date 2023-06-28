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
                create_note()
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
        with open("notes.json") as file:
            data = json.load(file)
    except:
        data = {"notes": [], "count_id": 0}

    return data


def create_note(): #Функция пошагово создаёт новую заметку, автоматически присваивает id и записывает в файл
    data = create_data()
    notes = data.get('notes')
    count = data['count_id'] + 1 #Получение id на основании ранее имеющихся id в файле заметок
    note = { #Заполнение полей заметки
        "id": count,
        "title": input('Введите заголовок заметки...\n'),
        "body": input('Введите информацию заметки...\n')
    }
    notes.append(note) #Добавление новой заметки к списку уже имеющихся
    data['notes'] = notes
    data['count_id'] = count #обновление значения id для создания следующих заметок

    with open('notes.json', 'w') as file: #запись в файл
        json.dump(data, file)


main()
