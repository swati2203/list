n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
l=len(n)
b=[]
for i in n:
    if i not in b:
        b.append(i)
print(b)
for i in b:
    count=0
    for x in n:
        if x is i:
            count+=1
    if count>=2:
        a=[]
        a.append(i)
        print(a)





