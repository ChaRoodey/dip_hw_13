class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename

    def display_massages(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    print(line, end='')
        except FileNotFoundError:
            print('Файл не найден')

    def add_massage(self, name, massage):
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.writelines(f'{name}: {massage}\n')
        except FileNotFoundError:
            print('Файл не найден')

    def run(self):
        name = input('Как вас зовут? ')
        print(f'Привет {name}, это чат\n1 - Отправить сообщение\n2 - Просмотреть сообщения\n3 - Выйти')
        while True:
            action = int(input('Выберете действие: '))
            if action == 1:
                self.add_massage(name, input('Введите сообщение: '))
                print('Сообщение отправлено!')
            elif action == 2:
                self.display_massages()
            elif action == 3:
                print('Выход из чата...')
                break
            else:
                print('Неизвестная команда')


class User:
    def __init__(self, name: str):
        self.name = name


if __name__ == '__main__':
    chat = Chat()
    chat.run()
