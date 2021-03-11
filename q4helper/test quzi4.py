adic = {1: 'a', 2: 'x', 4: 'm', 8: 'd', 16: 'f'}
# adic = list(tuple(adic.items()))
# print(adic)
it = iter(sorted(adic.items()))

print(next(it))
del adic[8]
print(next(it))
print(next(it))
print(next(it))

print(next(it))

