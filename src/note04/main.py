#functions

def hello(name):
    print("Hello " + name)
    print("Have a nice day")

hello("doğanay")
hello("emir")

def nameWriter(firstName, lastName,age):
    print("Hello " + firstName + " " + lastName)
    print("your age is " + str(age))

nameWriter("Doğanay","Balaban",20)


print("--------------------------------------")
print("--------------------------------------")

#return statement

def multiply(a,b):
    return a*b

print(multiply(3,2))

print("--------------------------------------")
print("--------------------------------------")
#nested functions

#print(round(abs(float(input("Enter a number: ")))))

print("--------------------------------------")
print("--------------------------------------")

#*args == argumentleri tuple yapar
def add(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return sum

print(add(1,2,3))


print("--------------------------------------")
print("--------------------------------------")
#**kwargs = argumentleri dictionary yapar
def hello(**kwargs):
    #print("Hello " + kwargs['firstName'] + " " + kwargs['lastName'])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")
hello(title="Mr.",first="Bro",middle="Dude",last="Code")




