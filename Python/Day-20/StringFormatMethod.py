# Placeholder ko string ke bich me set krne ke liye Stri format method ka use kya jata he
# placehoder define { } se hota h
w="monika {} prajapat {}".format("hello",20);
print(w)

w="Welcome {1} to OiLab {0}".format("monika",200);
print(w)
w="Welcome {a} to OiLab {b}".format(a=32220,b=200);
print(w)

# placehoder ho size kese de? ^ < >
w="Welcome {a:<5} to OiLab {b:^10}".format(a=20,b=200);
print(w)



