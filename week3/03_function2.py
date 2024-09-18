def function2(b1, b2):
    len1 = len(b1)
    len2 = len(b2)
    shorter_length = min(len1, len2)
    return shorter_length

b1 = input("Enter b1:-")
b2 = input("Enter b2:-")
print(function2(b1,b2))