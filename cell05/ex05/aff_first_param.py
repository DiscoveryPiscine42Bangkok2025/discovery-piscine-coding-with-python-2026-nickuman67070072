text = input()

if text.strip() == "":
    print("none")
else:
    params = text.split()
    print(params[0])