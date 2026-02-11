keyword = input()
text = input()

count = text.count(keyword)

if keyword.strip() == "" or count == 0:
    print("none")
else:
    print(count)