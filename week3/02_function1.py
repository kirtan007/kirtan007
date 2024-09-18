def function1(a1,a2,a3):
    sum = a1 + a2 + a3
    minimum = min(a1,a2,a3)
    return sum - minimum

a1 = int(input("number:-"))
a2 = int(input("number:-"))
a3 = int(input("number:-"))
print(function1(a1,a2,a3))