import sys
#Allows the program to know that these all mean the same thing
yeslist = ["yea", "yes", "y", "yeah", "ok", "yep"]
nolist = ["no", "n"]
#Sets the price and pizza orders to 0
price = 0
p_max = 0
success = False
#List of all the pizzas and toppings to call back to later
pizzalist = ("Cheese", "Cheesy Garlic", "Pepperoni", "Hawaiian", "Ham and Cheese", "Bacon", "Classic Veggie", "Margherita", "Meat lovers", "Loaded Hawaiian", "Loaded Pepperoni", "Supreme")
toppingslist =  ("With Jalapenos", "With Olives", "With Pineapples", "With Mushrooms", "With Extra Cheese", "With Ham")
#Empty list which is added to create the order
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

def get_yesno(prompt):
    while True:
        answer = str(input(prompt))
        if answer not in yeslist and answer not in nolist:
            print("Please make sure you enter Y/N.\n")
            continue
        else:
            break
    return answer

#defines what start means
def start():
    #asks the user if they would like to run the program
    run = str(get_yesno("Would you like to run the program?[Y/N]\n>>> "))
    #creates a loop so that as long as the user answers incorrectly to the question they will be asked again til a correct answer is provided
    while True:
        #If the user answers one of the answers in the list I created with accetable 'no' answers it will run this
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        #If the user answers with an acceptable 'yes answer from the yeslist then the loop will be stop
        else:
            break



#Defines the delivery function which asks the user about the method of picking up the pizza they want
def delivery():
    global price
    #Asks the user if they want pickup or delivery then stores their answer in order_type
    order_type = str(get_int("\nWould you like to recieve your order via Pick up [1] or delivery [2]\n>>> "))
    #confirms the address is correct with a while loop so when it is incorrect the loop will repeat
    while True:
        if order_type == "2":
            price += 3
            print("\n\nOption 2 picked - delivery.")
            address = str(input("\nWhat is the customers address? \n>>> "))
            correct = str(get_yesno("\nIs this the correct address?[Y/N]]\n[{}]\n>>> ".format(address)))
            if correct.lower() in yeslist:
                break
            else:
                continue
        elif order_type == "1":
            print("Option 1 picked - pick up.\n")
            break
        else:
            print("That is not a valid answer! please pick [1] for pick up or [2] for delivery below")
            order_type = str(get_int(">>> "))
            continue

#Defines the function 'name' which stores the users name and makes sure that it is correct using a loop
def name():
    while True:
        name = str(input("What is the customers name?\n>>> "))
        correct = str(get_yesno("\nIs this the correct Name?[Y/N]\n[{}]\n>>> ".format(name)))
        if correct.lower() in yeslist:
            break
        else:
            continue

#Defines the function 'phone' which stores the users name and makes sure that it is correct using a loop
def phone():
    while True:
        phone_num = str(get_int("\nWhat is the customers phone number?\n>>> "))
        correct = str(get_yesno("\nIs this the correct Phone number?[Y/N]\n[{}]\n>>> ".format(phone_num)))
        if correct.lower() in yeslist:
            break
        else:
            continue

        
#Defines the p_function function which handles the ordering of the pizzas
def p_function():
    global p_max
    global p_amount
    global price
    global p_order
    global success
    success = False
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
    p_amount = int(get_int("How many {} pizzas do you want [max 5]?\n>>>".format(pizzalist[p_order - 1])))
    #Stops p_amount if more than 5 or less than 1
    while True and not success:
        if p_amount > 5 or p_amount <1:
            print("You can only have 5 pizzas sorry!")
            # p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))# #I commented out this#
            p_amount = int(get_int("How many of this pizza do you want?\n>>>")) #I added this line#
            continue
        #elif p_amount <= 0:
       #     print("You can not pick a negative number of pizzas sorry!\n")
       #     continue
        else:
            p_max += p_amount
            while True:
                if p_max >5:
                    print("You cant have that many pizzas sorry")
                    p_max -= p_amount
                    p_amount = int(get_int("How many of this pizza do you want?\n>>>"))
                    p_max +=p_amount
                    continue
                else:
                    print("You have added {} {} pizzas ".format(p_amount, pizzalist[p_order - 1]))
                    if p_order >= 1 and p_order <= 7:
                        price += 8.50 * p_amount
                    else:
                        price += 13.50 * p_amount
                    toppings()
                    #p_amount = 0 
                    break
        
    

def toppings():
    global price
    global success
    success = False
    p_topping = str(get_yesno("Would you like extra toppings for this pizza?[Y/N]\n>>> "))
    if p_topping.lower() in yeslist:
        print("""Extra toppings are 50 cents and the choices are below.
[1] Jalapenos                        |      [4] Mushroom
[2] Olives                           |      [5] Extra Cheese
[3] Pineapples                       |      [6] Ham
\n""")
        topping_choice = int(get_int("Please enter the corresponding number next to the topping you want\n>>> "))
        while True:
            if topping_choice >=1 and topping_choice <= 6:
                price += 0.5*p_amount
                break
            else:
                print("We do not have a topping associated with that number, please enter a number between 1 and 6")
                topping_choice = int(get_int("Please enter the corresponding number to the topping you want\n>>>"))
                continue
    elif p_topping.lower() in nolist:
        print("Ok!")
    #adds to the users total order and displays it
    order.append(p_amount)
    order.append(pizzalist[p_order - 1])
    if p_topping.lower() in yeslist:
        order.append(toppingslist[topping_choice - 1])
    else:
        order.append("with no toppings")
    order.append(",")
    print(*order, sep= " ")
    success = True
    
        
def pizza_order():
    global p_max
    global topping_choice
    global p_topping
    global p_order
    p_max = 0
    global p_amount
    global price
    p_function()
    while True:
        if p_max == 5:
            print("You have reached the limit for pizzas.")
            finalise()
            break
        else:
            if p_amount < 5:
                p_cont = str(get_yesno("Would you like to order another pizza?[Y/N]\n>>> "))
                if p_cont in yeslist:
                    p_function()
                    continue
                else:
                    finalise()
                    break
            else:
                finalise()
                break


def finalise():
    print("You have reached the end of your order!\n")
    cancel = str(input("Would you like to finalise the order[F] or cancel[C]? (cancelling will bring you back to the start of the program)\n"))
    while True:
        if cancel.lower() == "f":
            print("Thank you for using this program, a receipt will be printed below.")
            break
        elif cancel.lower() == "c":
            print("Your order has been cancelled.")
            restart()
        else:
            print("Please enter F to finalise the order or C to cancel the order.")
            cancel = str(input(">>>"))
            continue


def receipt():
    #include customer name with a full stop at the end. Must be at the start and first letter of each name must be a capital.
    # if for delivery, need to include the delivery address
    print(*order, sep= " ")
    print(price)


def restart():
    global price
    global order
    global success
    run = get_yesno("\n\nWould you like to restart the program?[Y/N]\n>>> ")
    while True:
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        else:
            break

    price = 0
    order.clear()
    success = False
    delivery()
    name()  
    phone()
    pizza_order()
    receipt()
    restart()


start()
delivery()
name()
phone()
pizza_order()
receipt()
restart()
