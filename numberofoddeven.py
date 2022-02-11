elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=len(elements)
conte=0
count=0
while i<a:
    if elements[i]%2==0:
        conte+=1
    else:
        count+=1
    i=i+1
print("total no. of odd numbers:",count)
print("total no. of even number:",conte)