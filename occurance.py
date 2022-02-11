char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
b=[]
for i in char_list:
    if i not in b:
        b.append(i)
print(b) 
for i in b:
    count=0
    for x in char_list:
        if x in i:
            count+=1
    print(i,count)








   
   


        