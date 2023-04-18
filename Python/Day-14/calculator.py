# How to Build Simple Calculator in Python
print('''
+ADD
-SUBTRACT
*MULTIPLY
/DIVIDE
''')
num1=int(input("Enter The Value 1 :-"))

num2=int(input("Enter The Value 2 :-"))

opr=input("Please Enter Operator")

if opr=="+":
	print(num1+num2)
elif opr=="-":
	print(num1-num2)
elif opr=="*":
	print(num1*num2)
elif opr=="/":
	print(num1/num2)
else:
	print("Please Enter Currect Operator")