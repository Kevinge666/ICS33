def yield_and_skip(iterable,skip):
    i = iter(iterable)
    try:
        while True:
            v = next(i)
            yield v
            for h in range(skip(v)):
                next(i)
    except StopIteration:
        return

if __name__ == '__main__':
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')
