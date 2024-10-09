class NameError(Exception):
    def __str__(self):
        return 'Имя должно состоять из двух слов с заглавной буквы'


class EmailError(NameError):
    def __str__(self):
        return 'Email должен содержать символы @.'


class AgeError(NameError):
    def __str__(self):
        return 'Возраст должен быть от 0 до 120'
