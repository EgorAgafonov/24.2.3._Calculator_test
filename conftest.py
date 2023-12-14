import time


def time_of_test(func):
    """Функция-декоратор для определения длительности авто-теста с момента запуска\до момента его окончания."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"\n\nНачало выполнения теста: {time.asctime()}")

        func(*args, **kwargs)

        end_time = time.time()
        print(f"Окончание выполнения теста: {time.asctime()}")
        result = end_time - start_time
        print(f"Общая продолжительность выполнения теста: {round(result, 3)} сек.")

    return wrapper
