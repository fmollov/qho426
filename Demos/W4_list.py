#Declare empty list
hated = []

#Declare non-empty list
fav = ["Carbonara", "Pizza", "Casatiello", "Pierogi"]

#Print full list
print(fav)

#Print a single element
print(fav[2])

#Add elements at the end of the list
hated.append("Tofu")
hated.append("Beans")
fav.append("Lasagne")

#Appending using a loop and user input
for i in range(2):
    print("Enter another hated dish: ")
    dish = input()
    hated.append(dish)

#Print out the length/size of my list "hated"
print(len(hated))

print(hated)

#Insert data at any position on the list
print(fav)
dish = input("Enter next dish to be inserted to the 1st position: ")
fav.insert(1,dish)
print(f"The number of favourite dishes is: {len(fav)} ")
print(fav)
fav.insert(3, "Pancakes")
print(fav)
print(f"The number of favourite dishes is: {len(fav)} ")

#Remove item from the list
fav.remove("Casatiello")

print(fav)

#Remove by index (and return)
x = fav.pop(1)

#Delete an item via index (forever and ever)
del fav[2]

print(fav)

#Slicing
print(hated[::-1])

for i in range(len(fav)):
    if fav[i] == "Pizza":
        print(f"Pizza is located in position {i}")

print(f"Pizza is located in position {fav.index('Pizza')}")