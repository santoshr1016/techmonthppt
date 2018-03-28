def make_pretty(func):
    def inner():
        print("*"*22)
        func()
        print("*" * 22)
    return inner

# @make_better
@make_pretty
def ordinary():
    print("I am ordinary function")


ordinary()

# Lets decorate ordinary function
# pretty = make_pretty(ordinary)
# pretty()

def smart_divide(func):
    def inner(a,b):
        print("I am going to divide a/b")
        if b == 0:
            print("b cannot be Zero")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(10, 2))
print(divide(10, 0))
