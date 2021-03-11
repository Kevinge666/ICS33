file = open('db1.txt', 'r')

blst = []
dic = {}
di = {}
lst = []
for line in file:
    list1 = line.replace('\n', '').split(':')
    lst.append(list1)
print(lst)
for i in range(len(lst)):
    while i+1 <= len(lst):

'''
    di = dict(sorted(di.items(),key=lambda x: x))
    dic[num] = di
    dic = dict(sorted(dic.items(),key=lambda x: x))
print(dic)

'''

