list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
n=len(list1)
for i in range(n):
    if list1[i] not in list2:
        print(list1[i],"not in list2")

