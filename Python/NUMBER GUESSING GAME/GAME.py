import random
cname=random.randrange(1,200)
userInp=int(input("Enter Your Number"))
if userInp>cname:
    print("your guess number is high.......",cname)

    print("your guess number is high.......")
elif cname>userInp:
    print("your guess number is high.......",cname)

    print("your guess number is Low.......")
else:
    print("your guess number is high.......",cname)

    print("your guess number is Equal.......")

