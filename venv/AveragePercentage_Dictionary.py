def avgPercent(list1):
    sum=0
    noError = True
    for i in list1:
        if i>=0 and i<=100:
            sum+=i
        else:
            noError = False
            break
    if noError == True:
        print("{:.02f}".format(sum/3))

if __name__ == '__main__':
    n = int(input())
    if n>=2 and n<=10:
        student_marks = {}
        for i in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        avgPercent(student_marks[query_name])

