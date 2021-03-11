class a(dict):
    pass
b=a()
print(isinstance(b, dict))

a={1,2}
b=[3]
b+=a
print(b)
b=sorted(b, key=None, reverse=False)
print(b)