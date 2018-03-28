def gen_function():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

gen = gen_function()
print(next(gen))
print(next(gen))
print(next(gen))

# using the for loop
# for item in gen_function():
#     print(item)
