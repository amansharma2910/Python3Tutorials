string1= input("Enter a string that you want to convert into acronymn: ")
list1= string1.split()
acronymn= ""
for i in list1:
    if i=="of" or i=="and":
        continue
    else:
        acronymn+=i[0]
print(acronymn.upper())

