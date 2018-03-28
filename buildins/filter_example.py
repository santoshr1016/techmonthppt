def even_check(num):
    if num%2:
        return True
temp = [1, 2, 3, 4, 5]

ret_list = list(filter(even_check, temp))
print(ret_list)

# Lambda way
# ret = list(filter(lambda x: x%2==0, range(20)))
# print(ret)