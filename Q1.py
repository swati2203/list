# #write your five friends name in list
# a=["mala","priya",""]

a=int(input("enter the number a :"))
b=int(input("enter the number b :"))
c=int(input("enter the number c :"))
if(a>b and a>c):
    print("a is max")
elif(b>a and b>c):
    print("b is max")
elif(c>a and c>b):
    print("c is max")
else:
    print("nothing")