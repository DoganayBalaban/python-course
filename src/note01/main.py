#variables
name = "Doğanay"
age = 20
GANO = 3.26
isStudent = True
#print("my name is " +name + " age is " + str(age) + " and am i student:"+ str(isStudent) + " and" + " my gano " +str(GANO))
name2,age2,GANO2 = "emre",20,2.20
#print("my name is " +name2 + " age is " + str(age2) + " and am i student:"+ str(isStudent) + " and" + " my gano " +str(GANO2))

#some string methods
print(len(name))
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*3)

#typeCasting
x=1
y=2.0
z="3"

y=int(y)
x=float(x)

print(x)
print(y)
print(z*3)
print(int(z)*3)

#userInput
surname=input("What is your surname?")
old = int(input("How old are you?"))
height = float(input("How tall are you?"))
print("hello"+surname)
print("you are "+str(old)+" old")
print("you are "+str(height)+" cm tall")