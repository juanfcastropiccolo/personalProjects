expression = input("Expression: ")


x, y, z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    print(float(round(x + z, 1)))
elif y == "-":
    print(float(round(x - z, 1)))
elif y == "*":
    print(float(round(x * z, 1)))
elif y == "/" and z != 0:
    print(float(round(x / z, 1)))
else:
    print("Bad expression")
