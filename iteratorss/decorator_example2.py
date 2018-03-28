# Higher order functions : Functions that take other functions as args are called HOF
def inc(num):
    return num + 1


def dec(num):
    return num - 1


def operate(func, num):
    res = func(num)
    return res

operate(inc, 100)

# A function can return another function
def is_called():
    def is_returned():
        print("Hello, I am returned by is_called function")
    return is_returned

new = is_called()
new()
