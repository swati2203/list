a=0
while a<10:
    a=a+1
    if a==2 or a==5:
        continue
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count+=1
        i=i+1
    if count==2:
        print("prime number",a)
    # else:
    #     print("not prime number",a)


    