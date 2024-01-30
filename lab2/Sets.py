#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#example
thisset = {"apple", "banana", "cherry"}
print(thisset)

#example
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#example
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#example
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#example
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#example
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#example
set1 = {"abc", 34, True, 40, "male"}

#example
myset = {"apple", "banana", "cherry"}
print(type(myset))

#example
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

