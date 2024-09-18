def main():
    a = 10
    b = 20 
    c = 30

    if a > b and b > c:
        print("A")

    if not (a > b and a > c):
        print("B")

    if a > b or a > c:
        print("C")
    
    if not (a > b or a > c):
        print("D")

main()
    
