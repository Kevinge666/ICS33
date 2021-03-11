from collections import defaultdict    # You may use or ignore  
from math import sqrt


# Euclidean distance between two coordinates, each represented by a 2-tuple of int
def dist(c1 : (int,int), c2 : (int,int)) ->  float:    
    return sqrt( (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 )


# Rental cost in cents: 100 (flat fee) + 10*(duration in minutes) + (distance in feet)/1_000
def rental_fee(duration,distance) ->  int:    
    return 100 + 10*duration + distance//100



def scooter_revenues(db : {str: {(int,int,int,int) : (str,int,int,(int,int))}}) ->  {str:int}:    
    dic = {}
    for a in db:
        fee = []
        for b, c in db[a].items():
            fee.append(rental_fee(c[1], c[2]))

        dic[a] = sum(fee)
    return dic
 


def read_db(file : open) ->  {str: {(int,int,int,int) : (str,int,int,(int,int))}}:    
    db = {}
    db1 = {}
    s = ''
    for line in file:
        lst = line.replace('\n', '').split(':')
        if lst[0] != s:
            db1 = {}
            s = lst[0]
        list1 = lst[1].split(',')
        list5 = lst[5].split(',')
        list11 = []
        list55 = []
        for a in list1:
            list11.append(int(a))
        for b in list5:
            list55.append(int(b))
        list2 = [lst[2], int(lst[3]), int(lst[4]), tuple(list55)]
        db1[tuple(list11)] = tuple(list2)
        db[s] = db1
    return db



def rental_counts(db : {str: {(int,int,int,int) : (str,int,int,(int,int))}}, ref_date = None) ->  int:    
    lst1 = []
    lst2 = []
    num = 0
    if ref_date is not None:
        for key in ref_date:
            lst1.append(key)
        for m, n in db.items():
            for b in n:
                for stti in b:
                    lst2.append(stti)
                if lst1[0] == lst2[0] and lst1[1] == lst2[1] and lst1[2] == lst2[2]:
                    num += 1
                lst2 = []

    else:
        for m, n in db.items():
            for umm in n:
                num += 1

    return num




def sorted_by_renter_frequency(db : {str: {(int,int,int,int) : (str,int,int,(int,int))}}) ->  [(str,{(int,int,int):int})]:    
    pass 



def sorted_by_base_closeness(db : {str: {(int,int,int,int) : (str,int,int,(int,int))}}, ref_date : (int,int,int)) ->  {str: float}:    
    input_data = []
    result = {}
    final = []
    ref_date = list(ref_date)
    for a in ref_date:
        input_data.append(int(a))
    for key, value in db.items():  # key is sc1 value is dic
        lst3 = []
        max_lst3 = []
        if len(input_data) > 3:
            input_data.pop()
        for date, juli in value.items():
            lst1 = []
            for a in range(len(date) - 1):
                lst1.append(date[a])
            if lst1 == input_data:
                lst3.append(int(date[3]))
        if len(lst3) > 0:
            max_lst3.append(max(lst3))
            for h in max_lst3:
                input_data.append(h)
            tu = value[tuple(input_data)]
            one_dis = dist(tu[3], (0, 0))
            result[key] = one_dis
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    for i in result:
        final.append(i)
    return final



def renter_stats(db : {str: {(int,int,int,int) : (str,int,int,(int,int))}}) ->  (str,[int,int,int,float,{str}]):    
    pass 





if __name__ == '__main__':
    import prompt
     
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer   == correct):
            print ('    Correct')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
 
 
 
    if prompt.for_bool('Test scooter_revenues?', True):
        db1 =\
          {'sc1': {(2020,9,10,480) : ('Alan', 20,  5_000, (     0,  5_000)), 
                   (2020,9,10,720) : ('Beth', 40, 15_000, (15_000,  5_000)),
                   (2020,9,11,490) : ('Alan', 30,  7_000, (15_000,  7_000))
                  },
           'sc2': {(2020,9,10,810) : ('Beth', 40, 18_000, (10_000,20_000)),
                   (2020,9,10,930) : ('Beth', 38, 18_000, (    0,      0))
                  }
         
           }
        print('  argument =',db1)
        answer   = scooter_revenues(db1)
        print('  answer   =', answer)
        check(answer, {'sc1': 1470, 'sc2': 1340})
         
        db2 =\
          {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                   (2020, 9, 10, 510): ('Beth', 30, 12000, (-8000, -8000)),
                   (2020, 9, 12, 510): ('Deja', 5, 5000, (0, 4000))},
           'sc2': {(2020, 9, 11, 480): ('Beth', 25, 5000, (0, 6000)),
                   (2020, 9, 10, 550): ('Alan', 10, 2000, (2000, 3000)),
                   (2020, 9, 11, 700): ('Beth', 8, 2000, (0, 3000)),
                   (2020, 9, 11, 800): ('Carl', 18, 4000, (0, 3000)),
                   (2020, 9, 12, 800): ('Carl', 18, 2000, (0, 6000))},
           'sc3': {(2020, 9, 10, 600): ('Alan', 30, 10000, (-3000, 8000)),
                   (2020, 9, 10, 480): ('Deja', 18, 5000, (0, 4000)),
                   (2020, 9, 10, 900): ('Deja', 16, 1000, (0, 1000)),
                   (2020, 9, 10, 500): ('Eric', 5, 3000, (10000, 10000)),
                   (2020, 9, 11, 900): ('Eric', 8, 4000, (10000, 11000)),
                   (2020, 9, 15, 900): ('Eric', 7, 3000, (12000, 10000))},
           'sc4': {(2020, 9, 11, 900): ('Beth', 60, 36000, (2000, 4000)),
                   (2020, 9, 10, 650): ('Alan', 5, 1000, (-2000, 8000))},
           'sc5': {(2020, 9, 10, 860): ('Alan', 20, 4000, (0, 6000)),
                   (2020, 9, 15, 1200): ('Fran', 90, 100000, (-40000, -40000))}}
        print('  argument =',db2)
        answer   = scooter_revenues(db2)
        print('  answer   =', answer)
        check(answer, {'sc1': 1070, 'sc2': 1440, 'sc3': 1700, 'sc4': 1220, 'sc5': 2340})
         
 
 
    if prompt.for_bool('Test read_db?', True):
        print('  argument = rental1.txt')
        answer   = read_db(open('rental1.txt'))
        print('  answer   =', answer)
        check(answer, {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                               (2020, 9, 10, 720): ('Beth', 40, 15000, (15000, 5000)),
                               (2020, 9, 11, 490): ('Alan', 30, 7000, (15000, 7000))},
                       'sc2': {(2020, 9, 10, 810): ('Beth', 40, 18000, (10000, 20000)),
                               (2020, 9, 10, 930): ('Beth', 38, 18000, (0, 0))}})
 
        print('  argument = rental2.txt')
        answer   = read_db(open('rental2.txt'))
        print('  answer   =', answer)
        check(answer, {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                               (2020, 9, 10, 510): ('Beth', 30, 12000, (-8000, -8000)),
                               (2020, 9, 12, 510): ('Deja', 5, 5000, (0, 4000))},
                       'sc2': {(2020, 9, 11, 480): ('Beth', 25, 5000, (0, 6000)),
                               (2020, 9, 10, 550): ('Alan', 10, 2000, (2000, 3000)),
                               (2020, 9, 11, 700): ('Beth', 8, 2000, (0, 3000)),
                               (2020, 9, 11, 800): ('Carl', 18, 4000, (0, 3000)),
                               (2020, 9, 12, 800): ('Carl', 18, 2000, (0, 6000))},
                       'sc3': {(2020, 9, 10, 600): ('Alan', 30, 10000, (-3000, 8000)),
                               (2020, 9, 10, 480): ('Deja', 18, 5000, (0, 4000)),
                               (2020, 9, 10, 900): ('Deja', 16, 1000, (0, 1000)),
                               (2020, 9, 10, 500): ('Eric', 5, 3000, (10000, 10000)),
                               (2020, 9, 11, 900): ('Eric', 8, 4000, (10000, 11000)),
                               (2020, 9, 15, 900): ('Eric', 7, 3000, (12000, 10000))},
                       'sc4': {(2020, 9, 11, 900): ('Beth', 60, 36000, (2000, 4000)),
                               (2020, 9, 10, 650): ('Alan', 5, 1000, (-2000, 8000))},
                       'sc5': {(2020, 9, 10, 860): ('Alan', 20, 4000, (0, 6000)),
                               (2020, 9, 15, 1200): ('Fran', 90, 100000, (-40000, -40000))}})
 
 
 
    if prompt.for_bool('Test rental_counts?', True):
        db1 =\
          {'sc1': {(2020,9,10,480) : ('Alan', 20,  5_000, (     0,  5_000)), 
                   (2020,9,10,720) : ('Beth', 40, 15_000, (15_000,  5_000)),
                   (2020,9,11,490) : ('Alan', 30,  7_000, (15_000,  7_000))
                  },
           'sc2': {(2020,9,10,810) : ('Beth', 40, 18_000, (10_000,20_000)),
                   (2020,9,10,930) : ('Beth', 38, 18_000, (    0,      0))
                  }
         
           }
        print('  argument =',db1)
        answer   = rental_counts(db1)
        print('  rental_counts(db1) answer   =', answer)
        check(answer, 5)
        answer   = rental_counts(db1,(2020,9,10))
        print('  rental_counts(db1,(2020,9,10) answer   =', answer)
        check(answer, 4)
        answer   = rental_counts(db1,(2020,9,11))
        print('  rental_counts(db1,(2020,9,11) answer   =', answer)
        check(answer, 1)
        answer   = rental_counts(db1,(2020,9,12))
        print('  rental_counts(db1,(2020,9,12) answer   =', answer)
        check(answer, 0)
 
        db2 =\
          {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                   (2020, 9, 10, 510): ('Beth', 30, 12000, (-8000, -8000)),
                   (2020, 9, 12, 510): ('Deja', 5, 5000, (0, 4000))},
           'sc2': {(2020, 9, 11, 480): ('Beth', 25, 5000, (0, 6000)),
                   (2020, 9, 10, 550): ('Alan', 10, 2000, (2000, 3000)),
                   (2020, 9, 11, 700): ('Beth', 8, 2000, (0, 3000)),
                   (2020, 9, 11, 800): ('Carl', 18, 4000, (0, 3000)),
                   (2020, 9, 12, 800): ('Carl', 18, 2000, (0, 6000))},
           'sc3': {(2020, 9, 10, 600): ('Alan', 30, 10000, (-3000, 8000)),
                   (2020, 9, 10, 480): ('Deja', 18, 5000, (0, 4000)),
                   (2020, 9, 10, 900): ('Deja', 16, 1000, (0, 1000)),
                   (2020, 9, 10, 500): ('Eric', 5, 3000, (10000, 10000)),
                   (2020, 9, 11, 900): ('Eric', 8, 4000, (10000, 11000)),
                   (2020, 9, 15, 900): ('Eric', 7, 3000, (12000, 10000))},
           'sc4': {(2020, 9, 11, 900): ('Beth', 60, 36000, (2000, 4000)),
                   (2020, 9, 10, 650): ('Alan', 5, 1000, (-2000, 8000))},
           'sc5': {(2020, 9, 10, 860): ('Alan', 20, 4000, (0, 6000)),
                   (2020, 9, 15, 1200): ('Fran', 90, 100000, (-40000, -40000))}}
        print('  argument =',db2)
        answer   = rental_counts(db2)
        print('  rental_counts(db2) answer   =', answer)
        check(answer, 18)
        answer   = rental_counts(db2,(2020,9,10))
        print('  rental_counts(db2,(2020,9,10) answer   =', answer)
        check(answer, 9)
        answer   = rental_counts(db2,(2020,9,11))
        print('  rental_counts(db2,(2020,9,11) answer   =', answer)
        check(answer, 5)
        answer   = rental_counts(db2,(2020,9,12))
        print('  rental_counts(db2,(2020,9,12) answer   =', answer)
        check(answer, 2)
        answer   = rental_counts(db2,(2020,9,13))
        print('  rental_counts(db2,(2020,9,13) answer   =', answer)
        check(answer, 0)
        answer   = rental_counts(db2,(2020,9,15))
        print('  rental_counts(db2,(2020,9,15) answer   =', answer)
        check(answer, 2)
 
 
 
    if prompt.for_bool('Test sorted_by_renter_frequency?', True):
        db1 =\
          {'sc1': {(2020,9,10,480) : ('Alan', 20,  5_000, (     0,  5_000)), 
                   (2020,9,10,720) : ('Beth', 40, 15_000, (15_000,  5_000)),
                   (2020,9,11,490) : ('Alan', 30,  7_000, (15_000,  7_000))
                  },
           'sc2': {(2020,9,10,810) : ('Beth', 40, 18_000, (10_000,20_000)),
                   (2020,9,10,930) : ('Beth', 38, 18_000, (    0,      0))
                  }
         
           }
        print('  argument =',db1)
        answer   = sorted_by_renter_frequency(db1)
        print('  answer   =', answer)
        check(answer, [('Alan', {(2020, 9, 10): 1, (2020, 9, 11): 1}), ('Beth', {(2020, 9, 10): 3})] )
 
        db2 =\
          {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                   (2020, 9, 10, 510): ('Beth', 30, 12000, (-8000, -8000)),
                   (2020, 9, 12, 510): ('Deja', 5, 5000, (0, 4000))},
           'sc2': {(2020, 9, 11, 480): ('Beth', 25, 5000, (0, 6000)),
                   (2020, 9, 10, 550): ('Alan', 10, 2000, (2000, 3000)),
                   (2020, 9, 11, 700): ('Beth', 8, 2000, (0, 3000)),
                   (2020, 9, 11, 800): ('Carl', 18, 4000, (0, 3000)),
                   (2020, 9, 12, 800): ('Carl', 18, 2000, (0, 6000))},
           'sc3': {(2020, 9, 10, 600): ('Alan', 30, 10000, (-3000, 8000)),
                   (2020, 9, 10, 480): ('Deja', 18, 5000, (0, 4000)),
                   (2020, 9, 10, 900): ('Deja', 16, 1000, (0, 1000)),
                   (2020, 9, 10, 500): ('Eric', 5, 3000, (10000, 10000)),
                   (2020, 9, 11, 900): ('Eric', 8, 4000, (10000, 11000)),
                   (2020, 9, 15, 900): ('Eric', 7, 3000, (12000, 10000))},
           'sc4': {(2020, 9, 11, 900): ('Beth', 60, 36000, (2000, 4000)),
                   (2020, 9, 10, 650): ('Alan', 5, 1000, (-2000, 8000))},
           'sc5': {(2020, 9, 10, 860): ('Alan', 20, 4000, (0, 6000)),
                   (2020, 9, 15, 1200): ('Fran', 90, 100000, (-40000, -40000))}}
        print('  argument =',db2)
        answer   = sorted_by_renter_frequency(db2)
        print('  answer   =', answer)
        check(answer, [('Fran', {(2020, 9, 15): 1}),
                       ('Carl', {(2020, 9, 11): 1, (2020, 9, 12): 1}),
                       ('Deja', {(2020, 9, 12): 1, (2020, 9, 10): 2}),
                       ('Eric', {(2020, 9, 10): 1, (2020, 9, 11): 1, (2020, 9, 15): 1}),
                       ('Beth', {(2020, 9, 10): 1, (2020, 9, 11): 3}),
                       ('Alan', {(2020, 9, 10): 5})] )
  
 
 
    if prompt.for_bool('Test sorted_by_base_closeness?', True):
        db1 =\
          {'sc1': {(2020,9,10,480) : ('Alan', 20,  5_000, (     0,  5_000)), 
                   (2020,9,10,720) : ('Beth', 40, 15_000, (15_000,  5_000)),
                   (2020,9,11,490) : ('Alan', 30,  7_000, (15_000,  7_000))
                  },
           'sc2': {(2020,9,10,810) : ('Beth', 40, 18_000, (10_000,20_000)),
                   (2020,9,10,930) : ('Beth', 38, 18_000, (    0,      0))
                  }
         
           }
        print('  argument =',db1)
        answer   = sorted_by_base_closeness(db1,(2020,9,10))
        print('  sorted_by_base_closeness(db1,(2020,9,10) answer   =', answer)
        check(answer, ['sc1', 'sc2'])
        answer   = sorted_by_base_closeness(db1,(2020,9,11))
        print('  sorted_by_base_closeness(db1,(2020,9,11) answer   =', answer)
        check(answer, ['sc1'])
        answer   = sorted_by_base_closeness(db1,(2020,9,12))
        print('  orted_by_base_closeness(db1,(2020,9,12) answer   =', answer)
        check(answer, [])
 
        db2 =\
          {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                   (2020, 9, 10, 510): ('Beth', 30, 12000, (-8000, -8000)),
                   (2020, 9, 12, 510): ('Deja', 5, 5000, (0, 4000))},
           'sc2': {(2020, 9, 11, 480): ('Beth', 25, 5000, (0, 6000)),
                   (2020, 9, 10, 550): ('Alan', 10, 2000, (2000, 3000)),
                   (2020, 9, 11, 700): ('Beth', 8, 2000, (0, 3000)),
                   (2020, 9, 11, 800): ('Carl', 18, 4000, (0, 3000)),
                   (2020, 9, 12, 800): ('Carl', 18, 2000, (0, 6000))},
           'sc3': {(2020, 9, 10, 600): ('Alan', 30, 10000, (-3000, 8000)),
                   (2020, 9, 10, 480): ('Deja', 18, 5000, (0, 4000)),
                   (2020, 9, 10, 900): ('Deja', 16, 1000, (0, 1000)),
                   (2020, 9, 10, 500): ('Eric', 5, 3000, (10000, 10000)),
                   (2020, 9, 11, 900): ('Eric', 8, 4000, (10000, 11000)),
                   (2020, 9, 15, 900): ('Eric', 7, 3000, (12000, 10000))},
           'sc4': {(2020, 9, 11, 900): ('Beth', 60, 36000, (2000, 4000)),
                   (2020, 9, 10, 650): ('Alan', 5, 1000, (-2000, 8000))},
           'sc5': {(2020, 9, 10, 860): ('Alan', 20, 4000, (0, 6000)),
                   (2020, 9, 15, 1200): ('Fran', 90, 100000, (-40000, -40000))}}
        print('  argument =',db2)
        answer   = sorted_by_base_closeness(db2,(2020,9,10))
        print('  sorted_by_base_closeness(db2,(2020,9,10) answer   =', answer)
        check(answer, ['sc1', 'sc4', 'sc5', 'sc2', 'sc3'])
        answer   = sorted_by_base_closeness(db2,(2020,9,11))
        print('  sorted_by_base_closeness(db2,(2020,9,11) answer   =', answer)
        check(answer, ['sc3', 'sc4', 'sc2'])
        answer   = sorted_by_base_closeness(db2,(2020,9,12))
        print('  sorted_by_base_closeness(db2,(2020,9,12) answer   =', answer)
        check(answer, ['sc2', 'sc1'])
        answer   = sorted_by_base_closeness(db2,(2020,9,13))
        print('  sorted_by_base_closeness(db2,(2020,9,13) answer   =', answer)
        check(answer, [])
        answer   = sorted_by_base_closeness(db2,(2020,9,15))
        print('  sorted_by_base_closeness(db2,(2020,9,15) answer   =', answer)
        check(answer, ['sc5', 'sc3'])



    if prompt.for_bool('renter_stats: worth only 1 point extra credit?', True):
        db1 =\
          {'sc1': {(2020,9,10,480) : ('Alan', 20,  5_000, (     0,  5_000)), 
                   (2020,9,10,720) : ('Beth', 40, 15_000, (15_000,  5_000)),
                   (2020,9,11,490) : ('Alan', 30,  7_000, (15_000,  7_000))
                  },
           'sc2': {(2020,9,10,810) : ('Beth', 40, 18_000, (10_000,20_000)),
                   (2020,9,10,930) : ('Beth', 38, 18_000, (    0,      0))
                  }
         
           }
        print('  argument =',db1)
        answer   = renter_stats(db1)
        print('  answer   =', answer)
        check(answer, [('Beth', [3, 118, 51000, 1990, 22360.679774997898, {'sc2', 'sc1'}]), 
                       ('Alan', [2, 50, 12000, 820, 16552.94535724685, {'sc1'}])])
 
        db2 =\
          {'sc1': {(2020, 9, 10, 480): ('Alan', 20, 5000, (0, 5000)),
                   (2020, 9, 10, 510): ('Beth', 30, 12000, (-8000, -8000)),
                   (2020, 9, 12, 510): ('Deja', 5, 5000, (0, 4000))},
           'sc2': {(2020, 9, 11, 480): ('Beth', 25, 5000, (0, 6000)),
                   (2020, 9, 10, 550): ('Alan', 10, 2000, (2000, 3000)),
                   (2020, 9, 11, 700): ('Beth', 8, 2000, (0, 3000)),
                   (2020, 9, 11, 800): ('Carl', 18, 4000, (0, 3000)),
                   (2020, 9, 12, 800): ('Carl', 18, 2000, (0, 6000))},
           'sc3': {(2020, 9, 10, 600): ('Alan', 30, 10000, (-3000, 8000)),
                   (2020, 9, 10, 480): ('Deja', 18, 5000, (0, 4000)),
                   (2020, 9, 10, 900): ('Deja', 16, 1000, (0, 1000)),
                   (2020, 9, 10, 500): ('Eric', 5, 3000, (10000, 10000)),
                   (2020, 9, 11, 900): ('Eric', 8, 4000, (10000, 11000)),
                   (2020, 9, 15, 900): ('Eric', 7, 3000, (12000, 10000))},
           'sc4': {(2020, 9, 11, 900): ('Beth', 60, 36000, (2000, 4000)),
                   (2020, 9, 10, 650): ('Alan', 5, 1000, (-2000, 8000))},
           'sc5': {(2020, 9, 10, 860): ('Alan', 20, 4000, (0, 6000)),
                   (2020, 9, 15, 1200): ('Fran', 90, 100000, (-40000, -40000))}}
        print('  argument =',db2)
        answer   = renter_stats(db2)
        print('  answer   =', answer)
        check(answer, [('Alan', [5, 85, 22000, 1570, 8544.003745317532, {'sc1', 'sc3', 'sc4', 'sc5', 'sc2'}]),
                       ('Beth', [4, 123, 55000, 2180, 11313.70849898476, {'sc4', 'sc1', 'sc2'}]),
                       ('Deja', [3, 39, 11000, 800, 4000.0, {'sc1', 'sc3'}]),
                       ('Eric', [3, 20, 10000, 600, 15620.499351813309, {'sc3'}]),
                       ('Carl', [2, 36, 6000, 620, 6000.0, {'sc2'}]),
                       ('Fran', [1, 90, 100000, 2000, 56568.5424949238, {'sc5'}])])
