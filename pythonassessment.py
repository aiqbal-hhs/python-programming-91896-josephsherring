import sys
yeslist = ["yea", "yes", "y", "yeah", "ok"]
nolist = ["no,", "n"]
price = 0
p_max = 0
pizzalist = ("Cheese", "Cheesy Garlic", "pepperoni", "Hawaiian", "Ham and Cheese", "Bacon", "Classic Veggie", "Margherita", "Meat lovers", "Loaded Hawaiian", "Loaded Pepperoni", "Supreme")
order = []

def get_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            break
        except ValueError:
            print("Please make sure you enter an integer value in your answer.\n============================================================")
    return answer


def start():
    run = input("\n\nWould you like to run the program?[y/n]\n>>> ")
    while True:
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        elif run.lower() in yeslist:
            break
        else:
            print("Invalid input. Please enter y/n ")
            run = input(">>> ")
            continue



def delivery():
    global price
    global yeslist
    order_type = str(get_int("\nWould you like to recieve your order via Pick up [1] or delivery [2]\n>>> "))
    while True:
        if order_type == "2":
            price += 3
            print("\n\nOption 2 picked - delivery.")
            address = str(input("\nWhat is the customers address? \n>>> "))
            while True:
                correct = str(input("\nIs this the correct address?[y/n]]\n[{}]\n>>> ".format(address)))
                if correct.lower() in yeslist:
                    break
                else:
                    address = str(input("What is the customers address? \n>>> "))
                    continue
            if correct.lower() not in yeslist:
                continue
            else:
                print("\nContinuing with your order")
                break
        elif order_type == "1":
            print("Option 1 picked - pick up.\n")
            break
        else:
            print("That is not a valid answer! please pick [1] for pick up or [2] for delivery below")
            order_type = str(get_int(">>> "))
            continue


def name():
    name = str(input("What is the customers name?\n>>> "))
    while True:
        correct = str(input("\nIs this the correct Name?[y/n]\n[{}]\n>>> ".format(name)))
        if correct.lower() in yeslist:
            break
        else:
            name = str(input("What is the customers Name? \n>>> "))
            continue


def phone():
    phone_num = str(get_int("What is the customers phone number?\n>>> "))
    while True:
        correct = str(input("\nIs this the correct Phone number?[y/n]\n[{}]\n>>> ".format(phone_num)))
        if correct.lower() in yeslist:
            break
        else:
            phone_num = str(get_int("What is the customers Phone number? \n>>> "))
            continue

def p_function():
    global p_max
    global p_amount
    p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
    p_amount = int(get_int("How many {} pizzas do you want [max 5]\n>>>".format(pizzalist[p_order - 1])))
    p_max += p_amount
    if p_max > 5:
        print("You are only allowed to have a total of 5 pizzas, your order has been removed for that pizza.")
    else:
        order.append(p_amount)
        order.append(pizzalist[p_order - 1])
        print("You have added {} {} ".format(p_amount, pizzalist[p_order - 1]))
#        order['pizza'] = pizzalist[p_order - 1]
        print(order)


def pizza_order():
    print("""\nClassic pizza options: Cost - $8.50 |      Gourmet pizza options: Cost - $13.50
[1] Cheese                           |    [8] Margherita
[2] Cheesy Garlic                    |    [9] Meat Lovers
[3] Pepperoni                        |    [10] Loaded Hawaiian
[4] Hawaiian                         |    [11] Loaded pepperoni
[5] Ham and Cheese                   |    [12] Supreme
[6] Bacon                            |
[7] Classic Veggie                   |
\n""")
    global p_max
    p_max = 0
    p_function()
    global p_amount
    while True:
        if p_amount > 5:
            print("You can only have 5 pizzas sorry!")
            p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
            p_function()
            continue
        elif p_amount < 0:
            print("You can not pick a negative number of pizzas sorry!\n")
            p_function()
            continue
        else:
            p_cont = input("Would you like to order another pizza?[y/n]\n>>> ")
            if p_cont in yeslist:
                p_function()
                continue
            elif p_cont in nolist:
                break
            else:
                print("Invalid input, please try again.")
                continue

def restart():
    global price
    run = input("\n\nWould you like to restart the program?[y/n]\n>>> ")
    while True:
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        elif run.lower() in yeslist:
            break
        else:
            print("Invalid input. Please enter y/n ")
            run = input(">>> ")
            continue
    price = 0
    delivery()
    name()  
    phone()
    pizza_order()
    restart()


start()
delivery()
name()
phone()
pizza_order()
restart()


