name = input("Enter your name: ")

if len(name) > 8:
    print("You have a looooong name! Can I use a nickname please?")
elif name == "Max":
    print("That's a boring name!")
elif len(name) <= 3:
    print("Wooow, your name is super short and easy to remember")
else:
    print("Oh, your name is pretty short")
print("Nevertheless, welcome to the session {}!".format(name))