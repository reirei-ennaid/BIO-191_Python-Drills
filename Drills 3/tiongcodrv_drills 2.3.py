d = int(input("Please enter an integer:"))
r = int(input("Please enter another integer:"))
v = int(input("Please enter a third integer:"))

maxNum = d
if r > maxNum:
    maxNum = r
if v > maxNum:
    maxNum = v

if maxNum % 2 == 1 :
    print(maxNum, "is the largest odd integer.")
else:
    print("The largest integer is not odd.")