
text = input().strip()

count = text.count('z')

if text == "" or count == 0:
    print("none")
else:
    print("z" * count)