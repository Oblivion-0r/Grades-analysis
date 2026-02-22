great = 0
good = 0
ok = 0
bad = 0
grades = open("grades.txt", "r")
max_grade = 0
min_grade = 5
for line in grades:
    grades = line.split()
    grades = int(line.strip())
    if grades > max_grade:
        max_grade = grades
    if grades < min_grade:
        min_grade = grades

    if grades == 5:
        great += 1
    elif grades == 4:
        good += 1
    elif grades == 3:
        ok += 1
    elif grades == 2:
        bad += 1
print('Average grade:', (5*great + 4*good + 3*ok + 2*bad) / (great + good + ok + bad))
print('Maximum grade:', max_grade)
print('Minimum grade:', min_grade)
print(bad, "bad grades")


