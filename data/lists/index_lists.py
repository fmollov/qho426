def movement():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    path = movement()
    for i in range(0, len(path), 2):
        print(f"{path[i]} for {path[i+1]} steps")

#range(start, end, step)
#range(end) if 1
#range(start, end) if 2 etc.

run()