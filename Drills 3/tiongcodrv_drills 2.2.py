age = int(input("Please enter you age:"))
natural = (input("Are you a natural born citizen of the U.S. (yes/no)?"))
if natural.lower() in 'yes':
    print("yes")
else:
    print("no")
years = int(input("How many years have you resided in the U.S.?"))

eligible = age, natural, years
if age>=35 and natural == "yes" and years >= 14:
    eligible = True
else: False

if eligible == True:
    print("You can run for president of USA.")
else:
    print("You cannot run for president of USA.")

