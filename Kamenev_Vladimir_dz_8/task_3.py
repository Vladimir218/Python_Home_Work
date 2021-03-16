from functools import wraps


def cower(func):
    def wrapper(*args, **kwargs):
        print(f'имя функции в def cower - {func.__name__}')
        result = func(*args, **kwargs)
        return result
    return wrapper


def type_logger(func):
    @wraps(func)
    def wrapper1(*args, **kwargs):
        # result = в условии задачи не сказано как обработать и выводить результат, если на входе не одно значение,
        # а несколько, заданные списком или словарем.
        log = ''
        if args:
            log = [f'{i}: {type(i)} {func.__name__}' for i in args] + [
                f'key - {i}: item - {j} {type(j)} {func.__name__}' for i, j in kwargs.items()]
        print(*log, sep=",\n")
    return wrapper1


@cower
@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(3, 4, 'fdsf', (1, 2, 435), {1: 1}, False, ключ=3)
