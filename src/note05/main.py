# str.format() outputlarda kullanıcıya daha fazla kontrol tanır

animal = "cow"
item = "moon"
print("the " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "bro"
print("hello, my name is {:10}. Nice to meet you!".format(name))
print("hello, my name is {:<10}. Nice to meet you!".format(name))
print("hello, my name is {:>10}. Nice to meet you!".format(name))

number = 3.14159
number2 = 1000
print("the number pi is {:.2f}".format(number))
print("the number is {:,}".format(number2))
print("the number is {:b}".format(number2))

print("--------------------------------------")
print("--------------------------------------")

# random sayı
import random

x = random.randint(1, 10)
y = random.random()
print(x)
print(y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king", "A"]
random.shuffle(cards)
print(cards)
print("--------------------------------------")
print("--------------------------------------")
# exception handling

try:
    #x = int(input("Enter a number to divide: "))
   # y = int(input("Enter a number to divide by: "))
    result = x / y
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("Always work !")

print("--------------------------------------")
print("--------------------------------------")

#file dedection
import os

path = "/Users/doganaybalaban/Desktop/DEVELOPER/PostgreSQL Dersleri.docx"

if os.path.exists(path):
    print("the file exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("the file does not exist")