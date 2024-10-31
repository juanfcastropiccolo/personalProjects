number = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip()

match number:
   case "42" | "forty-two" | "forty two" | "FoRty TwO":
      print("Yes")
   case _:
      print("No")

