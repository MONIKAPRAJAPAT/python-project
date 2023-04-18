# Python String Function
# lower()
# upper()
# title() // capital each word
# capitalize() 
#find()
#index()
# isalpha()
#isdigit()
#isalnum()
#chr()
# ord()


w="Monika Prajapat"
n=w.lower()
print(n)

# upper()
w="Monika Prajapat"
n=w.upper()
print(n)

# title()

w="Monika Prajapat hello everOne"
n=w.title()
print(n)


# capitalize() 
w="Monika Prajapat hello everOne"
n=w.capitalize()
print(n)

#find()
w="welcome to monika coding life"

print(w.find('m',6))

#index
w=" I love My Family"

print(w.index('F'))

# index me value nhi milti to error return kr deta he



# isalpha()
# only aplphabets use you
w="dszd12sad"

print(w.isalpha())



#isdigit()
# only use number and digits
w="45454"

print(w.isdigit())



#isdigit()
# "" me number ho ya text output true hi milega answer
#isdigit function me alphabet and number use only Special charactor not used
w="monuprj"
w="monuprj@"

print(w.isalnum())


# chr()
# Convert integer 65 to ASCII Character('A')

w=chr(65)

print(w)

# output A

w=67;

print(chr(w))

# ord()
# Convert ASCII Unicode Character 'A' to 65
w='a'
print(ord(w))
