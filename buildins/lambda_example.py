from functools import reduce

def double(num):
    return num * 2

print(double(5))

d = lambda x: x * 2

print(d(5))


def is_even(num):
    if num%2 ==0:
        return True
    return False

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

even_list = []

for i in my_list:
    if is_even(i):
        even_list.append(i)
print(even_list)


def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print(find_max(22, 100))
# print(reduce(find_max, [34, 23, 44, 99, 3232, 20, 10]))
