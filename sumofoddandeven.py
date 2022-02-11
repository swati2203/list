elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
a=len(elements)
i=0
sum1=0
sum=0
while i<a:
    if elements[i]%2==0:
        sum1+=elements[i]
    else:
        sum+=elements[i]
    i=i+1
print("sum of even numbers",sum1)
print("sum of odd numbers",sum)