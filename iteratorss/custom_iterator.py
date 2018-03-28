class CustomIterator:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        if self.num < self.max:
            self.num += 1
            return self.num
        else:
            raise StopIteration


for i in iter(CustomIterator(5)):
    print(i)
# custom_obj = iter(CustomIterator(5))
# next(custom_obj)
# next(custom_obj)
# next(custom_obj)
# next(custom_obj)
# next(custom_obj)


