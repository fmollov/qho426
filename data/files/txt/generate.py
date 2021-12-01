def search(name):
  print("Searching...")
  data = {}
  with open(name) as f:
    for line in f:
      if line.startswith("Section"):
        items = line.split(":")
        s_name = items[1]
      elif section in data:
        data[section].append(line)
      else:
        data[section] = [line]
  print("Done!")
  return data

def run ():
  d = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.csv", "w") as potato:
    for s, l_b in d.items():
      for item in l_b:
        potato.write(f"{s}, {item}\n")



run()
        