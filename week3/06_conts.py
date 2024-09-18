def a1(a):
    years = a + 10
    print("1.", years)

def a2(years):
    print("2.", years)
    years = 20

def main():
    years = 5 
    a1(years)
    print("3.", years)
    a2(years)
    print("4.", years)

main()