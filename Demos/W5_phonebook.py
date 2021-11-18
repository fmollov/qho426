#Initialise empty dictionary
phonebook = {}
d2 = dict()
print(type(phonebook))

#Initialise non-empty dictionary
Fikret_data = {"Name": "Fikret", "Age" : 55, "Dogo": False, "Title" : "Mr"}

#Print full dictionary
print(Fikret_data)

#Use part of the dictionary for printing purposes
x = Fikret_data["Name"]
y = Fikret_data["Age"]
print(f"{x} is {y} years old")

#Adding elements to a dictionary
phonebook["Max"] = "077895865845"
phonebook["Ugabuga"] = "07758124512"
phonebook["Lucy"] = None

print(phonebook)

#Add more people to the phonebook
for i in range(3):
  n = input("Enter the name: ")
  numb = input(f"Enter {n}'s number: ")
  phonebook[n] = numb

name = input("Who you like to call?")

if 
if name in phonebook:

  print(f"Calling {name} with phone number {phonebook[name]}")
else:
  print(f"{name} is not in your phonebook")