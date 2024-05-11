# 1
def computer_counter(counter: int):
    """Функция, которая принимает целое число в качестве аргумента и возвращает строку, содержащую это число и слово
        "компьютер" в нужном склонении по падежам в зависимости от числа"""
    if counter % 10 == 1 and counter % 100 != 11:
        return f'{counter} компьютер'
    elif 2 <= counter % 10 <= 4 and (counter % 100 < 12 or counter % 100 > 14):
        return f'{counter} компьютера'
    else:
        return f'{counter} компьютеров'


if __name__ == '__main__':
    print('Вывод результатов первого задания')
    print(computer_counter(15))
    print(computer_counter(1))
    print(computer_counter(44))
