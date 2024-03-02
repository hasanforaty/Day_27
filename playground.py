def add(*args):
    su = 0
    for n in args:
        su += n
    return su


print(add(10, 20, 30, 40))


def calculate(n, **kwargs):
    keys = kwargs.keys()
    if 'add' in keys:
        n += kwargs['add']
    if 'subtract' in keys:
        n -= kwargs['subtract']
    if 'multiply' in keys:
        n *= kwargs['multiply']
    return n


result = calculate(10, add=15, multiply=2)
print(result)