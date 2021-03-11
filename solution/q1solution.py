from collections import defaultdict  # Use or ignore

def function_cycler(*fs : callable) -> callable:
    if len(fs) == 0:
        raise TypeError('q1solutionf20.function_cycler: no functions passed')
#     i = 0
#     def one_f(x : object) -> object:
#         nonlocal i
#         answer = fs[i](x)
#         i = (i+1) % len(fs)
#         one_f.times_called += 1
#         return answer
    fs = list(fs)
    def one_f(x : object) -> object:
        answer = fs[0](x)
        fs.append(fs.pop(0))
        one_f.times_called += 1
        return answer
    one_f.times_called = 0            
    return one_f



def jobs(db1 : {str:{str:int}}, min_skill_level : int) -> {str}:
    return {job for job_skills in db1.values() for job,skill_level in job_skills.items() 
              if skill_level >= min_skill_level}



def rank(db1 : {str:{str:int}}) -> [str]:
    return sorted(db1.keys(), key = lambda name : (-sum(db1[name].values())/len(db1[name]),name))



def popular(db1 : {str:{str:int}}) -> [str]:
    return sorted(jobs(db1,0), 
                    key = lambda job_name : (-sum(int(job_name in job_skills) for job_skills in db1.values()),job_name))
#                     key = lambda job_name : (-sum(1 for job_skills in db1.values() if job_name in job_skills),job_name))



def who(db1 : {str:{(str,int)}}, job: str, min_skill_level : int) -> [(str,int)]:
    return sorted ([(name,skill_level)
                       for name,job_skills in db1.items() for job_name,skill_level in job_skills.items() 
                         if job_name==job and skill_level>=min_skill_level],
                   key = lambda t : (-t[1],t[0]))



def by_job(db1 : {str:{str:int}}) -> {str:{str:int}}:
    answer = defaultdict(dict)
    for name,job_rankings in db1.items():
        for job,ranking in job_rankings.items():
            answer[job][name] = ranking
    return dict(answer.items())



def by_skill(db1 : {str:{str:int}}) -> [int,[str,[str]]]:
    answer = defaultdict(lambda : defaultdict(list))
    for name,job_rankings in db1.items():
        for job,ranking in job_rankings.items():
            answer[ranking][job].append(name)
    for ranking,data in answer.items():
        answer[ranking] = [(job,sorted(people)) for job,people in sorted(data.items())]
    return sorted(answer.items(), reverse = True)





if __name__ == '__main__':
    from goody import irange
    
    print('\nTesting function_cycler')
    try:
        cycler0 = function_cycler()
        print("Incorrect: Did not raise required exception for no-argument function call")
    except TypeError:
        print("Correct: rasised required exception for no-argument function call")
    cycler1 = function_cycler( (lambda x : x), (lambda x : x**2))
    print('Cycler 1:',[cycler1(x) for x in irange(1,10)],'... times called: ',cycler1.times_called)
    cycler2 = function_cycler( (lambda x : x+1), (lambda x : 2*x), (lambda x : x**2))
    print('Cycler 2:',[cycler2(x) for x in irange(1,10)],'... times called: ',cycler2.times_called)
 
    print('Cycler 1 again:',[cycler1(x) for x in irange(10,15)],'... times called: ',cycler1.times_called)
    print('Cycler 2 again:',[cycler2(x) for x in irange(10,20)],'... times called: ',cycler2.times_called)
    
    
    # Note: the keys in this dicts are not specified in alphabetical order
    db1 = {
          'Diane':   {'Laundry': 2,   'Cleaning': 4, 'Gardening': 3},
          'Betty':   {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3},
          'Charles': {'Plumbing': 2,  'Cleaning': 5},
          'Adam':    {'Cleaning': 4,  'Tutoring': 2, 'Baking': 1}
          }

    db2 = {
           'Adam': {'Laundry': 2, 'Driving': 2, 'Tutoring': 2, 'Reading': 1, 'Gardening': 1},
           'Emil': {'Errands': 4, 'Driving': 1, 'Baking': 3},
           'Chad': {'Repairing': 2, 'Reading': 2, 'Errands': 4, 'Baking': 2},
           'Ivan': {'Gardening': 5, 'Errands': 5, 'Reading': 4, 'Cleaning': 3},
           'Gene': {'Driving': 1, 'Laundry': 1, 'Baking': 2, 'Gardening': 2, 'Repairing': 2, 'Errands': 5},
           'Dana': {'Driving': 2}, 
           'Hope': {'Driving': 5, 'Reading': 3, 'Errands': 2, 'Shopping': 2, 'Gardening': 1, 'Laundry': 2},
           'Bree': {'Baking': 2, 'Errands': 5},
           'Faye': {'Tutoring': 2, 'Reading': 5, 'Repairing': 5, 'Baking': 4}
           }

    print('\nTesting jobs')
    print('jobs(db1,0):',jobs(db1,0))
    print('jobs(db1,3):',jobs(db1,3))
    print('jobs(db2,0):',jobs(db2,0))
    print('jobs(db2,5):',jobs(db2,5))


    print('\nTesting rank')
    print ('rank(db1):',rank(db1))
    print ('rank(db2):',rank(db2))


    print('\nTesting popular')
    print ('popular(db1):',popular(db1))
    print ('popular(db2):',popular(db2))


    print('\nTesting who')
    print("who(db1,'Cleaning',4):", who(db1,'Cleaning',4))
    print("who(db1,'Gardening',0):", who(db1,'Gardening',0))
    print("who(db1,'Tutoring',3):", who(db1,'Tutoring',3))
    print("who(db1,'Gambling',0):", who(db1,'Gambling',0))
    print("who(db2,'Baking',0):", who(db2,'Baking',0))
    print("who(db2,'Cleaning',1):", who(db2,'Cleaning',1))
    print("who(db2,'Driving',2):", who(db2,'Driving',2))
    print("who(db2,'Errands',3):", who(db2,'Errands',3))
    print("who(db2,'Gardening',4):", who(db2,'Gardening',4))
    print("who(db2,'Laundry',5):", who(db2,'Laundry',5))

    print('\nTesting by_job')
    print ('by_job(db1):',by_job(db1))
    print ('by_job(db2):',by_job(db2))


    print('\nTesting by_skill')
    print ('by_skill(db1):',by_skill(db1))
    print ('by_skill(db2):',by_skill(db2))



    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = 'bscq1F20.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
