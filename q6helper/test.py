class popdict(dict):
    def __init__(self, initial_dict=[], **kargs):
        a = 0
        self.dict = {}
        self.popular = {}
        lst = []
        for i in initial_dict:
            b = list(i)
            while a < len(b) - 1:
                self.dict[b[a]] = b[a + 1]
                a += 2
        for keys, values in kargs.items():
            self.dict[keys] = values
        for i in self.dict.keys():
            lst.append(i)
            self.popular[i] = lst.count(i)

    def __getitem__(self, key):
        self.popular[key] = self.popular[key] + 1
        self.dict[key] = self.dict[key] + 1

    def __setitem__(self, key, value):
        if key in self.dict:
            self.dict[key] += 1
        else:
            self.dict = 1
        if key in self.popular:
            self.popular[key] += 1
        else:
            self.popular = 1

    def __delitem__(self, key):
        del self.dict[key]
        del self.popular[key]

    def __call__(self, key):
        if key in self.dict:
            return self.popular[key]
        else:
            return 0

    def clear(self):
        self.dict.clear()
        self.popular.clear()

    def __iter__(self):
        self.popular = dict(sorted(self.popular.keys(), key=lambda x: -x))
        for i in self.popular:
            yield i
