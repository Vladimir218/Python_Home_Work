def val_checker(callback):
    def _val_checker(func):
        def wrapper(num):
            if callback(num):
                result = func(num)
                return result
            else:
                raise ValueError(f'wrong val {num}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(30)
print(a)
