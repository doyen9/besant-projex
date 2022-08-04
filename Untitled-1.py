




a,b,c = 0,0,0


def abc():
    global a
    global b
    global c


    a = 5
    b= 9
    c = a+b
    return a,b,c

abc()
print(a,b,c)