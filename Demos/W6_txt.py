with open("harry.txt") as h:
    with open("john.txt") as j:
        h_lines = h.readlines()
        j_lines = j.readlines()

h = open("harry.txt")


for i in range (len(h_lines)):
    print(f"\033[92mJohn: {j_lines[i]}\033[0m", end = "")