f = int(input("first:"))
s = int(input("second:"))
print(str(f) + " x " +  str(s) + " = " +  str((f * s)))
if (f * s) > 0:
    print("This number is positive")
elif (f * s) == 0:
    print("This number is both positive and negative.")
else:
    print("This number is negative.")