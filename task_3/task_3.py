from random import randint


class MagicNumber:
    _number = 0

    def add_number(self, number):
        try:
            with open('numbers.txt', 'a', encoding='utf-8') as f:
                f.writelines(f'{number}\n')
        except FileNotFoundError:
            print('Файл не найден')

    def run(self):
        while self._number <= 777:
            num = int(input('Введите число: '))
            if not randint(0, 13):
                raise Exception('Вас постигла неудача!')
            else:
                self.add_number(num)
                self._number += num
        print('Победа!')


if __name__ == '__main__':
    m1 = MagicNumber()
    m1.run()
