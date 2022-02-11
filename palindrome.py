n=["n","i","t","i","n"]
y=n
l=len(n)
sum=""
i=l-1
while i>-1:
    sum+=n[i]
    i=i-1
print(list(sum))
if list(sum)==y:
    print("palindrome")
else:
    print("not palindrome")