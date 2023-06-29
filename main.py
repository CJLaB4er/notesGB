from datetime import datetime
import json


def main():
    interface()


def interface():
    while True:
        print('Выберите одну из опций:\n'
              '1 - добавить заметку\n'
              '2 - Вывести список заметок\n'
              '3 - Прочитать заметку\n'
              '4 - редактирование заметки\n'
              '5 - удалить заметку\n'
              '6 - выход из программы\n')

        answer = input()

        match answer:
            case "1":
                print("создание заметки")
                create_note()
            case "2":
                print("вывод списка заметок")
                print_list_notes()
            case "3":
                print("прочитать заметку")
                read_note()
            case "4":
                print("отредактировать заметку")
            case "5":
                print("удаление заметки")
            case "6":
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
    date_stamp = datetime.now().strftime("%d.%m.%Y %H:%M")  # Строка с отметкой времени, последнего изменения
    note = { #Заполнение полей заметки
        "id": str(count),
        "title": input('Введите заголовок заметки...\n'),
        "body": input('Введите информацию заметки...\n'),
        "last_edit":date_stamp
    }

    notes.append(note) #Добавление новой заметки к списку уже имеющихся
    data['notes'] = notes
    data['count_id'] = count #обновление значения id для создания следующих заметок

    with open('notes.json', 'w') as file: #запись в файл
        json.dump(data, file, indent=4, ensure_ascii=False)


def print_list_notes(): #Функция выводит список всех заметок с краткой информацией
    data = create_data()
    count = 0
    for note in data['notes']:
        count+=1
        print(f"{count}). id: {note['id']} \u231a{note['last_edit']} '{note['title']}' ")
    print(f"Всего записей - {count} \n")

def read_note(): #Функция запросит id заметки, и отобразит ее содержимое
    data = create_data()
    choice = input("Введите id необходимой заметки...\n")
    for note in data['notes']:
        if note['id'] == choice:
            print(f"{note['title']}\n"
                  f"{note['body']}\n"
                  f"Последний раз отредактировано: {note['last_edit']}\n"
                  )
            break
    else:
        print(f"Заметка с id = {choice} не найдена\n")


main()
