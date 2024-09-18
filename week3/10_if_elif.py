def what_to_do_now():
    message = "time to"
    promot = "Enter selection(1,2 or 3)."
    user_choice = int(input(promot))


    if user_choice == 1:
        print(message, "eat")
    elif user_choice == 2: 
        print (message, "play")
    elif user_choice == 3:
        print(message, "sleep")
    else:
        print("incorrect selection!")

what_to_do_now()

