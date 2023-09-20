def Check_Grade(grade):
    Grades = ('A','B+','B','C+','C','D+','D','F')
    Values = (4,3.5,3,2.5,2,1.5,1,0)
    for n in range(len(Grades)):
        if grade == Grades[n]:
            return(Values[n])

done = True
while done:
    grade = input('Enter grade (Q-EXIT): ')
    grade = grade.upper()
    if grade == 'Q':
        break
    else:
        value = Check_Grade(grade)
        print(f'Score value of {grade} is {value}')
print('End Program')