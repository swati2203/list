# list=[1,-2,3,-4,5,6,-7,-9]
# list=[2,3,4,0,7,0,6,0,5]
# list=["1","2","3","5","6","7"]
# op=["12","35","67"]
# i=5
# while i>=1:
#     print(str(i)*i)
#     i=i-1

# a=[]
# for i in list:
#     if i<0:
#         i=0
#         a.append(i)
#     else:
#         a.append(i)
# print(a)    

# b=[]
# c=[]
# for i in list:
#     if i==0:
#         c.append(i)
#     else:
#         b.append(i)
# print(c)
# print(b)
# for i in c:
#     b.append(i)
# print(b)




# i=0
# l=len(list)
# a=[]
# while i<l:
#     sum=list[i]+list[i+1]
#     a.append(sum)
#     i=i+2
# print(a)



# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i-1
    

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i-1

    

n=[10,11,12,13,14,17,18,19]
a=[]
i=0
while i<len(n):
    if n[i]+n[i+1]==30:
        a.append(n[i],n[i+1])
    i=i+1
print(a)