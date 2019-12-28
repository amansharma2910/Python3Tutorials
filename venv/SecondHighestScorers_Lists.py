## Input the names and grades for each student in a Physics class of  students, store them in a multi-dimentional list and print the name(s) of any student(s) having the second lowest grade.
from operator import itemgetter, attrgetter

N = int(input("Enter the number of students: "))
low = 0
sec_low = 0
multiDemList = [[0] * 2 for i in range(N)]

for i in range(N):
    for j in range(2):
        multiDemList[i][j] = input()
    multiDemList[i][1] = float(multiDemList[i][1])

multiDemList.sort(key=itemgetter(1))
low = multiDemList[0][1]
for i in range(N):
    if multiDemList[i][1] > low:
        sec_low = multiDemList[i][1]
        break

sec_low_list = []

for i in range(N):
    if multiDemList[i][1] == sec_low:
        sec_low_list.append(multiDemList[i][0])

sec_low_list.sort()
print("The student(s) with second highest score:")
for i in sec_low_list:
    print("",i)
