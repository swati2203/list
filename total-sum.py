# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# a=len(n)
# i=0
# while i<a:
#     j=1
#     b=len(n)
#     while j<b:
#         if (n[i])+(n[j])==number:
#             c=[n[i],n[j]]
#             print(c,end="")
#         j+=1
#         d=[]
#         d.append(i)
#         print(d)
#     i=i+1


# b=["zero","one","two","three","four","five","six","seven","eight","nine"]
# i=0
# a=[]
# while i<7:
#     x=int(input("enter the number"))
#     a.append(b[x])
#     i=i+1
# print(a)

# 

sum=""
i=0
while i<5:
    a=input("enter the nasmes")
    sum+=a+","
    i=i+1
print(sum)
list=sum.split(",")
print(list)
list2=[]
list2.append(list[::-1])
print(list2)

# a=["swati is the navgurukul student"]
# i=0
# while i<len(a):
#    b=list(a[i])
#    print(b)
#    i=i+1
# i=0
# c=[]
# for i in b:
#     if i not in c:
#         c.append(i)
# print(c)
# for i in c:
#     count=0
#     for j in b:
#         if i in j:
#             count+=1
#     print(i,count)

