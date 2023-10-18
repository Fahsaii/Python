from random import randint

def random_score(scores):
    for n in range(1, 11):
        scores[n] = randint(0, 100)

def check_grade(scores, grades):
    grades_range = {80:"A", 70:"B", 60:"C", 50:"D", 0:"F"}
    for n, score in scores.items():
        for key, value in grades_range.items():
            if(score >= key):
                grades[n] = value
                break

def report_grade(scores, grades):
    print("="*23)
    print("| No. | Scores | Grade |")
    print("="*23)
    for n in scores:
       print(f"| {n:3d} |  {scores[n]:3d}   |    {grades[n]:3s}|")
    print("="*23)

scores = {}
grades = {}
random_score(scores)
check_grade(scores, grades)
report_grade(scores,  grades)