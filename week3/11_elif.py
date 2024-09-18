name = input("Enter your name:-")
age = input("Enter your age:-")
#print("Hello, ", name,". You are ",age," years old",sep="")
# fstring
print(f"Hello,{name}. You are {age} years old.")

# The both are same but the diffrence is only second one is use fstring and first one is not
# important:
# when we use fstring then we should use curlly brackets otherways we can not use fstring and fstring is easy for use 

pi = 3.141592653589
print(pi)
Formatted_pi = f"Value of pi to 2 decimal places : {pi: .2f}"
print(Formatted_pi)

salary = float(input("Enter your weekly salary:-"))
print(f"Your weekly salary is :-{salary:.2f}")

#second example

a = 10 
b = 20 

result = f"The result of {a} multiplied by {b} is {a * b}"
print(result)