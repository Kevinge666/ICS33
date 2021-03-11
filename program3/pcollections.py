import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False, defaults={}):
    def show_listing(s):
        for line_nmber, line_txt in enumerate(s.split('\n'), 1):
            print(f' {line_nmber: >3} {line_txt.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class

    re_ex = re.compile('^([a-zA-Z]{1}\w*)$')
    if re.match(re_ex, str(type_name)) is None:
        raise SyntaxError
    if type(field_names) == list or type(field_names) == str:
        a = ''
        for i in field_names:
            if i != ' ' and i != ',':
                a += i
            else:
                if a != '':
                    if a in keyword.kwlist == True:
                        raise SyntaxError
                    elif re.match(re_ex, a) is None:
                        raise SyntaxError
                    else:
                        a = ''
        if a in keyword.kwlist:
            raise SyntaxError
        elif re.match(re_ex, a) is None:
            raise SyntaxError
    else:
        raise SyntaxError

    class_template = '''\
import copy
class {type_name}:
    _fields = {fields}
    _mutable = {mutable}
    def __init__(self, {str1}):
        {s}
    def __repr__(self):
        return f'{type_name}({re})'
    {g}
    def __getitem__(self, index):
        if type(index) not in (str, int):
            raise IndexError
        if type(index) is str:
            if index not in {fields}:
                raise IndexError
            else:
                return self.__dict__[index]
        if type(index) is int:
            if index<=len(self._fields)-1:
                return self.__dict__[self._fields[index]]
            else:
                raise IndexError

    def __eq__(self,right):
        return str(self) == str(right)
        
    def _asdict(self):
        return self.__dict__
    def _make(it):
        st=''
        for i in range(len({fields})):
            st+={fields}[i]+'='+str(it[i])+','
        st=st[:-1]
        return '{type_name}('+st+')'
    def _replace(self, **kargs):
        if self._mutable:
            for keys, values in kargs.items():
                if keys not in self._fields:
                    raise TypeError
                else:
                    self.__dict__[keys] = values
            return 
        else:
            dict = copy.deepcopy(self)
            for keys, values in kargs.items():
                if keys in dict._fields:
                    dict.__dict__[keys] = values
                else:
                    raise TypeError
            return dict
    def __setattr__(self,a,b):
        if self._mutable==False:
            if a in self.__dict__:
                raise AttributeError
            self.__dict__[a] = b
        else:
            self.__dict__[a] = b        
    '''
    if type(field_names) == str:
        field_names = field_names.replace(',', '')

        a = field_names.split(' ')
        b = a.copy()
        for i in a:
            if i == '':
                b.remove(i)
    else:
        for i in field_names:
            if i == ' ':
                field_names.remove(i)
        b = field_names
    c = ''
    s = ''
    q = ''
    g = ''
    for i in b:
        c += i
        c += ','
        s += 'self.' + i + '=' + i + '\n'
        s += '        '
        q += i + '=' + '{self.' + i + '},'

        g += 'def get_' + i + '(self):' + '\n'
        g += '        '
        g += 'return self.'+i
        g += '\n    '
    q = q[:-1]
    c = c[:-1]
    class_definition = class_template.format(type_name=type_name,
                                             fields=list(b),
                                             mutable=mutable,
                                             str1=c, s=s, re=q,
                                             g=g)

    # Debug help: uncomment next line, which prints source code for the class
    #show_listing(class_definition)

    # Execute the class_definition's str in name_space; next bind its
    #   source_code attribute to this class_definition; following try+except
    #   return the class object created; if there are any syntax errors, show
    #   the class and also show the error
    name_space = dict(__name__=f'pnamedtuple_{type_name}')
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError, SyntaxError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')

    # driver tests
    import driver

    driver.default_file_name = 'bscp3F20.txt'
    #     driver.default_show_exception_message= True
    #     driver.default_show_traceback= True
    driver.driver()
