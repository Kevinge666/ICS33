# Submitter: jiachep1(Pan, Jiachen)
# Partner  : yuxig5(Ge, Yuxi)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming


import prompt

class Sparse_Matrix:

    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
        
    def __init__(self, rows, cols, *matrix):
        s=0
        if type(rows) is not int or rows <= 0:
            raise AssertionError
        if type(cols) is not int or cols <= 0:
            raise AssertionError
        for i in matrix:
            for j in i:            
                if type(j) != int and type(j) != float:
                    raise AssertionError
            if i[0]>(rows-1) or i[1]>(cols-1):
                raise AssertionError
            for d in matrix:
                if i[0]==d[0] and i[1]==d[1]:
                    s+=1
            if s>1:
                raise AssertionError
            s=0
        self.rows = rows
        self.cols = cols
        self.matrix={}
        for i in matrix:
            if i[2]!=0:
                self.matrix[(i[0],i[1])]=i[2]
            
        

    def size(self):
        return '(' + str(self.rows) + ', ' + str(self.cols) + ')'

    def __len__(self):
        return self.cols * self.rows

    def __bool__(self):
        if self.matrix == {}:
            return False
        else:
            return True                                                                                                

    def __repr__(self):
        a='Sparse_Matrix('+str(self.rows)+', '+str(self.cols)
        for i in self.matrix:
            a+=', ('
            for j in i:
                a+=str(j)+', '
            a+=str(self.matrix[i])+')'
        a+=')'
        return a
    
    
    def __getitem__(self,t):
        if t[0]>self.rows-1 or t[0]<0:
            raise TypeError
        if t[1]>self.cols-1 or t[1]<0:
            raise TypeError
        if len(t)!=2:
            raise TypeError
        for i in t:
            if type(i)!=int:
                raise TypeError
        self.matrix.get(t,0)
        if t in self.matrix.keys():
            
            return self.matrix[t]
        else:
            return 0
       
                
        
    def __setitem__(self,t,v):
        if t[0]>self.rows-1 or t[0]<0:
            raise TypeError
        if t[1]>self.cols-1 or t[1]<0:
            raise TypeError
        if len(t)!=2:
            raise TypeError
        for i in t:
            if type(i)!=int:
                raise TypeError
        if type(v)!=int and type(v)!=float:
            raise TypeError
        if v!=0:
            self.matrix[t]=v
        if t in self.matrix.keys():
            if v==0:
                del self.matrix[t]
                
    def __delitem__(self,t):
        if t[0]>self.rows-1 or t[0]<0:
            raise TypeError
        if t[1]>self.cols-1 or t[1]<0:                
            raise TypeError
        if len(t)!=2:
            raise TypeError
        for i in t:
            if type(i)!=int:
                raise TypeError
        if t in self.matrix:
            del self.matrix[t]
    
    def row(self,a):
        lst1=[]
        for i in range(self.rows):
            lst1.append(i)
        if a not in lst1:
            raise AssertionError
        lst=[]
        for i in range (self.cols):
            
            if (a,i) in self.matrix.keys():
                lst.append(self.matrix[(a,i)])
            else:
                lst.append(0)
        return tuple(lst)
    
    def col(self,a):
        lst1=[]
        for i in range(self.cols):
            lst1.append(i)
        if a not in lst1:
            raise AssertionError
        lst=[]
        for i in range (self.rows):
            
            if (i,a) in self.matrix.keys():
                lst.append(self.matrix[(i,a)])
            else:
                lst.append(0)
        return tuple(lst)
    
    def details(self):
        a=''
        a+=str(self.rows)+'x'+str(self.cols) + ' -> '
        a+=str(self.matrix)
        a+=' -> ('
        for i in range(self.rows):
            a+=str(self.row(i))+', '
        a=a[:-1]
        a+=')'
        return a
        
    def __call__(self,a,b):
        
        d=self.matrix.copy()
        lst=[]
        if a<0:
            raise AssertionError
        if b<0:
            raise AssertionError
        if type(a) != int or type(b) != int:
            raise AssertionError
        for i in d:
            if i[0]>=a:
                del self.matrix[i]
            elif i[1]>=b:
                del self.matrix[i]
        for i in self.matrix:
            lst.append((i[0],i[1],self.matrix[i]))
        self.__dict__.clear()
        self.__init__(a, b,*lst)

        
    def __iter__(self):
        lst=[]
        for i in self.matrix:
            lst.append((i[0],i[1],self.matrix[i]))
      
        lst=sorted(lst,key= lambda x : x[2])
   
        t=tuple(lst)
        for i in t:
            
            yield i
    def __pos__(self):
        lst=[]
        
        for i in self.matrix:
            lst.append((i[0],i[1],self.matrix[i]))
        return Sparse_Matrix(self.rows,self.cols,*lst)
    
    def __neg__(self):
        lst=[]
        
        for i in self.matrix:
            lst.append((i[0],i[1],-self.matrix[i]))
        return Sparse_Matrix(self.rows,self.cols,*lst)
    
    def __abs__(self):
        lst=[]
        for i in self.matrix:
            lst.append((i[0],i[1],abs(self.matrix[i])))
        return Sparse_Matrix(self.rows,self.cols,*lst)
    
    
    def __add__(self,right):
        if type(right)!=Sparse_Matrix and type(right)!= int and type(right)!= float :
            raise TypeError
        lst=[]
        
        if type(right)==Sparse_Matrix:

            if self.size()!=right.size():
                
                raise AssertionError
            for i in self.matrix:
                lst.append((i[0],i[1],self.matrix[i]+right.matrix[i]))
            return Sparse_Matrix(self.rows,self.cols,*lst)
        else:
            for i in self.matrix:
                lst.append((i[0],i[1],self.matrix[i]+right))
            return Sparse_Matrix(self.rows,self.cols,*lst)
        
    def __radd__(self,left):
        return self.__add__(left)
    
    def __sub__(self,right):
        if type(right)!=Sparse_Matrix and type(right)!= int and type(right)!= float :
            raise TypeError
        lst=[]
        
        if type(right)==Sparse_Matrix:

            if self.size()!=right.size():
                
                raise AssertionError
            for i in self.matrix:
                lst.append((i[0],i[1],self.matrix[i]-right.matrix[i]))
            return Sparse_Matrix(self.rows,self.cols,*lst)
        else:
            for i in self.matrix:
                lst.append((i[0],i[1],self.matrix[i]-right))
            return Sparse_Matrix(self.rows,self.cols,*lst)
    
    def __rsub__(self,left):
        right=left
        if type(right)!=Sparse_Matrix and type(right)!= int and type(right)!= float :
            raise TypeError
        lst=[]
        
        if type(right)==Sparse_Matrix:

            if self.size()!=right.size():
                
                raise AssertionError
            for i in self.matrix:
                lst.append((i[0],i[1],right.matrix[i]-self.matrix[i]))
            return Sparse_Matrix(self.rows,self.cols,*lst)
        else:
            for i in self.matrix:
                lst.append((i[0],i[1],right-self.matrix[i]))
            return Sparse_Matrix(self.rows,self.cols,*lst)
        
    def __mul__(self,right):
        if type(right)!=Sparse_Matrix and type(right)!= int and type(right)!= float :
            raise TypeError
        lst=[]
        a=0
        if type(right)==Sparse_Matrix:
            if self.rows==right.cols and self.cols==right.rows:
                for i in range(self.rows):
                    for j in range(right.cols):
                        for q in range(len(self.row(i))):
                       
                            a+=self.row(i)[q]*right.col(j)[q]
                
                        lst.append((i,j,a))
                      
                        a=0
                return Sparse_Matrix(self.rows,right.cols,*lst)
            else:
                raise AssertionError
        else:
            for i in self.matrix:
                lst.append((i[0],i[1],right*self.matrix[i]))
            return Sparse_Matrix(self.rows,self.cols,*lst)
    def __rmul__(self,left):
        right=left
        if type(right)!=Sparse_Matrix and type(right)!= int and type(right)!= float :
            raise TypeError
        lst=[]
        a=0
        if type(right)==Sparse_Matrix:
            if self.rows==right.cols and self.cols==right.rows:
                for i in range(self.rows):
                    for j in range(right.cols):
                        for q in range(len(self.row(i))):                 
                            a+=self.row(i)[q]*right.col(j)[q]
                        lst.append((i,j,a))
                        a=0
                return Sparse_Matrix(self.rows,right.cols,*lst)
            else:
                raise AssertionError
        else:
            for i in self.matrix:
                lst.append((i[0],i[1],right*self.matrix[i]))
            return Sparse_Matrix(self.rows,self.cols,*lst)
        
    def __pow__(self,right):
        if type(right) != int:
            raise TypeError
        a=self
        if right<1:
            raise AssertionError
        if self.rows!=self.cols:
            raise AssertionError
        for i in range(right-1):
            self*=a
        return self
    
    def __eq__(self,right):
        
        if type(right)==Sparse_Matrix:
            if self.rows==right.rows and self.cols == right.cols and self.matrix==right.matrix:
                return True
            else:
                return False
        elif type(right)==int:
            s=0
            for i in self.matrix.values():
                if i==right:
                    s+=1
            if s==self.rows*self.cols:
                return True
            elif right==0 and sum(self.matrix.values())==0:
                return True
            else:
                return False
        else:
            return False
    
    
    def __setattr__(self,name,value):
        if name!='rows' and name!='cols' and name!='matrix':
            raise AssertionError
        if name in self.__dict__:
            raise AssertionError
        self.__dict__[name] = value 
    
        
         
        
                
                 
        
if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
    #Debugging problems with these tests is simpler
    
    print('Printing')
    m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
    print(m)
    print(repr(m))
    print(m.details())
  
    print('\nlen and size')
    print(len(m), m.size(),)
    
    print('\ngetitem and setitem')
    print(m[1,1])
    m[1,1] = 0
    m[0,1] = 2
    print(m.details())

    print('\niterator')
    for r,c,v in m:
        print((r,c),v)
    
    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m+m)
    print(m+1)
    print(m==m)
    print(m==1)
    print()   
    import driver
    driver.default_file_name = 'bscp22F20.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
