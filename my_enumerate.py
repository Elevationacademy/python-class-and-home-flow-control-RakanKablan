
def my_enumerate(iterable, start=0):
    counter = start
    for val in iterable:
        yield counter, val
        counter += 1


mytup = (11, 22, 33, 44, 55)
myit = my_enumerate(mytup)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit), None)
