import math,time

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))

# string slices
name = "Doğanay Balaban"
first_name = name[0:7:1]
print(first_name)
last_name = name[8:16:1]
print(last_name)
deneme = name[0:16:2]
print(deneme)
deneme2 = name[8:]
print(deneme2)
reversed_name = name[::-1]
print(reversed_name)

website_url = "http://www.python.org"
slice = slice(11, -4, 1)
print(website_url[slice])

# if statement
age = int(input("How old are you? "))

if 25 > age >= 18:
    print("You are a teenager")
elif age >= 70:
    print("You are a old")
elif age < 18:
    print("You are a child")
else:
    print("Wrong age")

# logical operators

temp = int(input("What is your temperature? "))
if 30 >= temp & temp > 0:
    print("the temp is good today")
elif temp < 0 | temp > 30:
    print("the temp is bad today")

if 1 != 2:
    print("1 ,2 ye eşit değil")

#loops
nameLoop = ""
while len(nameLoop) == 0:
    nameLoop = input("Enter your name: ")
print("hello " + nameLoop)

for i in range(10):
    print(i+1)

for i in range(50,100 + 1):
    print(i)

for i in range(50,100 + 1,2):
    print(i)

for i in "Bro Code":
    print(i)
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year")

rows = int(input("how many rows do: "))
cols = int(input("how many columns do: "))
symbol = input("enter a symbol use: ")
for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()
#break döngüyü sonlandırır
#continue yeni iterasyona atlar
#pass bişey yapmaz yer tutucududr
