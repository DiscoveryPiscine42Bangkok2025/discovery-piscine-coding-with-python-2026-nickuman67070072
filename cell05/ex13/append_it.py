text = input().strip()

if text == "":
    print("none")
else:
    params = text.split()
    found = False
    
    for word in params:
        if not word.endswith("ism"):
            print(word + "ism")
            found = True
    
    if not found:
        print("none")