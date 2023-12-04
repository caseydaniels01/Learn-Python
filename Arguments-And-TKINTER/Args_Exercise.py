
def add(*args):
    i=0
    for n in args:
        i += n
    return i

print(add(1,2,3,4,5))
    

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add=3, multiply=5)


def combined(a, *args, **kwargs):
    print(a, args, kwargs)

combined(4, 7, 3, 0, x=10, y=64)