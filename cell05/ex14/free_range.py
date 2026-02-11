text = input().strip()

params = text.split()

if len(params) != 2:
    print("none")
else:
    start = int(params[0])
    end = int(params[1])
    
    numbers = list(range(start, end + 1))
    print(numbers)