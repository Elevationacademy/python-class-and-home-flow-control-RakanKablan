
def my_accummulate(seq):
    sum = 0
    for element in seq:
        sum += element
        yield sum

mytup = (11, 22, 33, 44, 55)
print(list(my_accummulate(mytup)))


