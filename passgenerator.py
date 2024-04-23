
import random
import string

print()
print()

print('=========================================== THE PASSWORD GENERATOR ==========================================    ')

print()
length = int(input('Enter the length of your password: '))

print()
if length<=4:
    print('!!!! warning !!!! \n \npassword length should be greater than 4')
    print()
    print()
else:
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    special = string.punctuation
    nums = string.digits

    all = upper_case+lower_case+special+nums

    temp = random.sample(all,length)

    password = "".join(temp)

    print('Your password as per the given length is :',password)

    print()
    print()
