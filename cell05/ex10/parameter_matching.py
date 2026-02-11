
param = input()

if param.strip() == "":
    print("none")
else:
    word = input("What was the parameter? ")
    
    if word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")