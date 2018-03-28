number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

zipped = list(zip(number_list, str_list))
print(zipped)

numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
result = zip(numbersList, strList, numbersTuple)
print(list(result))
