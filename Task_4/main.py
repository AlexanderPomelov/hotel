# 4
def multiplication_table(number: int):
    """Функция, которая в консоль выводит таблицу умножения.
    На вход функция получает число, до которого выводит таблицу умножения"""
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            print(i * j, end='\t')
        print()


if __name__ == '__main__':
    print('Вывод результатов четвертого задания')
    multiplication_table(5)
    multiplication_table(7)
    multiplication_table(3)
