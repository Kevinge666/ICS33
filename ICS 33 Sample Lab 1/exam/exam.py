from collections import defaultdict # You can use this or just use regular dict

# You might use these abbreviations in your code
# z  : zipcode
# p  : party
# v  : voter
# s  : state


def party_summary(db : {int:{str:int}}) -> {str:int}:
    lst = []
    dic = {} # key should be parties, values are the total votes
    for keys in db: #keys are the zip code.
        for party in db[keys]:
            lst = []
            for a in db:
                for b in db[a]:
                    if party == b:
                        lst.append(db[a][b])
            dic[party] = sum(lst)
    return dic


def read_db(file : open) -> {int:{str:int}}:
    blst = []
    dic = {}
    di = {}
    for line in file:
        list1 = line.replace('\n','').split(':')
        num = list1[0]
        blst.append(list1)
        print(blst)
        for i in range(len(blst)):
            if num == blst[i][0]:
                list1.pop(0)
                for a in list1:
                    blst[i].append(a)
            else:
                blst.append(list1)
        print(blst)
        di = dict(sorted(di.items(),key=lambda x: x))
        dic[num] = di
        dic = dict(sorted(dic.items(),key=lambda x: x))
    return dic



def registered_ordering(db : {int:{str:int}}, p : str) -> [int]:
    pass


def state_summary(db : {int:{str:int}}, state_zips : {str:{int}}) -> {str:{str:int}}:
    pass
    

def predicted_winners(db : {int:{str:int}}) -> {str:{int}}:
    pass



def biggest_gap(db : {int:{str:int}}) -> (int,int):
    pass




 
