l=[]
while True:
    c=int(input('''
        1  Push Elements
        2 Pop  First Element
        3 Front Element
        4 Last Element 
        5 Display Stack
        6 Exit
    '''))
    if c==1:
        n=input("Enter The Value :-")
        l.append(n)
        print(l)
    elif c==2:
        if len(1)==0:
            print("Empty Queue")
        else:
            del l[0]
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("First Queue Value:- ",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("Last Queue Value:- ",l[-1])
    elif c==5:
        print("Displa Queue",l)
    elif c==6:
        break;
    else:
        print("Enter only 1 to 6 Number ")