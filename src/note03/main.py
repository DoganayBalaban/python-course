# list
foods = ["pizza", "hamburger", "hotdog", "spagetti"]
print(foods[0])
foods[0] = "chicken"
print(foods[0])

foods.append("ice cream")
foods.remove("hotdog")
foods.pop()
foods.insert(0, "cake")
foods.sort()
foods.clear()

for food in foods:
    print(food)

print("--------------------------------------")

drinks = ["coffee", "water", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["ice cream", "cake"]

meals = [drinks, dinner, dessert]
print(meals)
print(meals[0][0])

print("--------------------------------------")
# tuple = sıralı ve değiştirilemez koleksiyonlardır, dataları gruplamak

student = ("Doğanay", 21, "male")
print(student.count("doğanay"))
print(student.index("male"))

for x in student:
    print(x)
if "Doğanay" in student:
    print("Doğanay is here")

print("--------------------------------------")
# set = sırasız, indeksiz koleksiyonlar
utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
utensils.update(dishes)
dinnerTable = utensils.union(dishes)

for x in dinnerTable:
    print(x)

print("--------------------------------------")

for x in utensils:
    print(x)

print("--------------------------------------")
print(utensils.difference(dishes))
print(utensils.intersection(dishes))

print("--------------------------------------")
print("--------------------------------------")
# dictionary = değişilebilir, sırasız, key-value çiftleri içeren koleksiyonlardır.

capitals = {'USA': 'Washington',
            'India': 'New Delhi',
            'Japan': 'Tokyo',
            'France': 'Paris'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'India': 'Singapore'})
capitals.pop("Japan")
#capitals.clear()

print(capitals['USA'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

print("--------------------------------------")

print("--------------------------------------")
#index operator []

name = "bro Code"
if (name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[0:3].upper()
print(first_name)