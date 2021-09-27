import sys
#Allows the program to know that these all mean the same thing
yeslist = ["yea", "yes", "y", "yeah", "ok"]
nolist = ["no,", "n"]
#sets the price and pizza orders to 0
price = 0
p_max = 0
p_check = 0
#List of all the pizzas and toppings to call back to later
pizzalist = ("Cheese", "Cheesy Garlic", "pepperoni", "Hawaiian", "Ham and Cheese", "Bacon", "Classic Veggie", "Margherita", "Meat lovers", "Loaded Hawaiian", "Loaded Pepperoni", "Supreme")
toppingslist =  ("With Jalapenos", "With Olives", "With Pineapples", "With Mushrooms", "With Extra Cheese", "With Ham")
#Empty list which is added to to create the order
order = []

#Defines get_int so when inserted into the code it stops value errors from happening so the program runs smoother
def get_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            break
        except ValueError:
            print("Please make sure you enter an integer value in your answer.\n============================================================")
    return answer

#defines what start means
def start():
    #asks the user if they would like to run the program
    run = input("\n\nWould you like to run the program?[y/n]\n>>> ")
    #creates a loop so that as long as the user answers incorrectly to the question they will be asked again til a correct answer is provided
    while True:
        #If the user answers one of the answers in the list I created with accetable 'no' answers it will run this
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        #If the user answers with an acceptable 'yes answer from the yeslist then the loop will be stopped
        elif run.lower() in yeslist:
            break
        #continues the loop if an answer outside of the accepted yes or no answers are given
        else:
            print("Invalid input. Please enter y/n ")
            run = input(">>> ")
            continue


#Defines the delivery function which asks the user about the method of picking up the pizza they want
def delivery():
    global price
    global yeslist
    #Asks the user if they want pickup or delivery then stores their answer in order_type
    order_type = str(get_int("\nWould you like to recieve your order via Pick up [1] or delivery [2]\n>>> "))
    #confirms the address is correct with a while loop so when it is incorrect the loop will repeat
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
                print("Please enter the correct address")
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

#Defines the function 'name' which stores the users name and makes sure that it is correct using a loop
def name():
    global yeslist
    global nolist
    name = str(input("What is the customers name?\n>>> "))
    while True:
        correct = str(input("\nIs this the correct Name?[y/n]\n[{}]\n>>> ".format(name)))
        if correct.lower() in yeslist:
            break
        elif correct.lower() in nolist:
            name = str(input("What is the customers Name? \n>>> "))
            continue

#Defines the function 'phone' which stores the users name and makes sure that it is correct using a loop
def phone():
    phone_num = str(get_int("What is the customers phone number?\n>>> "))
    while True:
        correct = str(input("\nIs this the correct Phone number?[y/n]\n[{}]\n>>> ".format(phone_num)))
        if correct.lower() in yeslist:
            break
        elif correct.lower() in nolist:
            phone_num = str(get_int("What is the customers Phone number? \n>>> "))
            continue
        else:
            print("That is not a valid answer, please try again and make sure to enter y/n \n")
            phone_num = str(get_int("What is the customers Phone number? \n>>> "))  
            continue

        
#Defines the p_function function which handles the ordering of the pizzas
def p_function():
    global p_max
    global p_check
    global p_amount
    global price
    #shows the user the different options for pizzas and the costs
    print("""\nClassic pizza options: Cost - $8.50 |      Gourmet pizza options: Cost - $13.50
[1] Cheese                           |    [8] Margherita
[2] Cheesy Garlic                    |    [9] Meat Lovers
[3] Pepperoni                        |    [10] Loaded Hawaiian
[4] Hawaiian                         |    [11] Loaded pepperoni
[5] Ham and Cheese                   |    [12] Supreme
[6] Bacon                            |
[7] Classic Veggie                   |
\n""")
    #asks the user what pizza they want
    p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
    #makes sure that the order is between 1 and 12 so that the code does not break
    while True:
        if p_order > 12:
            print("We do not have a pizza associated with that number, please enter a number between 1 and 12")
            p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
            continue
        elif p_order < 1:
            print("We do not have a pizza associated with that number, please enter a number between 1 and 12")
            p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
            continue
        elif p_order >= 1 and p_order <= 7:
            price += 8.50
            break
        elif p_order >= 8 and p_order <= 12:
            price += 13.50
            break
        else:
            break
    p_amount = int(get_int("How many {} pizzas do you want [max 5]\n>>>".format(pizzalist[p_order - 1])))
    print("You have added {} {} pizzas ".format(p_amount, pizzalist[p_order - 1]))
    p_topping = input("Would you like extra toppings for this pizza?[y/n]\n>>> ")
    while True:
        if p_topping.lower() in yeslist:
            print("""Extra toppings are 50 cents and the choices are below.
[1] Jalapenos                        |      [4] Mushroom
[2] Olives                           |      [5] Extra Cheese
[3] Pineapples                       |      [6] Ham
\n""")
            topping_choice = int(get_int("Please select the corresponding number next to the topping you want\n>>> "))
            while True:
                if topping_choice > 6:
                    print("We do not have a topping associated with that number, please enter a number between 1 and 12")
                    topping_choice = int(get_int("Please select the corresponding number to the topping you want\n>>>"))
                    continue
                elif topping_choice < 1:
                    print("We do not have a pizza associated with that number, please enter a number between 1 and 12")
                    topping_choice = int(get_int("Please select the corresponding number to the topping you want\n>>>"))
                    continue
                else:
                    break
        elif p_topping.lower() in nolist:
            print("Ok!")
            break
        else:
            p_topping = input("Sorry that is not a valid answer. Please enter [y/n] below\n>>>")
            continue
    p_check += p_amount
    if p_check > 5:
        print("You are only allowed to have a total of 5 pizzas, your order has been removed for that pizza.")
        p_check -= p_amount
    else:
        p_max += p_check
        order.append(p_amount)
        order.append(pizzalist[p_order - 1])
        if p_topping.lower() in yeslist:
            order.append(toppingslist[topping_choice - 1])
        else:
            order.append("with no topping")
        order.append(",")
        print(*order, sep= " ")

        
def pizza_order():
    global p_check
    global p_max
    p_max = 0
    p_check = 0
    p_function()
    global p_amount
    while True:
        if p_amount > 5:
            print("You can only have 5 pizzas sorry!")
            p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
            p_function()
            continue
        elif p_amount <= 0:
            print("You can not pick a negative number of pizzas sorry!\n")
            p_function()
            continue
        else:
            if p_amount < 5:
                p_cont = input("Would you like to order another pizza?[y/n]\n>>> ")
                if p_cont in yeslist:
                    p_function()
                    continue
                elif p_cont in nolist:
                    break
                else:
                    print("Invalid input, please try again.")
                    continue
            else:
                print("You have reached the end of your order!\n") #give them an option to cancel the order
                break


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
