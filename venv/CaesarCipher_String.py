string1= input("Enter an alphabetic string: ")
key= int(input("How many characters do you want the string characters to shift(1-26): "))
string2= ""
for char in string1:
    if ((ord(char)>=65 and ord(char)<=90-key) or (ord(char)>=97 and ord(char)<=122-key)):
        string2 += chr(ord(char)+key)
    elif (char.isalpha()==False):
        string2 += char
    elif (ord(char)>=91-key and ord(char)<=90) or (ord(char)>=123-key and ord(char)<=122):
        string2 += chr(ord(char)-26+key)
print("Encrypted message :", string2)

string1= ""
for char in string2:
    if ((ord(char)>=65+key and ord(char)<=90) or (ord(char)>=97+key and ord(char)<=122)):
        string1 += chr(ord(char)-key)
    elif (char.isalpha()==False):
        string1 += char
    elif (ord(char)>=65 and ord(char)<=64+key) or (ord(char)>=97 and ord(char)<=96+key):
        string1 += chr(ord(char)+26-key)
print("Decrypted message :", string1)
