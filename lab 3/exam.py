from predicate import is_even
from ile3helper import ints, primes, is_prime, hide, nth, nth_for_m
from collections import defaultdict


def zip_skip(predicate: callable, exception_bool, *iterables):
    args = [iter(i) for i in iterables]
    while True:
        lst = []
        result = []
        for i in args:
            try:
                b = next(i)
                result.append(b)
            except StopIteration:
                return
            if type(b) == int:
                lst.append(predicate(b))
            elif type(b) == str:
                lst.append(exception_bool)
        if lst == [True, True]:
            yield tuple(result)
        elif len(result) == 0:
            return


def closest_sums(ns: [int], l1: [int], l2: [int]) -> [[int], [int]]:
    pass


class shared_dict(dict):
    # Write __init_, __setitem, and __delitem__ below, after str/verify_shared

    # Useful for debugging: see the state of all the dictionaries       
    def __str__(self):
        return f'  # _counts     = {dict.__repr__(self._counts)}\n  # _stored_kvs = {dict.__str__(self._stored_kvs)}\n  # shared_dict = {dict.__str__(self)}'

    def verify_shared(self, trace_all=False):
        errors = 0
        vd = defaultdict(list)

        def check(name_checking, d_checking):
            nonlocal errors
            if trace_all: print(f'\nChecking {name_checking} for shared objects')
            for k, v in d_checking.items():
                if trace_all: print('  ......')
                if trace_all: print(f'  key   {k} = {object.__repr__(k)}')
                vd.setdefault(k, k)
                if vd[k] is not k:
                    errors += 1
                    print(f'  ERROR: in {name_checking} key   {k} does not refer to the correct object')

                if trace_all: print(f'  value {v} = {object.__repr__(v)}')
                vd.setdefault(v, v)
                if vd[v] is not v:
                    errors += 1
                    print(f'  ERROR: in {name_checking} value {v} does not refer to the correct object')

        check('_counts', self._counts)
        check('_counts', self._stored_kvs)
        check('shared_dict', self)
        return errors

    def __init__(self):
        dict.__init__(self)
        self._counts = {}
        self._stored_kvs = {}

    def __setitem__(self, key, value):
        if key in self._counts:
            self._counts[key] += 1
        else:
            self._counts[key] = 1
        if value in self._counts:
            self._counts[value] += 1
        else:
            self._counts[value] = 1
        if key not in self._stored_kvs:
            self._stored_kvs[key] = key
        if value not in self._stored_kvs:
            self._stored_kvs[value] = value
        dict.__setitem__(self,self._stored_kvs[key],self._stored_kvs[value])

    def __delitem__(self, key):
        self._counts[key] = self._counts[key] - 1
        if self._counts[key] == 0:
            del self._counts[key]
            del self._stored_kvs[key]
        self._counts[dict.__getitem__(self, key)] = self._counts[dict.__getitem__(self, key)] - 1
        if self._counts[dict.__getitem__(self, key)] == 0:
            del self._counts[dict.__getitem__(self, key)]
            del self._stored_kvs[dict.__getitem__(self, key)]
        dict.__delitem__(self, key)


