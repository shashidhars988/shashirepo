import random

lplayagain = ''
while lplayagain == '':
    rand = random.randrange(1,7,1)
    if rand == 1:
        print("o")
    elif rand == 2:
       print("o \n o")
    elif rand == 3:
       print("o \n o \n  o")
    elif rand == 4:
       print("o o \no o")
    elif rand == 5:
       print("o   o \n  o \no   o")
    else:
        print("o o o \no o o")          
                  
    lplayagain = input("\nPress enter to roll again!")
