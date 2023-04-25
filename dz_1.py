# 1. Реализуем три метода, которые будут возвращать разные исключения
def zero_ex():
    raise ZeroDivisionError('test zero divison exception')

def name_ex():
    raise NameError('test name error exception')

def value_ex():
    raise ValueError('test value error exception')

# 2. При помощи инструкции raise можно вызвать любое стандартное исключение
#    с произвольным текстом, либо же свое собственное

# 3. Реализуем метод, возвращающий разность двух массивов
def two_arrs_sub(arr1: list, arr2: list):
    if len(arr1) != len(arr2):
        raise RuntimeError('arrs lengths are different!')
    res = []
    for i in range(len(arr1)):
        res.append(arr1[i] - arr2[i])
    return res

# 4. Реализуем метод, возвращающий частное двух массивов
def two_arrs_div(arr1: list, arr2: list):
    if len(arr1) != len(arr2):
        raise RuntimeError('arrs lengths are different!')
    res = []
    for i in range(len(arr1)):
        res.append(arr1[i] / arr2[i])
    return res


if __name__ == "__main__":
    # zero_ex()  # ZeroDivisionError
    # name_ex()  # NameError
    # value_ex()  # ValueError

    print(two_arrs_sub([1, 2, 3], [0, 1, 2]))
    # print(two_arrs_sub([1, 2, 3], [0, 1, 2, 3]))  # RuntimeError

    print(two_arrs_div([4, 9, 16], [2, 3, 4]))
    # print(two_arrs_div([4, 9, 16, 21], [2, 3, 4]))  # RuntimeError
