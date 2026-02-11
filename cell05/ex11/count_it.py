text = input().strip()

if text == "":
    print("none")
else:
    params = text.split()
    print(f"parameters: {len(params)}")
    
    for word in params:
        print(f"{word}: {len(word)}")