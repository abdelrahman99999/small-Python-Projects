import random 
y='abcdefghigklmnopqrstuvwxyz'
z='1234567890'
k='!@#$%^&*'
x=y+z+k

size = int(input('enter the size of pass ? '))
chars = input('do you want chars ? ')
numbers = input('do you want numbers ? ')
special = input('do you want special chars ? ')
password=''

while len(password) < size :
    random_char=random.choice(x)
    if chars =='no':
        if random_char in y:
            random_char = ''
    elif numbers == 'no' :
        if random_char in z:
            random_char = ''
    elif special == 'no':
        if random_char in k:
            random_char = ''
    password = password + str(random_char)

print(password)
q=input()
