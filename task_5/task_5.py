from Exeptions import NameError, AgeError, EmailError


class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __setattr__(self, key, value):
        if key == 'name':
            if not (isinstance(value, str) and str.istitle(value) and ' ' in value):
                raise NameError
        elif key == 'age':
            if not (isinstance(value, int) and 0 <= value <= 120):
                raise AgeError
        elif key == 'email':
            if not (isinstance(value, str) and '@.' in value):
                raise EmailError
        super(User, self).__setattr__(key, value)

    def __str__(self):
        return f'{self.name = }, {self.age = }, {self.email = }'


if __name__ == '__main__':
    try:
        u1 = User('Олег Викторович', 55, 'olegV@.ru')
        print(u1)
    except NameError or AgeError or EmailError as e:
        print(e)
