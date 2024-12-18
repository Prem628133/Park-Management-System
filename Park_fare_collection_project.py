print("$#$#$#$# Welcome to the indira park $#$#$#$#$#$#$#$")
print("$#$#$#$# Enter your details to book tickets $#$#$#$#$#$#$#$")

def display_menu():
    print("Choose an Option:")
    print("1. Book Ticket")
    print("2. Check Price")
    print("3. Discounts")
    print("4. No of people visited")


def your_choice(option):
    if option == "1":
       print("Enter your details as follow :")
    elif option =="2":
        print("The prices are as below")
    elif option=="3":
        print("The discounts are as follow")
    elif option == "4":
        print("Total no of visitors")
        exit()
    else:
        print("Invalid Number")
while True:
    user_choice =("Select your choice")
    your_choice(user_choice)

