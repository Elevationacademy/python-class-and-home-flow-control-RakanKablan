def my_sum(num1, num2):
    return num1 + num2


def my_mul(num1, num2):
    return num1 * num2


def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first


mytup = (11, 22, 33, 44, 55)
print(f'Sum of the elements {mytup} is: {my_reduce(my_sum, mytup)}')
print(f'Multiplication of the elements {mytup} is: {my_reduce(my_mul, mytup)}')
