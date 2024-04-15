l = int(input("Input length of square: "))
print( )

print("*"*l + " " + "*"*l)

for i in range(l-2):
    print("*"*l + " " + "*" + " "*(l-2) + "*")

print("*"*l + " " + "*"*l)