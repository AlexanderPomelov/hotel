# 3
def prime_numbers(start_num: int, end_num: int):
    """Функция, которая возвращает массив простых чисел в диапазоне"""

    def is_prime(number: int):
        """Функция, которая проверяет, является ли число простым"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    list_prime_numbers = []
    for num in range(start_num, end_num + 1):
        if is_prime(num):
            list_prime_numbers.append(num)

    return list_prime_numbers


if __name__ == '__main__':
    print('Вывод результатов третьего задания')
    print(prime_numbers(11, 20))
    print(prime_numbers(22, 40))
    print(prime_numbers(0, 10))
