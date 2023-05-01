# Generating a random number
import random
print(random.randrange(1,10))


a ="hello World"
#1
print(a.replace("h", "j"))
#2
print(a.split())

#3
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#4
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

#5
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#6
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#7
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#8
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#9
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#10
thislist = ["apple", "banana", "cherry"]
del thislist


#11
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#12
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#13
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']
newlist = [x if x != "banana" else "orange" for x in fruits]


#14
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#15
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



#16
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#17
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



#18
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.remove("banana") # Will raise error if banana is not present
thisset.discard("banana") # Will not raise error
thisset.clear()
del thisset
x = thisset.pop() # Pops random element
print(thisset)

#19
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)



#20
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)  # Apple
x.symmetric_difference_update(y) #The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
z = x.symmetric_difference(y)    # The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.