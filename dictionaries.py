thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")

x = thisdict["model"]

x = thisdict.keys()
x = thisdict.values()
x = thisdict.items() # Return dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.update({"year": 2020})

thisdict["color"] = "red" # Adding items
thisdict.update({"color": "red"})


thisdict.pop("model") # Removing items  {'brand': 'Ford', 'year': 1964}
thisdict.popitem()  #{'brand': 'Ford', 'model': 'Mustang'}
del thisdict["model"]
del thisdict
thisdict.clear()





#Looping
for x in thisdict:
  print(x)              #brand model year

for x in thisdict:
  print(thisdict[x])    #Ford Mustang 1964

for x in thisdict.keys():
  print(x)              #brand model year
for x in thisdict.values():
  print(x)              #Ford Mustang 1964

for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964   








