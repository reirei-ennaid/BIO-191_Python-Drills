D = int(input("Enter D: "))
print(D)

ast = 1
while ast <= D:               
    for j in range(0, ast) :
        if (j != ast) :                  
            print("*", end=" ")
    ast = ast + 1
    print()
