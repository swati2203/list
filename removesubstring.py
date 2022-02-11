mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
str1=mainStr.split(" ")
i=0
while i<len(str1):
       if  "over" in str1[i]:
              str1[i]="on"
       i+=1   
print(str1)  

       
       

# a=int(input("enter no"))
# i=0
# min=i
# while i<=a:
#        if min==1:
#        n=int(input("enter no."))
       

