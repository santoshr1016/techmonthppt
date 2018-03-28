from functools import reduce


def sum_of_all(x, y):
    return x + y

res = reduce(sum_of_all, ['a', 'd', 's'])
print(res)

# Lambda way
res = reduce(lambda x, y: x+y, range(11))
print(res)
