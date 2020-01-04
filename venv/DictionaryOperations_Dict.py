## Let us cosider the list given below as an example.
# dict1 = {"f_name" : "Aman" , "l_name" : "Sharma" , "reg_no" : "19BAI10007" , "prog" : "BTECH"}

## dict1.values() will return all the values stored in the dictionary.
# print(dict1.values())

## dict1.keys() will return all the keys stored inside the dictionary.
# print(dict1.keys())

## By using the method given below, we can print all the key value pair in the dictionary.
# for k,v in dict1.items():
#     print(k, ":" , v)

## The following program will create a list of customers
customer_list = []
while True:
    enter = input("Enter customer (Y/N?) : ")
    enter = enter.strip().lower()
    if enter == "y" or enter == "yes":
        f_name, l_name = input("Enter customer name : ").split()
        customer_list.append({"f_name" : f_name , "l_name" : l_name })
    elif enter == "n" or enter == "no":
        break;
for i in customer_list:
    print(i)

