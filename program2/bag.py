# Submitter: yuxig5(Ge, Yuxi)
# Partner  : (Pan, Jiacheng)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from copy import deepcopy
from collections import defaultdict
from goody import type_as_str
import prompt


class Bag:
    def __init__(self, bl=''):
        self.dic = defaultdict(int)
        for i in bl:
            self.dic[i] = bl.count(i)

    def __repr__(self):
        a = ''
        for i in self.dic:
            for n in range(self.dic[i]):
                a += '\'' + i + '\', '
        a = a[:-2]

        return 'Bag([' + a + '])'

    def __str__(self):
        a = ''
        for i in self.dic:
            a += i + '[' + str(self.dic[i]) + '], '
        a = a[:-2]
        return 'Bag(' + a + ')'

    def __len__(self):
        return sum(self.dic.values())

    def unique(self):
        i = 0
        for b in self.dic:
            i += 1
        return i

    def __contains__(self, item):
        if item in self.dic.keys():
            return True
        else:
            return False

    def add(self, name):
        if name in self.dic:
            self.dic[name] += 1
        else:
            self.dic[name] = 1

    def count(self, item):
        lst = []
        for i in self.dic:
            lst.append(i)
        if item in lst:
            return self.dic[item]
        else:
            return 0

    def __add__(self, right):
        lst = []
        if type(right) != Bag:
            raise TypeError
        for i in right.dic:
            for n in range(right.dic[i]):
                lst.append(i)
        for i in self.dic:
            for n in range(self.dic[i]):
                lst.append(i)
        return Bag(lst)

    def remove(self, name):
        if name in self.dic:
            self.dic[name] -= 1
            if self.dic[name] == 0:
                del self.dic[name]

        else:
            raise ValueError

    def __eq__(self, d):
        if type(d) != Bag:
            return False

        if self.dic == d.dic:
            return True
        else:
            return False

    def __ne__(self, d):
        if type(d) != Bag:
            return True
        if self.dic != d.dic:
            return True
        else:
            return False

    def __iter__(self):
        if 'n' in self.__dict__:
            if self.k != self.dic:
                self.n = self.dic.copy()
                self.k = self.n.copy()
                return self
            else:
                self.n = self.m.copy()
                self.k = self.n.copy()
                return self
        else:
            self.n = self.dic.copy()
            self.k = self.n.copy()
            self.m = deepcopy(self.dic)
            return self

    def __next__(self):
        if sum(self.n.values()) == 0:
            raise StopIteration
        else:
            for i in self.n:
                for n in range(self.n[i]):
                    if self.n[i] >= 1:
                        self.n[i] -= 1
                        return i

if __name__ == '__main__':
    import driver

    driver.default_file_name = 'bscp21F20.txt'
    #     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
    #     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
    #     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
    # Simple tests before running driver
    # Put your own test code here to test Bag before doing the bsc tests
    # Debugging problems with these tests is simpler
'''
    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)

    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
'''
