import random

alphnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

while 1:
    password_len = int(input("Length of your password you want?: "))
    password_count = int(input("How many password you want?: "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_alphnum = random.choice(alphnum)
            password = password + password_alphnum
        print("Your password: ",password)
