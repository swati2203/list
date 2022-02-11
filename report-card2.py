marks = [[78, 76, 94, 86, 88],
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]]
i=0
sum=0
n=len(marks)
while i<n:
    j=0
    m=len(marks[i])
    while j<m:
        sum+=marks[i][j]
        j+=1
    print("average of",i+1,"year:",sum/m)
    i+=1

