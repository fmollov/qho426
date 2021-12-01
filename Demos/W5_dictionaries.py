#Initialise empty dictionary
phonebook = {}
d2 = dict()

#Initialise non-empty dictionary
piotr_data = {"Name": "Piotr", "Age" : 55, "Doggo": False, "Title" : "Mr"}

#Print full dictionary
print(piotr_data)

x = piotr_data["Name"]
y = piotr_data["Age"]
#Use part of the dictionary for printing purposes
print(f"{x} is {y} years old")

#Adding elements to a dictionary
phonebook["Max"] = "+447789564839"
phonebook["Ugabuga"] = "+5677467364736"
phonebook["Lucy"] = None

print(phonebook)

#Add more people to the phonebook
for i in range(3):
    n = input("Enter the name: ")
    numb = input(f"Enter {n}'s number: ")
    phonebook[n] = numb

name = input("Who would you like to call?")

if name in phonebook:
    print(f"Calling {name} with phone number {phonebook[name]}")
else:
    print(f"{name} is not in your phonebook")