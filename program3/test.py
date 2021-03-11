class_template = '''\
class {type_name}:
    _fields = {fields}
    _mutable = {mutable}
    def __init__(self, {str1}):
        {s}
    def __repr__(self):
        return f'{type_name}({re})'
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
for i in b:
    c += i
    c += ','
    s += 'self.' + i + '=' + i + '\n'
    s += '        '
    q += i + '=' + '{self.' + i + '},'
q = q[:-1]
c = c[:-1]
print(b, c, s)

class_definition = class_template.format(
    type_name=type_name,
    fields=list(b), mutable=mutable, str1=c, s=s, re=q)

# Debug help: uncomment next line, which prints source code for the class
show_listing(class_definition)

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