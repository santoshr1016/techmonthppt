def all_even():
    n = 0
    while True:
        n += 2
        yield n


count = 0
for i in all_even():
    print(i)

# filter(lambda x: x%2==0, range(50))