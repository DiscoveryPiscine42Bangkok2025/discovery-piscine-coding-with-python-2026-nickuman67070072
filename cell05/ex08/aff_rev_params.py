text = input()

params = text.split()

if len(params) < 2:
    print("none")
else:
    for word in reversed(params):
        print(word)