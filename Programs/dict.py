import math as m
a = m.sqrt(337)
print(a)
values = ["1","2","3"]
names = ["I'm", "Jatin", "Yadav"]
des = dict(zip(values,names))
print(des)

print("--------")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

print("--------")


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

print(car)

print("--------")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

print(car)

print("--------")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

print(car)

print("--------")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)


