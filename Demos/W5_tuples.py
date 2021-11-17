def simple_tuples():
    person = ("Fikret", 32, True)

    #Printing a tuple
    print(person)
    #Check data type
    print(type(person))
    #Access elements via inbox
    print(f"{person[0]} is {person[1]} year old")
    #No mutation possible
    #person[0] = "Fikret"
    #print(person)
    if person[2]:
        print("You have a doggo!")
    else:
        print("No doggo no fun!")
        #Tuples can be concatenated (joined - but this creates a different tuple)
    p1 = person + (20, "None")
    print(p1)
    print(person)
    t = (16, 8, 9, 21, 55)
    print(max(t))
    print(min(t))
    print(min(p1))


