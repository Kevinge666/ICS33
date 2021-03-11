# Submitter: jiachep1(Pan, Jiachen)
# Partner  : yuxig5(Ge, Yuxi)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # Start off binding the class attribute to True allowing checking to occur
    #   (but iff the function's self._checking_on is likewise bound to True)
    checking_on  = True
  
    # To check the decorated function, bind its self._checking_on as True
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Start off by matching check's function annotation with its arguments
        if annot is None:
            pass
        elif type(annot)==type:
            assert type(value)==annot,f'\'{param}\' failed annotation check(wrong type): value =\'{value}\'\n  ' \
                                            f'was type {type_as_str(value)} ...should be type {str(annot)[8:-2]}'
        elif isinstance(annot,list):
            
            assert type(value)==list,f'\'{param}\' failed annotation check(wrong type): value =\'{value}\'\n  ' \
                                           f'was type {type_as_str(value)} ...should be type list'
            if len(annot)==1:
                if inspect.isfunction(annot[0]) == True:
                    for i in value:
                        self.check(param,annot[0],i)
                elif type(annot[0])==list or type(annot[0])==tuple:
                    s=-1
                    for i in value:
                        for j in i:
                            s+=1
                            assert type(j)==annot[0][0]
                else:           
                    s=-1
                    for i in value:
                        s+=1
                        assert type(i)==annot[0],f'\'{param}\' failed annotation check(wrong type): value =\'{i}\'\n  ' \
                                               f'was type {type_as_str(i)} ...should be type {str(annot[0])[8:-2]}''\n'\
                                               f'list[{s}] check: {annot[0]}'
            else:
                assert len(annot)==len(value),f'\'{param}\' failed annotation check(wrong number of elements): value = {value}\n  ' \
                                                  f'annotation had {len(annot)} elements{annot}'
                for i in range(len(annot)):
                    assert annot[i]==type(value[i])
        elif isinstance(annot, set) is True:
            assert type(value) == set, f'{param} failed annotation check(wrong type): value = {value}\n  ' \
                                       f'was type {type(value)} ...should be type {type(annot)}'
            assert len(annot) == 1, f'{param} annotation inconsistency: set should have 1 item but had {len(annot)}\n  ' \
                                    f'annotation = {annot}'

            for a in annot:
                for b in value:
                    assert type(b) == a, f'{param} failed annotation check(wrong type): value = {b}\n  ' \
                                         f'was type {type(b)} ...should be type {type(a)}\nset value check: {a}'

        elif isinstance(annot, frozenset) is True:
            assert type(value) == frozenset, f'{param} failed annotation check(wrong type): value = {value}\n  ' \
                                             f'was type {type(value)} ...should be type {type(annot)}'
            assert len(annot) == 1, f'{param} annotation inconsistency: frozenset should have 1 item but had {len(annot)}\n  ' \
                                    f'annotation = {annot}'
            for a in annot:
                for b in value:
                    assert type(b) == a, f'{param} failed annotation check(wrong type): value = {b}\n  ' \
                                          f'was type {type_as_str(b)} ...should be type {type(a)}\n' \
                                          f'frozenset value check: {a}'
        elif isinstance(annot, dict) is True:
            for i in annot.keys():
                if type(i)==Check_All_OK or type(annot[i])==Check_All_OK:
                    for a,b in value.items():
                        try:
                            i.__check_annotation__(self.check,param,a,'')
                            annot[i].__check_annotation__(self.check,param,b,'')
                        except Exception:
                            raise AssertionError
                else:        
                    assert type(value) == dict, f'{param} failed annotation check(wrong type): value = {value}\n  ' \
                                                f'was type {type_as_str(value)} ...should be type {type_as_str(annot)}'
                    assert len(annot) <= 1, f'{param} annotation inconsistency: dict should have 1 item but had {len(annot)}\n  ' \
                                            f'annotation = {annot}'
                    for a,b in value.items():
                        for i in annot.keys():
                            assert type(a)==i,f'{param} failed annotation check(wrong type): value = {value}' \
                                                     f'was type {type(value)} ...should be type {type(annot)}' \
                                                     f'dict key check: {annot}'
                            assert type(b)==annot[i],f'{param} failed annotation check(wrong type): value = {value}' \
                                                     f'was type {type(value)} ...should be type {type(annot)}' \
                                                     f'dict value check: {annot}'
        elif inspect.isfunction(annot) == True:
            assert len(annot.__code__.co_varnames) == 1, f'{param} annotation inconsistency: predicate should have 1 ' \
                                                         f'parameter but had {len(annot.__code__.co_varnames)}\n  ' \
                                                         f'predicate = {annot}'
                    
            try:
                assert annot(value)==True
            except Exception as new:
                if type(new) == AssertionError:
                    word = f'{param} failed annotation check: value = {value}\n  predicate = {annot}'
                else:
                    word = f'{param} annotation predicate({annot}) raised exception\n  exception = {type(new)}: {new}'
                raise AssertionError(word)
        elif isinstance(annot, tuple) is True:
            assert type(value) is tuple, f'{param} failed annotation check(wrong type): value = {value}\n  ' \
                                         f'was type {type_as_str(value)} ...should be type {type_as_str(annot)}'

            
            if len(annot)==1:
                if type(annot[0])==tuple or type(annot[0])==list:
                    s=-1
                    for i in value:
                        for j in i:
                            s+=1
                            assert type(j)==annot[0][0]
                else:           
                    s=-1
                    for i in value:
                        s+=1
                        assert type(i)==annot[0]
            else:
                assert len(value) == len(annot), f'\'{param}\' failed annotation check(wrong number of elements): ' \
                                                 f'value = {value}\nannotation had {len(annot)} elements{annot}'
                for i in range(len(annot)):
                    assert annot[i] == type(value[i]), f'\'{param}\' failed annotation check(wrong number of elements): ' \
                                     f'value = {value[i]}\n  was type {type_as_str(value[i])} ' \
                                     f'...should be type {str(annot[i])[8:-2]} \n list[{i}] check: {annot[i]} '
        elif isinstance(annot, str) is True:
            if len(param)==1:
                try:
                    assert eval(annot.replace(param,str(value)))
                except Exception:
                    raise AssertionError
            else:
                for i in range(len(param)):
                    annot=annot.replace(param[i],str(value[i]))
                try:
                    assert eval(annot)
                except Exception:
                    raise AssertionError
        elif annot is not None:
            try:
                annot.__check_annotation__()
            except Exception:
                raise AssertionError(f'\'{param}\' annotation undecipherable: {annot}')
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        # Return the parameter/argument bindings via an ordereddict (a special
        #   kind of dict): it binds the function header's parameters in order
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        try:
            s=0
            annotations = self._f.__annotations__
            for keys, values in param_arg_bindings().items():           
                if keys in annotations:
                    #self.check(keys, annotations[keys], param_arg_bindings()[keys])
                    b=keys
                    a=annotations[keys]
                    c=param_arg_bindings()[keys]
                else:
                    s+=1
            if s!=0:
                for keys, values in param_arg_bindings().items():           
                    if keys not in annotations:
                        self.check((keys,b), a, (param_arg_bindings()[keys],c))
                        s=0
            else:
                self.check(b, a, c)
            result = self._f(**param_arg_bindings())
            if self.checking_on and self._checking_on:
                if 'return' in annotations:
                    assert type(result) == annotations['return']
            return result
            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it
            
            # Return the decorated answer
            
            #remove after adding real code in try/except
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #    print(l.rstrip())
            #print(80*'-')
            raise AssertionError




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    
    def f(x:int): pass
    f = Check_Annotation(f)
    #f(3)
    #f('a')
    #driver tests
    import driver
    driver.default_file_name = 'bscp4F20.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
