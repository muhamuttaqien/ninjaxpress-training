
# name = input("Enter name: ")
# print("Your name is", name)

# OPERASI TERHADAP TIPE DATA (STRING)
# my_string = "Hello world!"

# print(len(my_string))
# print(my_string[0:6]) # 0-5
# print(my_string[0:8]) # 0-7
# print(my_string[0])

# my_string = my_string.replace("world", "friend")
# print(my_string)

# a = "Hello"
# b = "World!"
# c = a + " " + b
# print(c)

# a = "Siap"
# b = 86
# c = a + " " + str(b)
# print(c)

# nama = "Angga"
# alamat = "Tokyo"

# my_profile = "Nama saya {} dan saat ini saya bekerja di {}.".format(nama, alamat)

# print(my_profile)

# x = "Indonesia AI"
# print(x[2:4])

# BOOLEANS
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 10
# b = 9

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than b")

# LIST
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append("my string")
my_list.append(10 > 9)

print(my_list)

print(True and False)

experience = 3
level = 1

if experience >= 3 and level == 2:
    print("Recommended salary is 9,000,000");
elif experience <=3 and level == 2:
    print("Recommended salary is 7,000,000")
else:
    print("Recommended salary is 5,000,000")