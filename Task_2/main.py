# 2
def common_divisors(arr: list):
    """Функция, которая на вход получает массив положительных целых чисел произвольной длины.
    На выходе возвращает массив чисел, которые являются общими делителями для всех указанных чисел"""

    def find_divisors(number: int):
        """Функция, которая на вход получает число и находит его делители"""
        list_divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                list_divisors.append(i)
        return list_divisors

    set_common_divisors = set(find_divisors(arr[0]))
    for num in arr[1:]:
        divisors = find_divisors(num)
        set_common_divisors = set_common_divisors.intersection(divisors)
    return list(set_common_divisors)


if __name__ == '__main__':
    print('Вывод результатов второго задания')
    print(common_divisors([45, 20, 14]))
    print(common_divisors([48, 12, 18]))
    print(common_divisors([0, 12, 18]))
