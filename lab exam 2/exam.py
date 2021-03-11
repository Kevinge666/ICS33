from goody import type_as_str  # Useful in some exceptions
import prompt                  # Use some functions here if needed

class DictList:
    def __init__(self, *dl):
        self.dl = []
        if dl == ():
            raise AssertionError
        for i in dl:
            if type(i) is not dict:
                raise AssertionError
            else:
                self.dl.append(i)

    def __len__(self):
        lst = []
        for i in self.dl:
            for keys, values in i.items():
                lst.append(keys)
        return len(list(set(lst)))

    def __repr__(self):
        a = 'DictList('
        for i in self.dl:
            a = a + str(i) + ', '
        a = a[:-2]
        a = a + ')'
        return a

    def __contains__(self, item):
        for i in self.dl:
            for keys, valus in i.items():
                if keys == item:
                    return True
        return False

    def __getitem__(self, item):
        dic = {}
        for i in self.dl:
            for keys, values in i.items():
                dic[keys] = values
        if item not in dic.keys():
            raise KeyError
        else:
            return dic[item]

    def __setitem__(self, key, value):
        dic = {}
        new_dic = {}
        for i in self.dl:
            for keys, values in i.items():
                dic[keys] = values
        if key in dic.keys():
            for i in self.dl:
                for a, b in i.items():
                    if a == key and b == dic[key]:
                        i[key] = value
            return self.dl
        else:
            new_dic[key] = value
            self.dl.append(new_dic)
            return self.dl

    def __call__(self, items):
        dic = {}
        a = -1
        for i in self.dl:
            a += 1
            for keys, values in i.items():
                if items == keys:
                    dic[a] = values
        return list(tuple(dic.items()))

    def __iter__(self):
        self.dl.reverse()
        lst = []
        for i in self.dl:
            for keys, values in i.items():
                if keys not in lst:
                    lst.append(keys)
                    yield (keys, values)

    def __eq__(self, right):
        if type(right) is not DictList and not dict:
            raise TypeError
        elif type(right) is int or len(right) == 0:
            raise TypeError
        else:
            dic = {}
            for i in self.dl:
                for keys, values in i.items():
                    dic[keys] = values
            if type(right) is DictList:
                new_dic = {}
                for i in right.dl:
                    for keys, values in i.items():
                        new_dic[keys] = values
                return dic == new_dic
            if type(right) is dict:
                return dic == right

            
if __name__== '__main__':      
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = r"bscile2F20.txt"      
    #Uncomment the following lines to SEE MORE DETAILS on exceptions      
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