if __name__ == '__main__':
    import prompt
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer   == correct):
            print ('    CORRECT')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
  
  
    if prompt.for_bool('Test party_summary?', True):  
        db1 = {1: {'d': 10, 'i': 15,          'r': 15},
               2: {'d': 12,                   'r':  8},
               3: {'d': 10, 'i': 30, 'l': 20, 'r': 22},
               4: {'d': 30,          'l': 20, 'r': 30},
               5: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db1)
        answer = party_summary(db1)
        print('  answer   =', answer)
        check(answer, {'d': 62, 'i': 60, 'r': 90, 'l': 55})
 
        db2 = {1000: {'d': 50, 'i': 27,          'r': 18, 'x': 46},
               2000: {'d': 32,                   'r': 58},
               3000: {'d': 20, 'i': 30, 'l': 20, 'r': 22},
               4000: {'d': 40, 'i': 20, 'l': 40, 'r': 39, 'x': 46},
               5000: {'d': 20, 'i': 30, 'l': 20,          'x': 15},
               6000: {         'i': 30,                   'x': 46},
               7000: {                  'l': 20,                 },
               8000: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db2)
        answer = party_summary(db2)
        print('  answer   =', answer)
        check(answer, {'d': 162, 'i': 152, 'r': 152, 'x': 153, 'l': 115})
 
 
    if prompt.for_bool('Test read_db?', True):  
        db1 = {1: {'d': 10, 'i': 15,          'r': 15},
               2: {'d': 12,                   'r':  8},
               3: {'d': 10, 'i': 30, 'l': 20, 'r': 22},
               4: {'d': 30,          'l': 20, 'r': 30},
               5: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument = db1.txt')
        answer = read_db(open('db1.txt'))
        print('  answer   =', answer)
        check(answer, db1)
 
        db2 = {1000: {'d': 50, 'i': 27,          'r': 18, 'x': 46},
               2000: {'d': 32,                   'r': 58},
               3000: {'d': 20, 'i': 30, 'l': 20, 'r': 22},
               4000: {'d': 40, 'i': 20, 'l': 40, 'r': 39, 'x': 46},
               5000: {'d': 20, 'i': 30, 'l': 20,          'x': 15},
               6000: {         'i': 30,                   'x': 46},
               7000: {                  'l': 20,                 },
               8000: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument = db2.txt')
        answer = read_db(open('db2.txt'))
        print('  answer   =', answer)
        check(answer, db2)
 
 
     
    if prompt.for_bool('Test registered_ordering?', True):  
        db1 = {1: {'d': 10, 'i': 15,          'r': 15},
               2: {'d': 12,                   'r':  8},
               3: {'d': 10, 'i': 30, 'l': 20, 'r': 22},
               4: {'d': 30,          'l': 20, 'r': 30},
               5: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db1)
        answer = registered_ordering(db1,'r')
        print('  answer   =', answer)
        check(answer, [4, 3, 1, 5, 2])
 
        db2 = {1000: {'d': 50, 'i': 27,          'r': 18, 'x': 46},
               2000: {'d': 32,                   'r': 58},
               3000: {'d': 20, 'i': 30, 'l': 20, 'r': 22},
               4000: {'d': 40, 'i': 20, 'l': 40, 'r': 39, 'x': 46},
               5000: {'d': 20, 'i': 30, 'l': 20,          'x': 15},
               6000: {         'i': 30,                   'x': 46},
               7000: {                  'l': 20,                 },
               8000: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db2)
        answer = registered_ordering(db2,'i')
        print('  answer   =', answer)
        check(answer, [3000, 5000, 6000, 1000, 4000, 8000])
 
 
  
    if prompt.for_bool('Test state_summary?', True):  
        state_zips1 = {'CA' : {1,3}, 'WA': {2,4,5}}
        db1 = {1: {'d': 10, 'i': 15,          'r': 15},
               2: {'d': 12,                   'r':  8},
               3: {'d': 10, 'i': 30, 'l': 20, 'r': 22},
               4: {'d': 30,          'l': 20, 'r': 30},
               5: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db1)
        answer = state_summary(db1, state_zips1)
        print('  answer   =', answer)
        check(answer,  {'CA':  {'d': 20, 'i': 45, 'r': 37, 'l': 20}, 'WA':  {'d': 42, 'r': 53, 'l': 35, 'i': 15}})
 
        state_zips2 = {'CA' : {1000,3000,7000}, 'WA': {2000,4000,5000,8000}, 'OR' : {6000}, 'NV' : {}}
        db2 = {1000: {'d': 50, 'i': 27,          'r': 18, 'x': 46},
               2000: {'d': 32,                   'r': 58},
               3000: {'d': 20, 'i': 30, 'l': 20, 'r': 22},
               4000: {'d': 40, 'i': 20, 'l': 40, 'r': 39, 'x': 46},
               5000: {'d': 20, 'i': 30, 'l': 20,          'x': 15},
               6000: {         'i': 30,                   'x': 46},
               7000: {                  'l': 20,                 },
               8000: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db2)
        answer = state_summary(db2, state_zips2)
        print('  answer   =', answer)
        check(answer,  {'CA': {'d': 70, 'i': 57, 'r': 40, 'x': 46, 'l': 40}, 'WA':  {'d': 92, 'r': 112, 'i': 65, 'l': 75, 'x': 61}, 'OR': {'i': 30, 'x': 46}})
 
 
 
    if prompt.for_bool('Test predicted_winners?', True):  
        db1 = {1: {'d': 10, 'i': 15,          'r': 15},
               2: {'d': 12,                   'r':  8},
               3: {'d': 10, 'i': 30, 'l': 20, 'r': 22},
               4: {'d': 30,          'l': 20, 'r': 30},
               5: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db1)
        answer = predicted_winners(db1)
        print('  answer   =', answer)
        check(answer, {'tie': {1, 4, 5}, 'd': {2}, 'i': {3}})
 
        db2 = {1000: {'d': 50, 'i': 27,          'r': 18, 'x': 46},
               2000: {'d': 32,                   'r': 58},
               3000: {'d': 20, 'i': 30, 'l': 20, 'r': 22},
               4000: {'d': 40, 'i': 20, 'l': 40, 'r': 39, 'x': 46},
               5000: {'d': 20, 'i': 30, 'l': 20,          'x': 15},
               6000: {         'i': 30,                   'x': 46},
               7000: {                  'l': 20,                 },
               8000: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db2)
        answer = predicted_winners(db2)
        print('  answer   =', answer)
        check(answer, {'d': {1000}, 'r': {2000}, 'i': {3000, 5000}, 'x': {4000, 6000}, 'l': {7000}, 'tie': {8000}})
 
     
   
    if prompt.for_bool('Test biggest_gap?', True):  
        db1 = {1: {'d': 10, 'i': 15,          'r': 15},
               2: {'d': 12,                   'r':  8},
               3: {'d': 10, 'i': 30, 'l': 20, 'r': 22},
               4: {'d': 30,          'l': 20, 'r': 30},
               5: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db1)
        answer = biggest_gap(db1)
        print('  answer   =', answer)
        check(answer, (2, 3))
 
        db2 = {1000: {'d': 50, 'i': 27,          'r': 18, 'x': 46},
               2000: {'d': 32,                   'r': 58},
               3000: {'d': 20, 'i': 30, 'l': 20, 'r': 22},
               4000: {'d': 40, 'i': 20, 'l': 40, 'r': 39, 'x': 46},
               5000: {'d': 20, 'i': 30, 'l': 20,          'x': 15},
               6000: {         'i': 30,                   'x': 46},
               7000: {                  'l': 20,                 },
               8000: {         'i': 15, 'l': 15, 'r': 15}}
        print('  argument =', db2)
        answer = biggest_gap(db2)
        print('  answer   =', answer)
        check(answer, (4000, 5000))
