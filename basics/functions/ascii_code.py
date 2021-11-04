print("Program started!")
print("Please enter a standard character:")
character = input()
if len(character) == 1:
  x = ord(character)
  print(f"The ASCII code for {character} is {x}.")
else:
  print("Wrong input given, you should have enter one character")

print("Program ended!")