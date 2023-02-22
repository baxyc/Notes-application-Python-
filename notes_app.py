import argparse
import sys
from notes_manager import NotesManager


def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    if notes_manager.create_note(title, content):
        print("Заметка успешно создана.")
    else:
        print("Заметка с таким заголовком уже существует.")


def read_notes_list():
    notes_list = notes_manager.get_notes_list()
    if not notes_list:
        print("Заметок нет.")
    else:
        for note in notes_list:
            print(f"{note.title} ({note.date_created}): {note.content}")


def read_note():
    title = input("Введите заголовок заметки: ")
    note = notes_manager.get_note_by_title(title)
    if note:
        print(f"{note.title} ({note.date_created}): {note.content}")
    else:
        print("Заметка не найдена.")


def edit_note():
    title = input("Введите заголовок заметки: ")
    note = notes_manager.get_note_by_title(title)
    if note:
        print(f"{note.title} ({note.date_created}): {note.content}")
        new_content = input("Введите новый текст заметки: ")
        notes_manager.edit_note_content(title, new_content)
        print("Заметка успешно изменена.")
    else:
        print("Заметка не найдена.")


def delete_note():
    title = input("Введите заголовок заметки: ")
    if notes_manager.delete_note_by_title(title):
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")


def parse_args(args):
    parser = argparse.ArgumentParser(description="Консольное приложение заметки.")
    subparsers = parser.add_subparsers(dest="command", help="Команда")

    create_parser = subparsers.add_parser("create", help="Создать заметку")
    create_parser.set_defaults(func=create_note)

    read_list_parser = subparsers.add_parser("read-list", help="Показать список заметок")
    read_list_parser.set_defaults(func=read_notes_list)

    read_parser = subparsers.add_parser("read", help="Показать заметку")
    read_parser.set_defaults(func=read_note)

    edit_parser = subparsers.add_parser("edit", help="Изменить заметку")
    edit_parser.set_defaults(func=edit_note)

    delete_parser = subparsers.add_parser("delete", help="Удалить заметку")
    delete_parser.set_defaults(func=delete_note)

    return parser.parse_args(args)


if __name__ == "__main__":
    notes_manager = NotesManager('notes.json')

    args = parse_args(sys.argv[1:])
    if hasattr(args, 'func'):
        args.func()
