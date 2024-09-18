def function3(c1):
    first = c1[0]
    last =c1[len(c1) -1]
    combined = last + first
    return combined.upper()

c1 = input ("Enter a word:-")
print(function3(c1))
    
