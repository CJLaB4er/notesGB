from datetime import datetime
import json


def interface():
    while True:
        print('Выберите одну из опций:\n'
              '1 - Добавить заметку\n'
              '2 - Вывести список заметок\n'
              '3 - Прочитать заметку\n'
              '4 - Редактирование заметки\n'
              '5 - Удалить заметку\n'
              '6 - Выход из программы\n')

        choice = input()

        match choice:
            case "1":
                print("режим создания заметки")
                create_note()
            case "2":
                print("вывод списка заметок")
                print_list_notes()
            case "3":
                print("режим чтения заметки")
                read_note()
            case "4":
                print("режим редактирования заметки")
                edit_note()
            case "5":
                print("режим удаления заметки")
                delete_note()
            case "6":
                print("Программа завершена")
                break
            case _:
                print("команда не распознана, повторите запрос\n")


def create_data():  # Функция открывает и считывает файл с заметками, при отсутствиии файла, создаёт новый словарь
    try:
        with open("notes.json") as file:
            data = json.load(file)
    except:
        data = {"notes": [], "count_id": 0}

    return data


def create_note():  # Функция пошагово создаёт новую заметку, автоматически присваивает id и записывает в файл
    data = create_data()
    notes = data.get('notes')
    count = data['count_id'] + 1  # Получение id на основании ранее имеющихся id в файле заметок
    date_stamp = datetime.now().strftime("%d.%m.%Y %H:%M")  # Строка с отметкой времени, последнего изменения
    note = {  # Заполнение полей заметки
        "id": str(count),
        "title": input('Введите заголовок заметки...\n'),
        "body": input('Введите информацию заметки...\n'),
        "last_edit": date_stamp
    }

    notes.append(note)  # Добавление новой заметки к списку уже имеющихся
    data['notes'] = notes
    data['count_id'] = count  # обновление значения id для создания следующих заметок
    print(f"\nЗаметка с заголовком '{note['title']}' добавлена, присвоен id  = {note['id']}\n")
    save_notes(data)


def print_list_notes():  # Функция выводит список всех заметок с краткой информацией
    data = create_data()
    count = 0
    for note in data['notes']:
        count += 1
        print(f"{count}). id: {note['id']} \u231a{note['last_edit']} '{note['title']}' ")
    print(f"Всего записей - {count} \n")


def read_note():  # Функция запросит id заметки, и отобразит ее содержимое
    print("Введите id необходимой заметки...\n")
    note_data = search_note()
    if len(note_data) > 0:
        print(f"{note_data[0]['title']}\n"
              f"{note_data[0]['body']}\n"
              f"Последний раз отредактировано: {note_data[0]['last_edit']}\n"
              )


def delete_note():  # Функция для удаления заметки по id
    data = create_data()
    print("Введите id заметки, для её удаления...")
    note_data = search_note()
    if len(note_data) > 0:
        data['notes'].pop(note_data[1])
        print(f"Заметка с id = {note_data[0]['id']} {note_data[0]['title']} была удалена")
        save_notes(data)


# Функция сохраняет в файл изменения произведенные с заметками, перед сохранением, производится сортировка по времени последнего изменения
def save_notes(data: dict):
    data['notes'] = sorted(data['notes'], key=return_datetime, reverse=True)
    with open('notes.json', 'w') as file:  # запись в файл
        json.dump(data, file, indent=4, ensure_ascii=False)


def search_note() -> list:  # Функция ищет заметку по id и возвращает список [{элементы заметки}, index], если заметка не найдена, вернется пустой список
    data = create_data()
    i = 0
    note_data = []
    choice = input()
    for note in data['notes']:
        if note['id'] == choice:
            note_data.append(note)
            note_data.append(i)
            return note_data
        i += 1
    else:
        print("Заметка с заданным id не найдена\n")
        return note_data


def edit_note():  # Функция редактирует заголовок и тело заметки по id, обновляется время последнего редактирования
    data = create_data()
    print("Введите id заметки, для её редактирования...")
    note_data = search_note()
    note = note_data[0]
    note['title'] = input("введите новый заголовок\n")
    note['body'] = input("введите новый текст заметки\n")
    note['last_edit'] = datetime.now().strftime("%d.%m.%Y %H:%M")
    data['notes'].pop(note_data[1])
    data['notes'].append(note)
    save_notes(data)

#Данная функция нужна для сортировки заметок по дате создания. Принимает на вход словарь заметки, преобразует строку
# c датой последнего редактирования и возвращает обхект datetime
def return_datetime(note: dict) -> datetime:
    return datetime.strptime(note['last_edit'], '%d.%m.%Y %H:%M')


if __name__ == "__main__":
    interface()
