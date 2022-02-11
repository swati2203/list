from sqlite3 import SQLITE_CREATE_TEMP_INDEX


numbers=[50,40,23,70,56,12,5,10,7,69]
max=0
for i in numbers:
    if max<i:
        max=i
secmax=0
for i in numbers:
    if i!=max and secmax<i:
        secmax=i
print(secmax)

        