if __name__ == '__main__':
    # print('\n\nTesting zip_skip')
    #
    # print("for i in zip_skip( (lambda x : x%2 == 0), False )\n  ... should produce nothing")
    # for i in zip_skip( (lambda x : is_even(x)), False ):
    #     print(' ',i)
    #
    # print("\nzip_skip( (lambda x : is_even(x)), False, hide([0, 0, 1, 1, 0]), hide([0, 1, 0, 1, 'X']))\n  ... should produce (0, 0)")
    # for i in zip_skip( (lambda x : is_even(x)), False, hide([0, 0, 1, 1, 0]), hide([0, 1, 0, 1, 'X'])):
    #     print(' ',i)
    #
    # print("\nzip_skip( (lambda x : is_even(x)), True, hide([0, 0, 1, 1, 0]), hide([0, 1, 0, 1, 'X']))\n   ... should produce (0, 1) and (0, 'X')")
    # for i in zip_skip( (lambda x : is_even(x)), True, hide([0, 0, 1, 1, 0]), hide([0, 1, 0, 1, 'X'])):
    #     print(' ',i)
    #
    # print("\nnth_for_m(primes(),10,3))\n...should produce\n[29, 31, 37]")
    # print( nth_for_m(primes(),10,3))
    #
    # print("\nnth_for_m(zip_skip( (lambda x : x%10 == 7), True, ints(), primes()),50,10)\n...should produce\n[(1777, 15227), (1797, 15377), (1807, 15467), (1877, 16127), (1927, 16657), (1967, 17047), (1977, 17167), (1997, 17377), (2027, 17627), (2037, 17747)]")
    # print( nth_for_m(zip_skip( (lambda x : x%10 == 7), True, ints(), primes()),50,10) )

    #
    # print('\n\nTesting closest_sums. Feel free to test other cases: e.g, base cases you choose')
    #
    # print('  closest_sums([],[],[])      = ',closest_sums([],[],[]),      '     ...should be [[],[]]     with allowed permutations')
    # print('  closest_sums([8],[],[])     = ',closest_sums([8],[],[]),     '    ...should be [[8],[]]    with allowed permutations')
    # print('  closest_sums([5,8],[],[])   = ',closest_sums([5,8],[],[]),   '   ...should be [[5],[8]]   with allowed permutations')
    # print('  closest_sums([2,5,8],[],[]) = ',closest_sums([2,5,8],[],[]), '...should be [[2,5],[8]] with allowed permutations')
    # print('  closest_sums([1,10,8,11,1,9,10],[],[]) = ',closest_sums([1,10,8,11,1,9,10],[],[]), '...should be [[1, 10, 11, 1],[8,9,10]] with allowed permutations')
    #
    #
    # print('\n\nTesting shared_dict. Feel free to test other cases')
    # print('__setitem__ test: see specifications')
    # sd = shared_dict()
    #
    # print('sd = shared_dict()\n',sd,sep='')
    # sd['a'] = tuple([1,2,3])
    # print("\nsd['a'] = tuple([1,2,3])\n",sd,sep='')
    #
    # sd['b'] = tuple([1,2,3])
    # print("\nsd['b'] = tuple([1,2,3])\n",sd,sep='')
    #
    # print("\nprint(sd['a'] is sd['b'])\n","  ",sd['a'] is sd['b'],sep='')
    #
    # sd['c'] = 'c'
    # print("\nsd['c'] = 'c'\n",sd,sep='')
    #
    # sd[tuple([1,2,3])] = 'd'
    # print("\nsd[tuple([1,2,3])] = 'd'\n",sd,sep='')
    #
    # print('\nverifying all equal (==) objects are shared; set trace_all = True for more details')
    # errors = sd.verify_shared(trace_all=False)
    # if errors != 0:
    #     print(f'---found {errors} objects not shared correctly')
    # else:
    #     print('---All are correctly shared')
    #
    # print('\n\n__delitem__ test: see specifications')
    # del sd['a']
    # print("\ndel sd['a']\n",sd,sep='')
    # del sd['b']
    # print("\ndel sd['b']\n",sd,sep='')
    # del sd['c']
    # print("\ndel sd['c']\n",sd,sep='')
    # del sd[tuple([1,2,3])]
    # print("\ndel sd[tuple([1,2,3])]\n",sd,sep='')
    #
    # print('\n\n__setitem__ EXTRA CREDIT test: see specifications')
    # sd = shared_dict()
    # print('sd = shared_dict()\n',sd,sep='')
    # sd['a'] = tuple([1,2,3])
    # print("\nsd['a'] = tuple([1,2,3])\n",sd,sep='')
    # sd['a'] = frozenset([1,2])
    # print("\nsd['a'] = frozenset([1,2])\n",sd,sep='')
    #
    # print()
    import driver

    # Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bscile3F20.txt'
    # But better to debug putting testing code above
    #     driver.default_show_exception=True
    #     driver.default_show_exception_message=True
    driver.driver()
