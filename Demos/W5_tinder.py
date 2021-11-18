def interests():
  print("Enter your interests,")


def tinderDaSecond():
  print("First person: ")
  p1 = interests()
  print("Second person: ")
  p2 = interest()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"Yey - you are a match made in heaven! You have {len(common)} interests in common.")
  else:
    print(f"Well, I don't think it will work out :( You only have {len(common)} interests in common")
tinderDaSecond()  