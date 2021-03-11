# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    a = ''
    for i in iterables:
        for m in i:
            a = a + m
    yield a


def group_when(iterable, p):
    a = ''
    for i in iterable:
        a = a + i
    ly = []
    new = []
    for i in a:
        if p(i) is True:
            ly.append(i)
            new.append(ly)
            ly = []
        else:
            ly.append(i)
    if len(ly) != 0:
        new.append(ly)
    for i in new:
        yield i


def drop_last(iterable, n):
    a = ''
    for i in iterable:
        a = a + i
    a = a[:-n]
    yield a


def yield_and_skip(iterable, skip):
    lst = []
    m = 0
    a = ''
    b = ''
    for i in iterable:
        a = a + i
    while m < len(a):
        lst.append(a[m])
        m = m + skip(a[m]) + 1
    for q in lst:
        b += q
    yield b


def alternate_all(*args):
    result = ''
    a = []
    for i in args:
        lst = []
        for m in i:
            lst.append(m)
        a.append(lst)
    all_lst = []
    for i in a:
        for m in i:
            all_lst.append(m)
    re = []
    num = 0
    c = len(a[0])
    for i in a:
        b = len(i)
        if b < c:
            c = b
    while num < c:
        for i in a:
            re.append(i[num])
        num += 1
    q = min(a, key=len)
    a.remove(q)
    r = len(a[0])
    for i in a:
        b = len(i)
        if b < r:
            r = b
    while num < r:
        for i in a:
            re.append(i[num])
        num += 1
    for i in all_lst:
        if i not in re:
            re.append(i)
    for i in re:
        result = result + i
    yield result


def min_key_order(adict):
    lst = []
    while len(lst) != len(adict):
        x = iter(sorted(adict.items()))
        for i in x:
            yield i
            lst.append(i)


if __name__ == '__main__':
    from goody import irange

    import driver

    driver.default_file_name = "bscq4F20.txt"
    #     driver.default_show_exception=True
    #     driver.default_show_exception_message=True
    #     driver.default_show_traceback=True
    driver.driver()

''' 
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test min_key_order; add your own test cases
    print('\nTesting Ordered')
    d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
    i = min_key_order(d)
    print(next(i))
    print(next(i))
    del d[8]
    print(next(i))
    d[32] = 'z'
    print(next(i))
    print(next(i))
'''
