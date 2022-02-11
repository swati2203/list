marks = [[78, 76, 94, 86, 88],
[91, 71, 98, 65],
[95, 45, 78],
[87, 67, 49, 68, 88]
]
n=len(marks)
i=0
sum=0
while i<n:
    j=0
    m=len(marks[i])
    while j<m:
        sum+=marks[i][j]
        j=j+1
    i=i+1
print(sum)


