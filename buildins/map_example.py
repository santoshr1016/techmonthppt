def square(num):
    return num**2


def cubic(num):
    return num**3

temp = [1, 2, 3, 4, 5]
print([i*10 for i in temp])
# for i in temp:
#     square(i)

result_square = list(map(square, temp))
print(result_square)

result_cubic = list(map(cubic, temp))
print(result_cubic)


# Lambda way
result_square = list(map(lambda num: num**2, temp))
result_cubic = list(map(lambda num: num**3, temp))

print(result_square)
print(result_cubic)

