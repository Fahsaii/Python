from random import randint

def genData(std, sub):
    scores = []
    for r in range(student):
        scores.append([])
        for c in range(subject):
            scores[r].append( randint(0,100))
    return scores
def displayData(scores):
    n = 1
    for score in scores:
        print(f'|Std %2d '%n,end='')
        for s in score:
            print(f'| %3s '%s,end='')
        print('|',end='')
        print( sum(score)/subject,end='')
        print('|',end='')
        print( max(score),end='')
        print('|')
        n = n + 1
        

student = int(input('Enter number of student : '))
subject = int(input('Enter number of subject : '))

Score = genData(student, subject)

displayData(Score)