magic_square =[
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]]
# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         j=int(input("enter the number"))
#         b.append(j)
#     a.append(b)
# print("matrix is.....")
# for i in range(3):
#     for j in range(3):
#         print(a[i][j],end="")
#     print()
sumd1=0
sumd2=0
for i in range(3):
    for j in range(3):
        if i==j:
            sumd1+=magic_square[i][j]
        if i+j==3-1:
            sumd2+=magic_square[i][j]
# print(sumd1,sumd2)
if sumd1!=sumd2:
    f=1
else:
    
    for i in range(3):
        sumr=0
        sumc=0
        for j in range(3):
            sumr=sumr+magic_square[i][j]
            sumc=sumc+magic_square[j][i]
        print(sumc,sumr)
        if sumc!=sumd1:
            f=1
        elif sumr!=sumd2:
            f=1
        else:
            f=0
if f==0:
    print("this is magic square")
else:
    print("this is not a magic square")    





