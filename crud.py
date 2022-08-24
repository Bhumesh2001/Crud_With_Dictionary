# crud optioration on dictionary.

d = {}
while True:
    # create 
    print()
    print("press 1 for creat\npress 2 for read\npress 3 for update\npress 4 for delete\npress 5 for exit")
    print()
    n = int(input("enter your choice: "))
    # create
    if n == 1:
        y = (input("enter your mobile number: "))
        if len(y)==10:
            d[y]=[input("enter your name: "),input("enter your email: "),input("enter your address: ")]
        else:
            print("please enter correct mo.number")
    #read
    elif n == 2:
        y = (input("which mo.number do you want to read: "))
        if len(y)==10:  
            if y in d:
                print(d[y])
            else:
                print("your enter mo.number not exist")
        else:
            print("please enter correct mo.number")
    # update
    elif n == 3:
        v = (input('which mo.number of data do you want to update: '))
        if len(v)==10:
            if v in d:
                a=[input("enter your name: "),input("enter your email: "),input("enter your address: ")]
                d[v]=a
                print(d)
            else:
                print('your enter mo.number not exist')
        else:
            print("please enter correct mo.number")
    # delite
    elif n == 4:
        mo = (input("which mo.number do you want delete: "))
        if len(mo)==10:
            if mo in d:
                d.pop(y)
                print(d)
            else:
                print("your enter mo.number not exist")
        else:
            print("please enter correct mo.number")
    # exist
    else:
        print("your are exit")
        break

