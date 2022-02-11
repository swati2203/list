binary_number=[1,0,0,1,1,0,1,1]
l=len(binary_number)
i=l-1
a=0
sum=0
while i>-1:
    sum+=binary_number[i]*(2**a)
    i=i-1
    a=a+1
print(sum)
    