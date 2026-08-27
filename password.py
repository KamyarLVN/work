import random
password_length = 0
pass_list = []
while password_length < 8:
    password_length = int(input("how many charactrs do you want your password to have?(8 or more): "))
characters = ["1","2","3","4","5","6","7","8","9","#","@","*","&","_"]
for i in range(password_length):
    list = random.choice(characters)
    pass_list.append(list)

random.shuffle(pass_list)
password = ""
for i in pass_list:
    password += i
print(password)
