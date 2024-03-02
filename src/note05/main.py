#str.format() outputlarda kullanıcıya daha fazla kontrol tanır

animal = "cow"
item = "moon"
print("the " + animal+" jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

text="The {} jumped over the {}"
print(text.format(animal,item))

name="bro"
print("hello, my name is {:10}. Nice to meet you!".format(name))
print("hello, my name is {:<10}. Nice to meet you!".format(name))
print("hello, my name is {:>10}. Nice to meet you!".format(name))

number = 3.14159
number2 = 1000
print("the number pi is {:.2f}".format(number))
print("the number is {:,}".format(number2))
print("the number is {:b}".format(number2))
