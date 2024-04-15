age = int(input("What is your age?"))
you_fish = (input("Do you have a fishing license in Minnesota (yes/no)?"))
if you_fish.lower() in 'yes':
    print("yes")
else:
    print("no")
parent = (input("Does your parent have a fishing license (yes/no)?"))
if parent.lower() in 'yes':
    print("yes")
else:
    print("no")

legal = age, you_fish, parent
if age<=15 and you_fish == "no" and parent == "yes":
    legal = True
else: False

if legal == True:
    print("You are legal to fish in Minnesota.")
else:
    print("You are not legal to fish in Minnesota.")

