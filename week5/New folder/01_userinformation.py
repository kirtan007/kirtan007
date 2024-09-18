
# def collect_user_information(id_counter):
#     # Prompt user for input
#     print("Enter User Information:")
#     name = input("Name: ").strip()
#     age = input("Age: ").strip()
#     email = input("Email Address: ").strip()

#     uniqe_id =id_counter + 1
#     id_counter = uniqe_id

#     print(f"\nUser Information:")
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Email Address: {email}")
#     print(f"Unique ID: {uniqe_id}")

#     return id_counter,uniqe_id,name,age,email

# def main():
#     """
#     Main function to initialize counter and collect user information.
#     """
#     id_counter = 5000
#     id_counter, uniqe_id, name, age, email = collect_user_information(id_counter)

# main()

"""
description :- create a function which create generate unique id  for each user and store user information in a dictionary
Author Sarthak modi


"""
def  collect_user_information(id_counter):
    print("Enter User information")
    name  = input("Name: ")
    age  = input("Age: ")
    email  = input("Email: ")

    unique_id = id_counter + 1
    id_counter = unique_id
    print("User information")
    print("User name :", name)
    print("Useg  age :", age)
    print("User email :", email)
    print("User id :",unique_id)
def main():
    id_counter = 5000
    collect_user_information(id_counter)
main()



