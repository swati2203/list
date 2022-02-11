elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
a=len(elements)
i=0
sum1=0
sum=0
sum2=0
counte=0
count=0
count1=0
while i<a:
    sum2+=elements[i]
    count1+=1
    if elements[i]%2==0:
        counte+=1
        sum1+=elements[i]
    else:
        count+=1
        sum+=elements[i]
    i=i+1
print("sum of even numbers:",sum1)
print("count of even numbers:",counte)
print("average of even numbers:",sum1/counte)
print("sum of odd numbers:",sum)
print("count of odd numbers:",count)
print("average of odd numbers:",sum/count)
print("total sum of elements:",sum2)
print("total count of elements",count1)
print("average of elements",sum/count1)