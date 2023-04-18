# Stack is a linear dat Structure
l=[]
while True:
    c=int(input('''
        1 Push Eelements
        2 Pop Eelements
        3 Peek Eelement
        4 Display stack
        5 Exit
    '''))
    if c==1:
        n=input("Enter The Value :")
        l.append(n)        
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack :")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:        
        if len(l)==0:
            print("Empty Stack :")
        else:
            print("Last Stack Value :",l[-1])
    elif c==4:
        print("Display Stack :",l)
    elif c==5:
            break;
    else:
            print("Please Enter Valide Number")