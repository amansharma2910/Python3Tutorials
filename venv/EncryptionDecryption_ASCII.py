string1= input("Enter an alphabetic string: ")
string2= ""
for char in string1:
    string2 += str(ord(char)-32)
print("Encrypted message :", string2)

string1= ""
for i in range(0, len(string2)-1,2):
    string1 += chr((((int(string2[i]))*10) + int(string2[i+1]))+32)
print("Decrypted message :", string1)